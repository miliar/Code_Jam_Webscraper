#include <bits/stdc++.h>
using namespace std;

int main( ){
	freopen("A-large.in", "r", stdin);
	freopen("saida.txt","w",stdout);
    int t,i=1,cnt;
    int c[15];
    long long n;
    for(scanf("%d",&t);i<=t;i++){
    	scanf("%lld",&n);
    	if(n==0){
    		printf("Case #%d: INSOMNIA\n", i);
    		continue;
		}
    	cnt=0;
    	memset(c,0,sizeof c);
    	for(long long j = 1LL;true;j++){
	    	long long aux = n*j;
	    	while(aux){
	    		if(!c[aux%10LL]) cnt++;
	    		c[aux%10LL] = 1;
	    		aux /= 10LL;
			}
			if(cnt==10){
				printf("Case #%d: %lld\n", i, n*j);
				break;
			}
		}
	}
    return 0;    
}
