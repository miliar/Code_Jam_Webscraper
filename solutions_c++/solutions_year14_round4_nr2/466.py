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

int p[1010];
int ord[1010];
bool comp(const int &a, const int &b){return p[a] < p[b];}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int Tc;
	scanf("%d",&Tc);
	for(int tt=1;tt<=Tc;tt++){
		printf("case #%d: ", tt);
		int n;
		scanf("%d",&n);
		int i, ans = 0;
		for(i=1;i<=n;i++)scanf("%d",p+i);
		for(i=1;i<=n;i++)ord[i] = i;
		sort(ord+1,ord+1+n,comp);
		int R = 1, L = n;
		for(i=1;i<=n;i++){
			if(ord[i] - R < L - ord[i]){
				for(int j=i+1;j<=n;j++)if(R<=ord[j] && ord[j]<ord[i])ord[j]++;
				ans += ord[i] - R;
				ord[i] = R;
				R++;
			}
			else{
				for(int j=i+1;j<=n;j++)if(ord[j]<=L && ord[j]>ord[i])ord[j]--;
				ans += L - ord[i];
				ord[i] = L;
				L--;
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}
