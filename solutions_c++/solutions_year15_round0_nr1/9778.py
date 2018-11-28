#include<stdio.h>
int main(void){
	int t,i,j,stand,need,ccc;
	int s_lev,s_str; //small : 0~6
	int shy[1001];
	char shy_c[1001];
	FILE *f,*f2;

	f=fopen("A-small-attempt0.in","r+");
	f2=fopen("output.txt","w+");

	ccc=0;
	fscanf(f,"%d",&t);
	while(t--){	
		ccc++;
		for(i=0;i<1001;i++){shy[i]=0;}

		fscanf(f,"%d",&s_lev);
		fscanf(f,"%s",shy_c);
		for(i=0;i<=s_lev;i++){		
			shy[i]=shy_c[i]-'0';
		}
		need=0;
		stand=shy[0];
		for(i=1;i<=s_lev;i++){
			if(shy[i]!=0){
				if(stand<i){
					need+=i-stand;
					stand+=need;
				}
			}
			stand+=shy[i];
		}
		fprintf(f2,"Case #%d: %d\n",ccc,need);

	}
	return 0;
}