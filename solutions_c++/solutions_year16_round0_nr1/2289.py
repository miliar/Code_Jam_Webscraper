#include<bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;
#define all(x)      (x).begin(), (x).end()
#define re(i,s,n)   for(int i=s;i<(n);++i)
#define fr(i,n)     re(i,0,n)
#define tr(i,x)     for(typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define SSTR( x ) dynamic_cast< std::ostringstream & >( \
        ( std::ostringstream() << std::dec << x ) ).str()
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;
typedef unsigned long long ull;
template<class T> T gcd(T a, T b) {
    return b ? gcd(b, a % b) : a;
}
const double EPS = 1e-7;

int main() {
    int t;
    scanf("%d",&t);
    fr(_t,t) {
        long n;
        scanf("%ld",&n);
        if(!n) {
            printf("Case #%d: INSOMNIA\n",_t+1);
        } else {
            bool f[10];
            fr(i,10) f[i] = false;
            int cnt = 0;
            long num = n;
            while(true) {
                long temp = num;
                while(temp) {
                    int d = temp%10;
                    if(!f[d]) cnt++;
                    f[d] = true;
                    temp = temp/10;
                }
                if(cnt == 10) {
                    printf("Case #%d: %ld\n",_t+1,num);
                    break;
                }
                num += n;
            }
        }
    }
    return 0;
}


