//hi
#include<bits/stdc++.h>
using namespace std;
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define LL long long int
int use[10];
void go(LL d){
	while(d){
		use[d%10]=1;
		d=d/10;
	}
}
int main(void){
    int t,hh;
    scanf("%d",&t);
    for(hh=1;hh<=t;hh++){
		LL n;
		scanf("%lld",&n);
		if(n==0) printf("Case #%d: INSOMNIA\n",hh);
		else{
			int i,j;
			for(i=0;i<10;i++) use[i]=0;
			for(i=1;;i++){
				LL d=n*i;
				go(d);
				for(j=0;j<10;j++) if(!use[j]) break;
				if(j==10) break;
			}
			printf("Case #%d: %lld\n",hh,i*n);
		}
	}
    return 0;
}
