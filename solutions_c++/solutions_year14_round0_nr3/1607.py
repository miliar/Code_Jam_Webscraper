
#include <iostream>
#include <assert.h>
using namespace std;
int cc[100];
int cn;
void an(int x,int r,int c){
	for(int i=0;i<100;i++)
		cc[i]=0;
	cn=0;
	if(x%2==0){
		while(x>=c){
			x-=c;
			cc[cn]=c;
			cn++;
		}
		if(cn==0){
			cc[0]=x/2;
			cc[1]=cc[0];
			cn=2;
			x=0;
		}
		else if(cn==1){
			cc[0]=(x+c)/2;
			cc[1]=cc[0];
			cn++;
			x=0;
		}
		if(x!=0 && x!=1){
			cc[cn]=x;
			cn++;	
		}
		else if(x!=0 && x==1){
			cc[cn-1]--;
			cc[cn]=2;
			cn++;
		}	
	}
	else{
		if(x%c!=1){
			while(x>=c){
				x-=c;
				cc[cn]=c;
				cn++;
			}
			if(c%2==1 && cn==1 && x==2){
				cc[0]--;
				cc[1]=x+1;
				cn++;
				x=0;
			}
			if(c%2==1 && cn==1 && x>2){
				cc[0]-=2;
				cc[1]=x-1;
				cc[2]=3;
				cn+=2;
				x=0;
			}

			if(x!=0){
				cc[cn]=x;
				cn++;
			}
			if(x>=7&& cn==1){
				cc[0]=(x-3)/2;
				cc[1]=cc[0];
				cc[2]=3;
				cn=3;
			}			
		}
		else{
			while(x>2*c){
				x-=c;
				cc[cn]=c;
				cn++;
			}
			if(x!=0){
				cc[cn]=c-1;
				cc[cn+1]=2;
				cn+=2;
				if(cn==3){
					cc[0]--;
					cc[2]++;
				}	

			}
		}
	}
}
int main() {
	int t,i,j,n;
	int r,c,m;
	int a,b;
	int w;
	bool possible;
	cin>>t;
	FILE *fp;
	fp=fopen("ans","w");
	assert(fp!=NULL);

	for(n=0;n<t;n++){
		possible=true;
		cin>>r;
		cin>>c;
		cin>>m;
		//find impossible
		if(r*c-m < 4){
			possible=false;
			if(r==1 || c==1)
				possible=true;
			if(r*c-m == 1)
				possible=true;
		}
		else if((r>=2 && c>=2)&&(r*c-m==7 || r*c-m==5)){
			possible=false;
		}
		else if((r==2 || c==2)&&((r*c-m)%2==1))
			possible=false;

		//impossile
		if(!possible){
			printf("Case #%d:\n",n+1);
			printf("Impossible\n");
			fprintf(fp,"Case #%d:\n",n+1);
			fprintf(fp,"Impossible\n");

			continue;
		}
		//start
		printf("Case #%d:\n",n+1);
		fprintf(fp,"Case #%d:\n",n+1);
		if(c==1){
			for(j=0;j<r;j++){
				if(m>0){
					printf("*\n");
					fprintf(fp,"*\n");
					m--;
				}
				else if(j==r-1){
					printf("c\n");
					fprintf(fp,"c\n");

				}
				else{
					printf(".\n");
					fprintf(fp,".\n");
				}
			}
		}
		else if(r==1){
			for(j=0;j<c;j++){
				if(m>0){
					printf("*");
					fprintf(fp,"*");
					m--;
				}
				else if(j==c-1){
					printf("c");
					fprintf(fp,"c");

				}
				else{
					printf(".");
					fprintf(fp,".");
				}	
			}
			printf("\n");
			fprintf(fp,"\n");
		}
		else if(r*c-m==1){
			for(i=0;i<r;i++)
				for(j=0;j<c;j++){
					if(i==0 &&j==0){
						printf("c");
						fprintf(fp,"c");
					}
					else{
						printf(".");
						fprintf(fp,"*");
						if(j==c-1){
							printf("\n");
							fprintf(fp,"\n");
						}
					}
				}
		}
		else{
			w=r*c-m;
			an(w,r,c);
			for(i=0;i<r;i++)
				for(j=0;j<c;j++){
					if(i==0 && j==0){
						printf("c");
						fprintf(fp,"c");
						cc[0]--;
					}
					else if(i<cn){
						if(cc[i]>0){
							printf(".");
							fprintf(fp,".");
							cc[i]--;
						}
						else{
							printf("*");
							fprintf(fp,"*");
						}
					}
					else{
						printf("*");
						fprintf(fp,"*");
					}
					if(j==c-1){
						printf("\n");
						fprintf(fp,"\n");

					}
				}
		}

	}
	fclose(fp);
	return 0;
}
