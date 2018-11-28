#include <stdio.h>

int main(){

	int test,c=1;
	long long ans1,ans2,max,n,p,temp,i;
	
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	for( scanf("%d",&test) ; test-- ; printf("Case #%d: %lld %lld\n",c++,ans1,ans2) ){
		scanf("%lld%lld",&n,&p);
		max = (1LL<<n)-1LL;
		
		if( p==1LL ) ans1=ans2=0LL;
		else if( p==max+1LL ) ans1=ans2=p-1LL;
		else{
			temp=p>>1LL;
			ans2=0LL;
			for( i=n-1LL ; temp ; i-- ){
				ans2 += 1LL<<i;
				temp/=2LL;
			}
			p=max-p+1LL;
			for( ans1=max ; p ;){
				ans1>>=1LL;
				p>>=1LL;
			}
			ans1<<=1LL;
		}
	}


	return 0;
}

