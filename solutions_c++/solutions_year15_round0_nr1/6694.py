#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int conversion(string p){ int o; o=atoi(p.c_str()); return o; }
string toString(int h){ stringstream ss; ss<<h; return ss.str(); }
long long gcd(long long a,long long b) {return (b==0 ? a : gcd(b,a%b));}
long long lcm(long long a,long long b) {return (a*(b/gcd(a,b))); }
long long toi(string p){long long x;istringstream in(p); in>>x; return x;}
// IMPRMIR DECIMALES -> %.3f
// Logaritmo en cualquir base ( nota: solo cambiar el 2 ) printf("Case %d: %.0lf\n", cnt++, max(0.0,ceil(log(n) / log(2))));

int main() {

    #ifndef ONLINE_JUDGE
    freopen("D:/input.txt","r",stdin);
    freopen("D:/output.txt","w",stdout);
    #endif

    int T,n,sum=0,res=0;
    cin>>T;
    string a;
    for(int z=1;z<=T;z++)
    {
        cin>>n>>a;
        for(int i=0;i<a.size();i++)
        {
            if(i==0) {sum+=(a[i]-'0');continue;}
            if(sum<i&&a[i]>'0')
            {
                res+=abs(i-sum);
                sum+=abs(i-sum)+(a[i]-'0');
            }
            else sum+=(a[i]-'0');
        }
        cout<<"Case #"<<z<<": "<<res<<endl;
        sum=res=0;
    }
}
