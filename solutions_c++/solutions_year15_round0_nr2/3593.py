#include <cstdio>
#include <algorithm>
using namespace std;

int main(){
	
	int D,T;
	int P[1000];
	
	scanf(" %d",&T);
	
	for(int i=1;i<=T;i++){
	    
	    int mx=0;
	    scanf(" %d",&D);
	    for(int j=0;j<D;j++){
	        scanf(" %d",&P[j]);
	        mx = max(mx,P[j]);
	    }
	    
	    int res = 0x7fffffff;
	    
	    for(int j=1;j<=mx;j++){
	        int rev=j;
	        for(int k=0;k<D;k++)
	            rev+=(P[k]-1)/j;
	        res = min(res,rev);
	    }
	    
	    printf("Case #%d: %d\n",i,res);
	}
	

	return 0;
}
