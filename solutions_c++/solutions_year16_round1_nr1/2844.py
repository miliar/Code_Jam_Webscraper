#include<cstdio>


int main()
{
int i,j,k,t,n,T;
char s[1004],f;
char a[1004],b[1004];
scanf("%d",&T);
for(t=1;t<=T;t++)
	{
    j=0;k=0;
    
    scanf("%s",s);
    f=s[0];
    for(i=1;s[i];i++)
        {
        if(s[i]>=f)
            {
            a[j++]=s[i];
            f = s[i];
            }
        else 
            b[k++]=s[i];
        }	
    
	printf("Case #%d: ",t);
    j--;
	for(;j>=0;j--)
	   {
       printf("%c",a[j]); 
       }
    printf("%c",s[0]); 
    
	for(i=0;i<k;i++)
	   {
       printf("%c",b[i]); 
       }    
    printf("\n");
	}
return 0;
}
