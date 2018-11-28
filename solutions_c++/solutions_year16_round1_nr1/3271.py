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
    fr(_t,t){
        string s;
        cin >> s;

        int n = s.size();

        string s2 = "";
        char f = s[0];
        fr(i,n){
            if(s[i]>=f){
                s2 = s[i] + s2;
            }else{
                s2 = s2 + s[i];
            }
            f = s2[0];
        }
        printf("Case #%d: ",_t+1);
        cout << s2 << endl;
    }
    return 0;
}


