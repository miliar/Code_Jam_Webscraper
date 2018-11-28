#include<stdio.h> 
long long ip,i,flag,ret;
#define ss ip=getchar(),flag=1;ret=0;for(;ip<'0'||ip>'9';ip=getchar())if(ip=='-'){flag=-1;ip=getchar();break;}for(;ip>='0'&&ip<='9';ip=getchar())ret=ret*10+ip-'0';ret=ret*flag;
int main()
{	
    FILE *ff,*gg;
    ff = fopen("ans2.txt", "w");
	gg = fopen("A-small-attempt9.txt","r");

	char output_buffer[22];
	output_buffer[21]='\n';
long k,t,x,y,a[4][4],b[4][4],i,j,c=0;
fscanf(gg,"%d",&t);
while(t--)
{fscanf(gg,"%d",&x);x--;c++;
for(i=0;i<4;++i)
for(j=0;j<4;++j)
{fscanf(gg,"%d",&a[i][j]);}
fscanf(gg,"%d",&y);y--;
for(i=0;i<4;++i)
for(j=0;j<4;++j)
{fscanf(gg,"%d",&b[i][j]);}
int e[4],r[4];
int f=0,n;
for(k=0;k<4;++k)
{
e[k]=a[x][k];
for(j=0;j<4;++j)
if(b[y][j]==e[k]){f++;n=e[k];}
}
if(f==0)
fprintf(ff,"Case #%d: Volunteer cheated!\n",c);
else if(f==1)
fprintf(ff,"Case #%d: %d\n",c,n);
else
fprintf(ff,"Case #%d: Bad magician!\n",c);



}	
fclose(ff);
fclose(gg);
return 0;}
