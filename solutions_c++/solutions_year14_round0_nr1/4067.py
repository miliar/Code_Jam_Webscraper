#include<stdio.h>
int main()
{
int t,k=0;
scanf("%d",&t);

while(t--)
{
          
int arr[10][10],r,c,ar[10],br[10],i,j;

scanf("%d",&r);
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
scanf("%d",&arr[i][j]);
}
}

scanf("%d",&c);

for(i=0;i<4;i++)
ar[i]=arr[c-1][i];

for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
scanf("%d",&arr[i][j]);
}
}

scanf("%d",&r);


int f=0,cc=0;

for(i=0;i<4;i++)
br[i]=arr[r-1][i];

for(i=0;i<4;i++)
printf("%d",br[i]);

for(i=0;i<4;i++)
printf("%d",ar[i]);

for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
if(ar[i]==br[j])
{
cc++;
f=ar[i];
}

}
}

if(cc==1)
printf("Case #%d: %d",k++,f);
else if(cc>1)
printf("Case #%d: Bad magician!",k++);
else if(cc==0)
printf("Case #%d: Volunteer cheated!",k++);



}
return 0;
}
