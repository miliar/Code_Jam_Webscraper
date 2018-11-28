#include<stdio.h>
#include<string.h>
int main()
{
int t,n,i,j,l,in,en;
char st[2000],ne[5000],t1[5],t2[5];
FILE *fptr,*op;
fptr=fopen("a.txt","r");
op=fopen("co2.txt","w");
op=fopen("co2.txt","a");
fscanf(fptr,"%d",&t);
for(j=1;j<=t;j++)
{
    in=2000;en=2001;
fscanf(fptr,"%s",st);
l=strlen(st);
ne[en++]=st[0];
i=1;
if(st[i]>st[0])
    ne[in--]=st[i];
else
    ne[en++]=st[i];
for(i=2;i<l;i++)
{
    t1[0]=st[i];t1[1]=ne[in+1];t1[2]=ne[en-1];t1[3]='\0';
    t2[0]=ne[in+1];t2[1]=ne[en-1];t2[2]=st[i];t2[3]='\0';
    if(strcmp(t1,t2)>0)
           ne[in--]=st[i];
    else
        ne[en++]=st[i];
}
   ne[en]='\0';
 fprintf(op,"Case #%d: %s\n",j,&ne[in+1]);
}
return 0;
}

