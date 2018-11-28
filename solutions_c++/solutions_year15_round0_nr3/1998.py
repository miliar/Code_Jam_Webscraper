#include <bits/stdc++.h>
using namespace std;
#define length(x) (int)x.size()
const double pi=acos(-1);

int mh[5][5] = {0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 0, 2, -1, 4, -3, 0, 3, -4, -1, 2, 0, 4, 3, -2, -1};
int a[1000000], f[100000];

void get(int &res, int &sign, int x, int t)
{
    if (t==1) res = mh[res][x]; else res = mh[x][res];
    if (res<0)
    {
        res = -res; sign = -sign;
    }
}

bool solve()
{
    int L, X;   cin>>L>>X;
    string st;  cin>>st;
    for(int i=1; i<=L; i++)
        for(int j=0; j<X; j++)
            if (st[i-1]=='i') a[j*L+i] = 2; else
                if (st[i-1]=='j') a[j*L+i] = 3; else a[j*L+i] = 4;
    int res = 1, sign = 1;
    for(int i=L*X; i>=1; i--)
    {
        get(res, sign, a[i], 2);
        f[i] = res * sign;
    }
    res = 1; sign = 1;
    for(int i=1; i<=L*X-2; i++)
    {
        get(res, sign, a[i], 1);
        if (res==2&&sign==1)
        {
            int res1 = 1, sign1 = 1;
            for(int j=i+1; j<=L*X-1; j++)
            {
                get(res1, sign1, a[j], 1);
                if (res1==3&&sign1==1)
                {
                    if (f[j+1]==4) return true;
                }
            }
        }
    }
    return false;
}

int main()
{
    freopen("input.inp","r",stdin);
    freopen("output.out","w",stdout);
    int test;   cin>>test;
    for(int t=1; t<=test; t++)
    {
        cout<<"Case #"<<t<<": ";
        if (solve()) cout<<"YES"<<endl; else cout<<"NO"<<endl;
    }
    return 0;
}
