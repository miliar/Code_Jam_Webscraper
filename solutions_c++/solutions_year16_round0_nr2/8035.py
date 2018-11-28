#include<cstdio>
#include<cstring>

using namespace std;

int main()
{
    int t,len,i,cnt,cases=1;
    char str[105];
    scanf("%d",&t);
    while(t--)
    {
                cnt=0;
                scanf("%s",str);
                len=strlen(str);
                for(i=0;i<len-1;i++)
                {
                   if(str[i]==str[i+1]) 
                   {
                   continue;
                   }
                   else 
                   {
                   cnt++;
                   }
                }
                if(str[len-1]=='-')
                {
                cnt++;
                }
                printf("Case #%d: %d\n",cases++,cnt);
               
    }
   
    return 0;
}
