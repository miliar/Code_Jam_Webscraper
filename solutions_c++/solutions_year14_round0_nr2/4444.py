#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

#define fr(a,b,c) for(int a=b;a<c;a++)
#define rp(a,b) fr(a,0,b)
#define cl(a,b) memset(a,b,sizeof(a))

double a,b,c;

int main(){
	int t; scanf("%d",&t); t++;
	fr(cas,1,t){
		scanf("%lf%lf%lf",&a,&b,&c);
		double d=2.0;
		double ans=0;
		while(true){
			if(ans + (c/d) < (ans+(a/d)+(c/(d+b)))){
				ans+=(c/d);
				break;
			}else{
				ans+=(a/d);
				d+=b;
			}
		}
		printf("Case #%d: %.7lf\n",cas,ans);
	}
	return 0;
}