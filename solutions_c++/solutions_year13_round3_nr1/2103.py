#include<stdio.h>
#include<math.h>
#include<string.h>
#define MAX 10000
int a[MAX];
int main()
{
    char str[MAX];
    int i,test,j,m,n,p,k,len,result,totlen;
    scanf("%d",&test);
    i=0;
    while(m<test)
    {
        scanf("%s%d",str,&n);
        len=strlen(str);
        for(i=0;i<=len-n;i++)
        {
            for(j=i,p=0;p<n;j++,p++)
            {
                if(str[j]=='a'||str[j]=='e'||str[j]=='i'||str[j]=='o'||str[j]=='u')
                {
                    a[i]=0;
                    break;
                }
                else
                {
                    a[i]=n;
                }
            }
        }

        result=0;
        totlen=len;
        k=0;
        for(i=0;i<=len-n;i++)
        {
           // printf("%d ",a[i]);
            if(a[i]==n)
            {
                result+=(len-i-n+1)+k*(len-i-n+1);
                totlen--;
                k=0;
            }
            else
            {
                k++;
            }
        }
        printf("Case #%d: %d\n",m+1,result);
        m++;
    }
    return 0;
}
