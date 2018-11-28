#include <iostream>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<stack>
#include<queue>
#include<list>
#include<cmath>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<fstream>
#include<map>
#include<iomanip>
using namespace std;
#define whiel while
#define itn int
#define null NULL
#define eps 1e-8
#define INF 0x3f3f3f
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
#define read(x) scanf("%d",&x)
using namespace std;

int main()
{
    #ifndef ONLINE_JUDGE
    freopen("D:\\ceshi.txt","r",stdin);
    #endif
    //ios::sync_with_stdio(false);//无法用scanf和输入挂

    long long n;
    bool num[15];
    int temp=1;
    int T;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%I64d",&n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",temp);
            temp++;
            continue;
        }
        memset(num,false,sizeof(num));
        long long t=1;
        long long k=0;
        int flag=0;
        long long ans=0;
        while(true)
        {
            k=n*t;
            ans=k;
            while(k)
            {
                int x=k%10;
                num[x]=true;
                k/=10;
            }
            flag=0;
            for(int i=0; i<=9; i++)
            {
                if(num[i]==false)
                {
                    flag=1;
                    break;
                }
            }
            if(flag==0)
            {
                break;
            }
            t++;
        }
        printf("Case #%d: %I64d\n",temp,ans);
        temp++;
    }





    return 0;
}
