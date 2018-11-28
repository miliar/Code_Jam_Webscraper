#include<stdio.h>

int main()
{

int a[4][4],b[4],c[4];
int t,i,j,cn=0,r,a1,a2,f=1;
scanf("%d",&t);

while(t--)
{
	
cn=0;
scanf("%d",&a1);
for(i=0;i<4;i++)
{
    for(j=0;j<4;j++)
    {
    
    scanf("%d",&a[i][j]);if(i==a1-1)b[j]=a[i][j];
}
}	
scanf("%d",&a2);
for(i=0;i<4;i++)
{
    for(j=0;j<4;j++)
    {
    
    scanf("%d",&a[i][j]);if(i==a2-1)c[j]=a[i][j];
    }
}
for(i=0;i<4;i++)
{
	for(j=0;j<4;j++)
	{
		if(b[i]==c[j])
		{
		cn++;r=b[i];}
	}
}
//printf("%d\n",cn);
if(cn==0)
printf("Case #%d: Volunteer cheated!\n",f);
else if(cn==1)
printf( "Case #%d: %d\n",f,r);
else if(cn>1)
printf("Case #%d: Bad magician!\n",f);

f++;
}
return 0;
}
