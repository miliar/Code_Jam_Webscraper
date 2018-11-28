#include <cstdio>
#include <algorithm>
using namespace std;
long long tc,tc_cnt,r,mid,n,le,ri,re,t;
//long double t; 
int main(void)
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%lld",&tc);
	while(tc--){
		scanf("%lld %lld",&r,&t);
		n=0;
		le=0;
		ri=1;
		for(int i=0; i<9; i++){
			if(2*ri*ri*100+(2*r-1)*ri*10<=t)
				ri*=10;
			else break;
		}
		ri*=10;
		while(le<=ri){
			mid=(le+ri)/2;
			re=mid*mid*2;
			re+=(2*r-1)*mid;
			if(re<=t){
				n=max(mid,n);
				le=mid+1;
			}
			else ri=mid-1;
		
		}
		tc_cnt++;
		printf("Case #%lld: %lld\n",tc_cnt,n);
	}


	return 0;
}