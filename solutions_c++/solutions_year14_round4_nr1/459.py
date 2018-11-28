#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<vector>
#include<math.h>
#include<stdlib.h>
#include<set>
#include<ctype.h>
using namespace std;

#define X first
#define Y second
typedef long long ll;
typedef pair<int,int> Pi;

int p[10010];
int cnt[710];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	int tt;
	for(tt=1;tt<=T;tt++){
		printf("Case #%d: ", tt);
		int i;
		int n, d;
		scanf("%d%d",&n,&d);
		for(i=1;i<=n;i++)scanf("%d",p+i);
		int ans = 0;
		for(i=1;i<=d;i++)cnt[i] = 0;
		for(i=1;i<=n;i++)cnt[p[i]]++;
		for(i=1;i<=d;i++){
			for(int j=0;j<cnt[i];j++){
				int t = d - i;
				for(;t>=i;t--){
					if(cnt[t]>0){cnt[t]--;break;}
				}
				++ans;
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}
