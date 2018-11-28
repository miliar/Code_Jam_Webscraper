#include<iostream>

using namespace std;

int main()
{

int t,m,n,a[4][4],b[4][4],p=0,k,i,j,u;
scanf("%d",&t);
u=t;
while(t--)
{
	p=0;
scanf(" %d",&m);
for(i=0;i<4;i++)
{for(j=0;j<4;j++)
scanf("%d",&a[i][j]);
}
scanf("%d",&n);
for(i=0;i<4;i++)
{for(j=0;j<4;j++)
scanf("%d",&b[i][j]);
}
for(j=0;j<4;j++)
{
for(i=0;i<4;i++)
{if(a[m-1][j]==b[n-1][i])
{p++;
k=a[m-1][j];
}

}

}
if(p==1)
printf("Case #%d: %d \n",u-t,k);
if(p>1)
printf("Case #%d: Bad magician!\n",u-t);
if(p==0)
printf("Case #%d: Volunteer cheated!\n",u-t);
}
return 0;
}
