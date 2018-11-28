#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair <int , int > ii;
double  EPS= 1e-9;
#define MAXN 200000 + 6

int conversion(string p){ int o; o=atoi(p.c_str()); return o; }
string toString(int h){ stringstream ss; ss<<h; return ss.str(); }
long long gcd(long long a,long long b) {return (b==0 ? a : gcd(b,a%b));}
long long lcm(long long a,long long b) {return (a*(b/gcd(a,b))); }
long long toi(string p){long long x;istringstream in(p); in>>x; return x;}
long long square(long long n) { return n*n; }
long long fastexp(long long base,long long power) {if (power==0) return 1LL;else if (power%2==0) return square(fastexp(base,power/2LL));else return base * (fastexp(base,power-1LL));}
bool is_prime(int n) {for (int i=2; i*i<=n; i++) if (n%i == 0) return 0;return 1;}
int logba(int a,int b){return log(a)/log(b);}
int rd(double d){int x=(int)((double)d + 0.5);return x;}
// IMPRMIR DECIMALES -> %.3f
// Logaritmo en cualquir base ( nota: solo cambiar el 2 ) printf("Case %d: %.0lf\n", cnt++, max(0.0,ceil(log(n) / log(2))));

int main()
{

    #ifndef ONLINE_JUDGE
     freopen("D:/input.txt","r",stdin);
     freopen("D:/output.txt","w",stdout);
     #endif

    int T;
    cin>>T;
    int ind=1;
    while(T--)
    {
        long long x;
        cin>>x;
        if(x==0) cout<<"Case #"<<ind++<<": INSOMNIA"<<endl;
        else
        {
            set<char> S;
            for(ll i=1;i<=100;i++)
            {
                string a=toString(x*i);
                for(int j=0;j<a.size();j++)
                {
                    S.insert(a[j]);
                }
                if(S.size()==10)
                {
                    cout<<"Case #"<<ind++<<": "<<x*i<<endl;
                    break;
                }
            }
            if(S.size()!=10) cout<<"Case #"<<ind++<<": INSOMNIA"<<endl;
        }
    }
}
