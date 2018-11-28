/**

¼ªÁÖ´óÑ§
Jilin U

Author:     sinianluoye (JLU_LiChuang)
Date:        2015-3
Usage:

**/

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

#define ll long long
#define eps 1e-8
#define ms(x,y) (memset(x,y,sizeof(x)))
#define fr(i,x,y) for(int i=x;i<=y;i++)
#define sqr(x) ((x)*(x))

using namespace std;

const int maxn=1e3+10;
char ch[maxn];

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;
    cin>>T;
    int cas=0;
    while(T--)
    {
        printf("Case #%d: ",++cas);

        int n;
        cin>>n;
        scanf("%s",ch);
        int t=ch[0]-'0',ans=0;
        for(int i=1;i<=n;i++)
        {
            if(ch[i]!='0')
            {
                if(t<i)
                {
                    ans+=i-t;
                    t=i;
                }
                t+=ch[i]-'0';
            }
        }
        printf("%d\n",ans);
    }
}

/*************copyright by sinianluoye (JLU_LiChuang)***********/
