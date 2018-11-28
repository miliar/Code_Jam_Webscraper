#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cassert>
#include <queue>
#include <iostream>
using namespace std;

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define lb(x) ((x)&(-(x)))
#define ms(x,y) memset(x,y,sizeof(x))
typedef vector<int> VI;
typedef long long ll;
typedef pair<int,int> PI;
const ll mod=1000000007;
const int inf=0x20202020;
const int N=105;
//head
int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int p[27];
	int tc,n;
	scanf("%d",&tc);
	for(int cc=1;cc<=tc;cc++) {
		printf("Case #%d: ",cc);
		scanf("%d",&n);
		int cnt=0,maxp=0,maxi;
		for(int i=1;i<=n;i++)
		{
			scanf("%d",&p[i]);
			if(p[i]>maxp) {
				maxp=p[i];
				maxi=i;
			}
			cnt+=p[i];
		}
		//printf("%d",cnt);
		if(cnt%2==1){
			p[maxi]--;
			printf("%c",'A'-1+maxi);
			cnt=2;
		}
		else cnt=0;
		while(true)
		{
			maxp=0;maxi=-1;
			for(int i=1;i<=n;i++)
				if(maxp<p[i]) {
					maxp=p[i];
					maxi=i;
				}
			if(maxi==-1)break;
			if(cnt!=0 && cnt%2==0)printf(" ");
			cnt++;
			p[maxi]--;
			printf("%c",'A'-1+maxi);
		}
		printf("\n");
	}
	return 0;
}
