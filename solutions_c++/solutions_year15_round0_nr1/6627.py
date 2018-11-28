#include<stdio.h>
#include<stdlib.h>
int main()
{
    char str[10001];
    int i,j,k,t,p,ans=0,n;
    scanf("%d",&t);
    k=1;
    
    while(t--)
    {
              scanf("%d %s",&n,str);
              
              p=0;
              i=0;
              ans=0;
              //printf("%s\n",str);
              
              while(str[i]!='\0')
              {
                         if(p>=i)
                         {
                                 p+=(str[i])-'0';
                                // printf("%d\n",p);
                         }
                         else if(i>p)
                         {
                             j=(i-p);
                             ans+=j;
                             p+=j;
                             p+=str[i]-'0';
                             //printf("%d %d\n",i,p);
                         }
                         
                         i++;
              }
              
            //  printf("%d\n",i);
              printf("Case #%d: %d\n",k,ans);
              k++;
    }           
    
    return 0;
}
