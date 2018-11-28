#include <bits/stdc++.h>

#ifdef LOCAL_BUILD
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;

#else

#define trace1(x)
#define trace2(x, y)
#define trace3(x, y, z)
#define trace4(a, b, c, d)
#define trace5(a, b, c, d, e)
#define trace6(a, b, c, d, e, f)

#endif

typedef long long LL;
typedef unsigned long long ULL;
typedef int  I32;
typedef unsigned int  UI32;
typedef short I16;
typedef unsigned short U16;
typedef char I8;
typedef unsigned char UI8;
const int MOD = 1e9 + 7;

#define loop(i,s,e) for(long long i=s;i<e;i++)
#define range(i,s,e) for(long long i=s;i<=e;i++)

ULL powermod(ULL x, ULL y)
{
    ULL temp;
    if( y == 0)
       return 1;
    temp = powermod(x, y/2);
    if (y%2 == 0)
        return (temp*temp)%MOD;
    else
    {
        if(y > 0)
            return (x*((temp*temp)%MOD))%MOD;
        else
            return (temp*temp)/x;
    }
}

using namespace std;
/***********************************************************************************/
char str[101];
int result;
class Solution
{
public:
int T;
    Solution(){ T=1; }
    void solve();
    void input(){
        cin>>T;
        loop(t,1,T+1){
            cin>>str;
            solve();
            cout<<"Case #"<<t<<": ";
            cout<<result<<endl;
        }
    }
    void output(){
    }
};

void Solution::solve(){
    int i=1;
    int cnt=1;
    while(str[i]){
        if(str[i] != str[i-1]) cnt++;
        i++;
    }
    if(str[i-1] =='+') cnt --;
    result = cnt;
}

int main()
{
#ifdef LOCAL_BUILD
    freopen("input.txt","r",stdin);
    freopen("debug.txt","w",stderr);
    freopen("output.txt","w",stdout);
#endif
    Solution S;
    S.input();
    S.output();
    return 0;
}
