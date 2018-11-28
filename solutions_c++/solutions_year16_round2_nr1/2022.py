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

int cnt[256];
char str[2001];
char result[2001];
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
            //cerr<<str<<endl;
            int len = strlen(str);
            memset(cnt,0,sizeof(cnt));
            loop(i,0,len){
                cnt[str[i]]++;
            }
            int i =0 ;
            int res[10];
            memset(res,0,sizeof(res));

            while(cnt['Z']){
                cnt['Z']--; cnt['E']--; cnt['R']--; cnt['O']--;
                res[0]++;
            }
            while(cnt['W']){
                cnt['T']--; cnt['W']--; cnt['O']--;
                res[2]++;
            }
            while(cnt['X']) {
                cnt['S']--; cnt['I']--; cnt['X']--; res[6]++;
            }
            while(cnt['G']){
                cnt['E']--; cnt['I']--; cnt['G']--; cnt['H']--; cnt['T']--; res[8]++;
            }

            while(cnt['S']){
                cnt['S']--; cnt['E']--; cnt['V']--; cnt['E']--; cnt['N']--; res[7]++;
            }
            while(cnt['V']){
                cnt['F']--; cnt['I']--; cnt['V']--; cnt['E']--; res[5]++;
            }
            while(cnt['F']){
                cnt['F']--; cnt['O']--; cnt['U']--; cnt['R']--; res[4]++;
            }

            while(cnt['H']){
                cnt['T']--; cnt['H']--; cnt['R']--; cnt['E']--; cnt['E']--; res[3]++;
            }
            while(cnt['O']){
                cnt['O']--; cnt['N']--; cnt['E']--; res[1]++;
            }
            while(cnt['I']){
                cnt['I']--; res[9]++;
            }

            cout<<"Case #"<<t<<": ";
            for(int j=0;j<10;j++){
                for(int k=0;k<res[j];k++) cout<<j;
            }
            cout<<endl;
        }
    }
    void output(){
    }
};

void Solution::solve(){

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
