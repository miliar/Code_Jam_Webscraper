#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define eps 1e-9
int tc,tcn,cnt;
long double c,f,x,re,d[200002],ans[200002];
int main(void){
	//freopen("B-large.in","r",stdin);
	//freopen("output.txt","w",stdout);
	scanf("%d",&tc);
	while(tc--){
		re=0;
		scanf("%Lf %Lf %Lf",&c,&f,&x);
		if(x<=2.0+eps){
			re=x/2.0;
		}
		else{
			re=x/2.0;
			
		//	cnt=(int)((x-2.0)/f);
		//	if(cnt){
				if( 2.0+(long double)cnt*f < x )
					cnt++;
				memset(d,0,sizeof(d));
				for(int i=0; i<=x; i++){
					d[i]=c/(2.0+f*(long double)i);
					if( i )
						d[i]+=d[i-1];
					ans[i]=d[i] + x/( 2.0+(long double)(i+1)*f);
					re=min( re, ans[i] );
			//		if ( re >= ans[i] )
				//		re=ans[i];
				//	else break;
				}
			//}
			//re+=x/( 2.0+(long double)cnt*f );

		}
		printf("Case #%d: %.7Lf\n",++tcn,re);
	}

	return 0;
}