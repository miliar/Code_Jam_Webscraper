#include <cstdio>

using namespace std;

int main()
{
   int count,i,j,m,won[50],won1[50],check=0,index=0;
   float remove=5,n[10],k[10],least=5,temp;
   float n1[10],k1[10];
   int testcase,p;
   scanf("%d",&testcase);
for(p=0;p<testcase;p++)
{
    won[p]=0;
    won1[p]=0;
   scanf("%d",&count);

   for(i=0;i<count;i++)
   {
       scanf("%f",&n[i]);
       n1[i]=n[i];
   }

for(i=0;i<count;i++)
  { scanf("%f",&k[i]);
   k1[i]=k[i];
  }

for(i=0;i<count;i++)
{
for(j=0;j<count-1;j++)
{
if(n[j]>n[j+1])
{
temp=n[j];
n[j]=n[j+1];
n[j+1]=temp;
}
}
}
for(i=0;i<count;i++)
{
for(j=0;j<count-1;j++)
{
if(k[j]>k[j+1])
{
temp=k[j];
k[j]=k[j+1];
k[j+1]=temp;
}
}
}
j=0;
for(i=0;i<count;i++)
{

if(n[i]<k[j])
{

}
else
{
    if(k[j]<n[i])
    {
        won1[p]++;
    }
        j++;

}
}






/******************************************************************/
/******************************************************************/

for(i=0;i<count;i++)
{
for(j=0;j<count-1;j++)
{
if(n1[j]>n1[j+1])
{
temp=n1[j];
n1[j]=n1[j+1];
n1[j+1]=temp;
}
}
}
for(j=0;j<count;j++)
            {
                remove=5;
                check=0;
                least=5;
                for(m=0;m<count;m++)
                {
                    if(k1[m]>-1)
                    {
                    if(k1[m]>n1[j])
                    {
                        if(remove>k1[m])
                        {
                        remove=k1[m];
                        index=m;

                        }
                        check=1;
                    }
                    }
                }
                if(check==0)
                {
                    for(int n=0;n<count;n++)
                    {
                        if(k1[n]>=0)
                        {
                            if(k1[n]<least)
                            {
                                least=k1[n];
                            index=n;

                        }
                    }
                }
                won[p]++;
                }

                k1[index]=-1;
                n1[j]=-1;
            }
}
for(p=0;p<testcase;p++)
    {
     printf("Case #%d: ",p+1);
     printf("%d %d\n",won1[p],won[p]);
    }
return 0;
}
