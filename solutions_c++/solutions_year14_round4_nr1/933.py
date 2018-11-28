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
#define maxn 10009
int T,n,x;
int a[maxn];
int main()
{
	freopen((filename+".in").c_str(),"r",stdin);
	freopen((filename+".out").c_str(),"w",stdout);
	//freopen((filename+".err").c_str(),"w",stderr);
	scanf("%d",&T);
	int Case=0;
	while(T--){
		printf("Case #%d: ",++Case);
		scanf("%d %d",&n,&x);
		int i;
		for(i=1;i<=n;i++){
			scanf("%d",a+i);
		}
		sort(a+1,a+n+1);
		int j=1,ans=0;
		for(i=n;i>=j;i--){
			if(a[i]+a[j]<=x) j++;
			ans++;
		}
		printf("%d\n",ans);
	}
	return 0;
}
