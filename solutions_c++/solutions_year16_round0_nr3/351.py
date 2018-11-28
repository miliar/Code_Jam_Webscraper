#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
using namespace std;

const int MAXP = 1000000;
const int MAXN = 100000;

long long T;
long long N, J;
long long bits[40];
long long cnt;
bool number[MAXP];
long long prime[MAXN];
long long divisor[15];

long long getRem(long long base, long long pw, long long mod)
{
    if( pw == 0 ) return 1;
    if( pw == 1 ) return base%mod;

    if( pw % 2 == 0 )
    {
        long long r = getRem(base, pw/2, mod);
        return r*r%mod;
    }
    else
    {
        int r = getRem(base, pw-1, mod);
        return r*base%mod;
    }
}
bool judge()
{
    memset(divisor,-1,sizeof(divisor));
    for(int base=2;base<=10;base++)
    {
        long double numval = 0;
        for(int i=1;i<=N;i++)
            if( bits[i] != 0 )
                numval += pow(base,N-i);
        if( numval < MAXP )
            if( number[(int)numval] == false )
                return false;
        for(int p=1;p<prime[0];p++)
        {
            long long rem = 0;
            for(int i=1;i<=N;i++)
            {
                if( bits[i] == 0 ) continue;
                rem += getRem((long long)base, (long long)(N-i),prime[p]);
                rem %= prime[p];
//                if( rem < 0 ){
//                    cout << rem << endl;
//                    cout << base << endl;
//                    for(int i=1;i<=N;i++)
//                    {
//                        cout << bits[i];
//                    }
//                    cout << endl;
//                }
            }
            if( rem == 0 )
            {
                divisor[base] = prime[p];
                break;
            }
        }
        if( divisor[base] == -1 ) return false;
    }
    for(int i=1;i<=N;i++) cout << bits[i]; cout << " ";
    for(int i=2;i<10;i++) cout << divisor[i] << " "; cout << divisor[10] << endl;
    return true;
}
bool dfs(int x)
{
    if( x == N )
    {
        if( judge() == true )
            cnt++;
        if( cnt == J ) return true;
        else return false;
    }
    bits[x] = 0;
    if( dfs(x+1) == true ) return true;
    bits[x] = 1;
    if( dfs(x+1) == true ) return true;
}
void solve()
{
    cnt = 0;
    bits[1] = 1;
    bits[N] = 1;
    dfs(2);
}
void getprime()
{
    memset(number,false,sizeof(number));
    for(int i=2;i<=(int)sqrt(MAXP)+1;i++)
    {
        if( number[i] == true ) continue;
        else
        {
            for(int j=i*i;j<MAXP;j=j+i)
            {
                number[j] = true;
            }
        }
    }
    prime[0] = 0;
    for(int i=2;i<MAXP;i++)
    {
        if( number[i] == false )
        {
            prime[0]++;
            prime[prime[0]] = i;
        }
    }
//    for(int i=1;i<=prime[0];i++)
//        cout << prime[i] << " ";
//    cout << endl << prime[0] << endl;
}
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("output-large.txt","w",stdout);
    cin >> T;
    getprime();
    for(int i=1;i<=T;i++)
    {
        cin >> N >> J;
        printf("Case #%d:\n",i);
        solve();
    }

    return 0;
}
