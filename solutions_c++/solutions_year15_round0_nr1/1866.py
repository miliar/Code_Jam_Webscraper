//#pragma comment(linker,"/STACK:102400000,102400000")
#include<stdio.h>
#include<iostream>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<string>
#define ll long long
#define db double
#define PB push_back
#define lson k<<1
#define rson k<<1|1
using namespace std;

const int N = 1005;

char str[N];

int main()
{
#ifdef PKWV
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
#endif // PKWV
    int T,cas(1);
    scanf("%d",&T);
    while(T--)
    {
        int n;
        scanf("%d",&n);
        scanf("%s",str);
        int s=str[0]-'0',res(0);
        for(int i=1;i<=n;i++)
        {
            if(i>s)
            {
                res+=i-s;
                s=i;
            }
            s+=str[i]-'0';
        }
        printf("Case #%d: %d\n",cas++,res);
    }
    return 0;
}
