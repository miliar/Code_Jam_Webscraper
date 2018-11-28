/*
ID: 1292871202
LANG: C++
*/
#pragma comment(linker,"/STACK:102400000,102400000")
#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <fstream>
#include <utility>

using namespace std;

typedef long long ll;

const int INF = 0x3f3f3f3f;
const int MAX = 0x7fffffff;
const ll LINF = 0x3f3f3f3f3f3f3f3fLL;
const ll LMAX = 0x7fffffffffffffffLL;
const double eps = 1e-9;
const double pi=acos(-1.0);

const int maxn = 100000+5;
const int maxm = 100000+5;
const int mod = 1e9+7;

#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1


int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    //cin.sync_with_stdio(false);
    //cout.sync_with_stdio(false);

    int t;cin>>t;

    for(int case_i=1;case_i<=t;++case_i)
    {
        cout<<"Case #"<<case_i<<": ";
        ll n;cin>>n;
        if(n==0)
        {
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        int flag=0;
        int aim = 0x3ff;
        ll k=1;

        ll ans=-1;
        while(1)
        {
            ll tem=k*n;
            while(tem)
            {
                flag=flag|(1<<(tem%10));
                tem/=10;
            }
            if(flag==aim)
            {
                cout<<k*n<<endl;
                break;
            }
            k++;
        }
    }
    return 0;
}
