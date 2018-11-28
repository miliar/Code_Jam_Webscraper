#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
#include<vector>
#include<algorithm>
//#include<conio.h>
 
#define MOD 1000000000
 
using namespace std;
 
int main()
{
int t,n,m;
int sel,tp1,tp2,tp;
int a[200][200];
 
scanf("%d",&t);
 
for(int i=1;i<=t;i++)
{
scanf("%d%d",&n,&m);
 
for(int j=0;j<n;j++)
{
for(int k=0;k<m;k++)
scanf("%d",&a[j][k]);
}
 
tp=0;
 
for(int j=0;j<n;j++)
{
    for(int k=0;k<m;k++)
        {                
                tp1=0;
                tp2=0;
                sel=a[j][k];
        
                
                for(int u=0;u<m;u++) // seeing row wise
                {
                        if(a[j][u]>sel)
            {
                                tp1=1;
                                break;
                        }
                }
                
        for(int u=0;u<n;u++)
                        {
                                if(a[u][k]>sel)
                                {
                                        tp2=1;
                                        break;
                                }
                        }
 
                if(tp1==1&&tp2==1)
                {
                        tp=1;
                        break;
                }
 
        }
 
        if(tp==1)
        break;
}
 
if(tp==1)
printf("\nCase #%d: NO",i);
 
else
printf("\nCase #%d: YES",i);
}
 
//      getch();
        return 0;
}
