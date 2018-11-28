#include<stdio.h>
#include<string.h>
int main()
{
int t,i,j,l,ans;
char arr[1005];
FILE *fptr,*op;
fptr=fopen("F:/a.txt","r");
op=fopen("F:\co.txt","w");
op=fopen("F:\co.txt","a");
fscanf(fptr,"%d",&t);
for(j=1;j<=t;j++)
{
    ans=0;
 fscanf(fptr,"%s",arr);
l=strlen(arr);
arr[l]='+';
arr[l+1]='\0';
 for(i=1;i<=l;i++)
    if(arr[i]!=arr[i-1])
    ++ans;
 fprintf(op,"Case #%d: %d\n",j,ans);
}
return 0;
}

