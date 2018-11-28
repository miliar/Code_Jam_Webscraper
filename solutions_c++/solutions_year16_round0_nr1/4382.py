#include <iostream>
#include <cstdio>
using namespace std;
int had[10];
int main(){
	int T,cases,x,y,m;
	freopen("A-large.in.txt","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for (int cases=1;cases<=T;cases++){
		printf("Case #%d: ",cases);
		scanf("%d",&x);
		if (!x) puts("INSOMNIA");
		    else{
		    	m=y=0;
		    	memset(had,false,sizeof(had));
		    	while (m!=10){
		    		y+=x;
		    		int t=y;
		    		while (t){
		    			if (!had[t%10])
		    				had[t%10]=true,m++;
		    			t/=10;
		    		}
		    	}
		    	printf("%d\n",y);
		    }
	}
	return 0;
}