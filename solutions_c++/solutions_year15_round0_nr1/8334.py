/* Bismillahir rahmanir rahim */
//#pragma comment(linker, "/STACK:36777216")

#include <bits/stdc++.h>

using namespace std;

#define INT_MAX     2147483647
#define INT_MIN     -2147483648
#define pi          acos(-1.0)
#define siz         1000000
#define eps         1e-9

#define rep(i, n)       for(int i = 0; i < (n); i++)
#define reps(i, a, b)   for(int i= (a); i <= (b); i++)
#define fill(a, v)      memset(a, v, sizeof (a))
#define pb              push_back
#define pf              push_front
#define mp              make_pair
#define all(a)          (a).begin(),(a).end()

template<class T> inline T gcd(T a, T b)    { return b == 0 ? a : gcd(b, a % b); }
template<class T> inline T lcm(T a, T b)    { return (a / gcd(a, b)) * b; }

typedef long long int LL;
typedef long double LD;
typedef vector<int> VI;

int diri[] = {0, 1, 0, -1, -1, 1, 1, -1};
int dirj[] = {1, 0, -1, 0, 1, 1, -1, -1};

int main(){
//clock_t start = clock();
//ios_base::sync_with_stdio(false);
//cin.tie(NULL);
//#ifndef ONLINE_JUDGE
    freopen("A-large.in", "r", stdin);
    freopen("output2.out", "w", stdout);
//#endif
    int t, k, c = 1;
    string s;
    cin>>t;
    while(t--){
        int ret = 0;
        int st = 0;

        cin>>k>>s;
        reps(i, 0, k){
            int p = s[i] - '0';
            if(i > st && p > 0){
                ret += i - st;
                st += i - st;
            }
            st += p;
        }

        cout<<"Case #"<<c++<<": "<<ret<<endl;
    }



//    clock_t final = clock()-start;
//    cerr<<endl<<final/ (double) CLOCKS_PER_SEC<<endl;
    return 0;
}
