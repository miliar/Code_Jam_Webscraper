#include<cstdio>

using namespace std;

int main(void){
	int a,b,k,t,tt;
	scanf("%d",&t);
	for(tt=1;tt<=t;tt++){
	    scanf("%d %d %d",&a,&b,&k);
	    int res=0;
	    for(int i=0; i<a; i++){
	        for(int j=0; j<b; j++){
	            res += (i&j)<k ? 1 : 0;
	        }
	    }
	    printf("Case #%d: %d\n",tt, res);
	}
	return 0;
}
