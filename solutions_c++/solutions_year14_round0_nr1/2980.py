#include <cstdio>

int main(){
	long t;
	scanf("%ld",&t);
	for(long g=1; g<=t; g++){
		long a,b,x[10],y[10];
		for(long v=0; v<2; v++){
			scanf("%ld",v==0?&a:&b);
			for(long i=1; i<=4; i++)
				for(long j=0; j<4; j++)
					if(i==(v==0?a:b)) scanf("%ld",v==0?&x[j]:&y[j]);
					else scanf("%*ld");
		}
		long res=-1;
		for(long i=0; i<4 && res!=-2; i++)
			for(long j=0; j<4; j++)
				if(x[i]==y[j] && res==-1) res = x[i];
				else if(x[i]==y[j] && res!=-1){
					res = -2;
					break;
				}
		printf("Case #%ld: ",g);
		if(res==-1) printf("Volunteer cheated!\n");
		else if(res==-2) printf("Bad magician!\n");
		else printf("%ld\n",res);
	}
}
	