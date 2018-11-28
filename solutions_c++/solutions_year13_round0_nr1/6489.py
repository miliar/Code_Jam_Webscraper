#include<conio.h>
#include<stdio.h>
using namespace std;
int main(){
    freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);    
    int i,j,k,m,n;
    char a[4][4];
    scanf("%d",&n);
    getchar();
    for(i=1;i<=n;i++){
		int flag=0,fp=0,fx[4][2],fo[4][2],ft[4][2];
		for(j=0;j<4;j++)
			for(k=0;k<2;k++)
				fx[j][k]=fo[j][k]=ft[j][k]=0;
		printf("Case #%d: ",i);
		if(i!=1)getchar();
	    for(j=0;j<4;j++){
            for(k=0;k<4;k++){
				scanf("%c",&a[j][k]);
				if(a[j][k]=='.')fp++;
				else if(a[j][k]=='X'){
					fx[j][0]++;
					fx[k][1]++;
				}
				else if(a[j][k]=='O'){
					fo[j][0]++;
					fo[k][1]++;
				}
				else if(a[j][k]=='T'){
					ft[j][0]++;
					ft[k][1]++;
				}
			}
			getchar();
        }
        for(j=0;j<4;j++){
			if(flag==1)break;
			for(k=0;k<2;k++){
				if((fo[j][k]+ft[j][k])==4){
					printf("O won\n");
					flag=1;
					break;	
				}
				else if((fx[j][k]+ft[j][k])==4){
					printf("X won\n");
					flag=1;
					break;	
				}
			}
		}
		int foo,fxx,ftt;
		if(flag==0){
			foo=fxx=ftt=0;
			for(j=0;j<4;j++){
				if(a[j][j]=='X')fxx++;
				else if(a[j][j]=='O')foo++;
				else if(a[j][j]=='T')ftt++;	
			}
			if((foo+ftt)==4){
				printf("O won\n");
				flag=1;
			}
			else if((fxx+ftt)==4){
				printf("X won\n");
				flag=1;
			}
		}
		if(flag==0){
			foo=fxx=ftt=0;
			for(j=0;j<4;j++){
				if(a[j][3-j]=='X')fxx++;
				else if(a[j][3-j]=='O')foo++;
				else if(a[j][3-j]=='T')ftt++;	
			}
			if((foo+ftt)==4){
				printf("O won\n");
				flag=1;
			}
			else if((fxx+ftt)==4){
				printf("X won\n");
				flag=1;
			}
		}
		if(flag==0){
			if(fp>0)printf("Game has not completed\n");
			else printf("Draw\n");
		}
    }
    getch();
    return 1;
}
