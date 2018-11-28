#include"iostream"
#include"vector"
#include"string"
#include"cstdio"
#include"cstdlib"
#include"cmath"
#include"algorithm"
#include"queue"
#include"cstring"
#include"map"
#include"set"
#include"fstream"
#include"sstream"
#include"numeric"
#include"stack"
#include"iomanip"
#include"bitset"
#include"list"
#include"functional"
#include"utility"
#include"ctime"
#include"cctype"
#include"cassert"
#include"exception"

using namespace std;

typedef long long ll;
const double eps=1e-6;
const int inf=0x3f3f3f3f;
const int hinf=0x3f3f3f3f;
const ll mod=1000000007;

#define fio freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
#define fino freopen("input.txt","r",stdin);
#define ms(a,i) memset((a),(i),sz(a))
#define clr(x) memset(x,0,sz(x))
#define cdp(x) memset((x),-1,sizeof(x))
#define infi(x) memset(x,0x3f,sz(x))
#define foreach(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin>>T;
    int Case = 0;
    while(T--) {
        double c , f , x ;
        double ans;
        int n;
        cin>>c>>f>>x;
        n = ceil(x/c - 2/f - 1);
        if(n <= 0)
            ans = x/2.0;
        else {
            ans = c/2.0;
            for(int i = 1 ; i + 1 <= n ; i ++)
                ans += c/(2.0 + 1.0 * i * f);
            ans += x/(2.0 + 1.0 * n * f);
        }
        printf("Case #%d: %lf\n",++Case , ans);
    }
    return 0;
}
