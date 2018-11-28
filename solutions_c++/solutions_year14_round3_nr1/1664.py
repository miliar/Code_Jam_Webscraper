#include <iostream>
#include <cstdio>
#include <vector>
#include <cstdlib>
using namespace std;
#define ll long long
ll gcd(ll a,ll b)
{
    int r;
    while(b>0)
    {
         r=a%b;
         a=b;
         b=r;
    }
    return a;
}
ll num[100];
int main()
{
    freopen("A-small-attempt1.in","r", stdin);
    freopen("out.txt", "w", stdout);
    ll a;
    ll b;
    int tot;
    int cc=0;
    cin >> tot ;
    num[0] = 2;
    for (int i = 1;i < 40;++i)
        num[i] = num[i-1] * 2;

    while (tot--)
    {
        cc++;
        printf("Case #%d: ", cc);
        scanf("%lld/%lld", &a, &b);

        ll t = gcd(a,b);
        b /= t;
        a /= t;
        int i = 0;
        for (; i < 40;++i)
            if(num[i] == b)
                break;
        if (i >= 40)
        {
            cout << "impossible" << endl;
        }
        else
        {
            int times = 0;
            while (a < b)
            {
                a*= 2;
                times++;
            }
            cout << times << endl;
        }

    }
    return 0;
}
/*
有个类 Tools
tool.next_line()去获得下一行。
然后假如一行有int,double,int,struct test,
是不是调用 tool.get(a),tool.get(b),tool.get(c),tool.get(d)就行
*/
