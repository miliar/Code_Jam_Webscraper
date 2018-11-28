#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;
#define N 100010
char s[N];
int main()
{
    int T,i1=1,i,len;
    int ans,flag,tmp;
//    freopen("B-large.in","r",stdin);
//    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        flag=0,ans=0,tmp=0;
        scanf("%s",s);
        len=strlen(s);
        for(i=0;i<len;i++)
        {
            if(s[i]=='+')
            {
                if(tmp)
                    ans+=(flag+1);
                tmp=0;
                flag=1;
            }
            if(s[i]=='-')
            {
                tmp=1;
            }
        }
        if(tmp)
            ans+=(flag+1);
        tmp=0;
        printf("Case #%d: %d\n",i1++,ans);
    }
    return 0;
}
