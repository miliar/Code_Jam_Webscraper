#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <vector>
#include <cctype>
#include <memory.h>
#include<conio.h>

using namespace std;

int main()
{
FILE *fp, *fs;

fp= fopen("input.txt","r");
fs= fopen("output.out","w");    


int t,m,n,chk;
int i,j,k;

fscanf(fp,"%d",&t);    

for(k=1;k<=t;k++)
{

fscanf(fp,"%d",&m);
fscanf(fp,"%d",&n);

int a[m][n],r[m],c[n];
memset(r,0,sizeof(r));
memset(c,0,sizeof(c));

for(i=0;i<m;i++)
   {                 
   for(j=0;j<n;j++)
      {
          fscanf(fp,"%d",&a[i][j]);
          if(r[i]< a[i][j]) 
                   r[i]=a[i][j];
                   
          if(c[j]< a[i][j])
                   c[j]=a[i][j];                     
      }
   }           

chk=1;
for (i=0;i<m;i++)
    {
    for(j=0;j<n;j++)
        {
        if(a[i][j]!= min(r[i],c[j]))
             chk=0;           
        }                
    }             
                 
if (chk==1)    
fprintf(fs,"Case #%d: YES\n",k);
else fprintf(fs,"Case #%d: NO\n",k);              
}

return 0;
}
