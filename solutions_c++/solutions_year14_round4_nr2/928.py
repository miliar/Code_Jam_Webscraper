#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <utility>
#include <iomanip>
#include <string>
using namespace std;
string filename(__FILE__,string(__FILE__).find(".cpp"));
#define PB push_back
#define MP make_pair
#define REP(x,a) for(__typeof(a.begin()) x=a.begin();x!=a.end();x++)
#define SIZE(a) ((int)a.size())
#define ACS(a,b) ((a)?(a)->b:0)
#define EACS(a,b,c) ((a)?(a)->b:(c))
#define ft first
#define sd second
#define maxn 1009
int T;
int x[maxn];
int a[maxn],b[maxn];
int main()
{
	freopen((filename+".in").c_str(),"r",stdin);
	freopen((filename+".out").c_str(),"w",stdout);
	//freopen((filename+".err").c_str(),"w",stderr);
	scanf("%d",&T);
	int Case=0;
	while(T--){
		printf("Case #%d: ",++Case);
		int n;
		scanf("%d",&n);
		int i,j;
		for(i=1;i<=n;i++){
			scanf("%d",x+i);
		}
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		for(i=1;i<=n;i++){
			for(j=i+1;j<=n;j++){
				if(x[i]>x[j]){
					a[j]++;
				}else{
					b[i]++;
				}
			}
		}
		int ans=0;
		for(i=1;i<=n;i++){
			ans+=min(a[i],b[i]);
		}
		printf("%d\n",ans);
	}
	return 0;
}
