#include<iostream>
#include<cstdlib>
#include<cstdio>
using namespace std;
int n;
char ch[1111];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int tot;
    scanf("%d",&tot);
    for(int tit=1;tit<=tot;tit++)
    {
        scanf("%d%s",&n,ch);
        int st=0,need=0;
        for(int i=0;i<=n;i++)
        {
            if(st<i)
            {
                need+=i-st;
                st=i;
            }
            st+=ch[i]-'0';
        }
        printf("Case #%d: %d\n",tit,need);
    }
}
