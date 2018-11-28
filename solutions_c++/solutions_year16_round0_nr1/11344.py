#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
typedef long long LL;
int t,n;
int num[15];

bool judge(LL x,int ii)
{
    LL tmp = x * n;
    LL ans = tmp;
    while(tmp != 0)
    {
        int temp = tmp % 10;
        tmp = tmp / 10;
        num[temp] = 1;
    }

    for(int i = 0 ; i < 10 ; i++)
    {
        if(num[i] == 0)
            return false;
    }
    cout<<"Case #"<<ii<<": "<<ans<<endl;
    return true;
}
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    cin >> t;
    for(int ii = 1 ;ii <= t ;ii++)
    {
        bool flag = false;
        cin >> n;
        memset(num,0,sizeof(num));
        for(int i = 1 ; i <= 2000 ; i++)
        {
            if(judge(i,ii))
            {
                flag = true;
                break;
            }
        }

        if(!flag)
           cout<<"Case #"<<ii<<": INSOMNIA"<<endl;
    }
    return 0;
}
