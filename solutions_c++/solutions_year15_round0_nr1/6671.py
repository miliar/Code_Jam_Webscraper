#include<bits/stdc++.h>
 
#define INF 1000000000
#define EPS 1e-9
#define sz(c) (int) (c).size()
#define all(c) (c).begin(), (c).end()
#define tr(c, i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define uniq(c) sort(all(c)); (c).resize(unique(all(c)) - (c).begin())
#define lobo(c, x) (int) (lower_bound(all(c), (x)) - (c).begin())
#define upbo(c, x) (int) (upper_bound(all(c), (x)) - (c).begin())
 
#define pb push_back
#define mp make_pair
#define fi first
#define se second
 
using namespace std;

#ifdef DEBUG   
    #define wrap(a) a
    #define debug(args...) { vector<string> _v = split(#args, ','); err(_v.begin(), args); }

    vector<string> split(const string& s, char c) {
        vector<string> v;
        stringstream ss(s);
        string x;
        while (getline(ss, x, c))
            v.emplace_back(x);
        return move(v);
    }

    void err(vector<string>::iterator it) { cout << endl; }
    template<typename T, typename... Args>
    void err(vector<string>::iterator it, T a, Args... args) {
        cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << ", ";
        err(++it, args...);
    }
#else
    #define debug(args...) 
    #define wrap(a) 
#endif
typedef long long ll;
typedef pair <int, int> ii;

inline int getint(char* s, int i) {
    return s[i]-'0';
}

int main() {
    int ntc; scanf("%d", &ntc);

    for ( int tc = 0; tc < ntc; ++tc ) {
        int smax; scanf("%d", &smax);
        char s[1005]; scanf("%s", &s);

        int sumall = getint(s, 0), ans = 0;
        for ( int i = 1; i <= smax; ++i ) {
            int gi = getint(s, i);
            if ( gi > 0 && sumall+ans < i ) {
                int k = i-(sumall+ans);
                ans += k;
            }

            sumall += gi;
        }

        printf("Case #%d: %d\n", tc+1, ans);
    }
    return 0;
}
