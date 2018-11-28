#include<stdio.h>
#include<string.h>
int coun[29],h,s,n;
void sets()
{
int i;
h=27;s=27;
for(i=0;i<n;i++)
if(coun[i]>=coun[h])
{s=h;h=i;}
else if (coun[i]>=coun[s])
s=i;
return;
}
int main()
{
    int t,i,j,k;
FILE *fptr,*op;
fptr=fopen("A.in","r");
op=fopen("co.txt","w");
op=fopen("co.txt","a");
fscanf(fptr,"%d",&t);
coun[27]=0;
for(j=1;j<=t;j++)
{
h=27;s=27;k=0;
fscanf(fptr,"%d",&n);

for(i=0;i<n;i++)
    {fscanf(fptr,"%d",coun+i);
    k+=coun[i];
    }
sets();
 fprintf(op,"Case #%d:",j,k);
 while(k){
fprintf(op," %c",65+h);
--k;--coun[h];
sets();
if(coun[h] > (k)/2)
{fprintf(op,"%c",65+h);
--k;--coun[h];
}
if(coun[s]>coun[h])
sets();

}

 fprintf(op,"\n");
}

return 0;
}

