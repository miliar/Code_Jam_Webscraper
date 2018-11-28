#include <cstdio>
using namespace std;

int t,tab[5],tabp[5],i,j,k,l,p,moz,mozw;

int main(){
	scanf("%d", &t);
	for(i=0;i<t;i++){
		scanf("%d", &p);
		for(j=1;j<=4;j++){
			for(k=0;k<4;k++) scanf("%d", &tab[k]);
			if(j==p) for(k=0;k<4;k++) tabp[k]=tab[k];
		}
		scanf("%d", &p);
		moz=0;
		for(j=1;j<=4;j++){
			for(k=0;k<4;k++) scanf("%d", &tab[k]);
			if(j==p) 
				for(k=0;k<4;k++)
					for(l=0;l<4;l++) if(tab[k]==tabp[l]){ moz++; mozw=tab[k];}
			 	
		}
		printf("Case #%d: ", i+1);
		if(moz==1) printf("%d\n", mozw);
		else if(moz==0) printf("Volunteer cheated!\n");
		else printf("Bad magician!\n");
	}
	return 0;
}
