#include <bits/stdc++.h>

#define all(x) (x).begin(), (x).end()

#ifdef KAZAR
    #define eprintf(...) fprintf(stderr,__VA_ARGS__)
#else
    #define eprintf(...) 0
#endif

using namespace std;

template<class T> inline void umax(T &a,T b){if(a<b) a = b ; }
template<class T> inline void umin(T &a,T b){if(a>b) a = b ; }
template<class T> inline T abs(T a){return a>0 ? a : -a;}
template<class T> inline T gcd(T a,T b){return __gcd(a, b);}
template<class T> inline T lcm(T a,T b){return a/gcd(a,b)*b;}

typedef long long ll;
typedef pair<int, int> ii;

const int inf = 1e9 + 143;
const ll longinf = 1e18 + 143;

inline int read(){int x;scanf(" %d",&x);return x;}

const int N = 220;

char foo[1 << 15];

int n;
vector<string> v[N];
vector<int> ids[N];

void read_inp(){
    for(int i = 0; i < N; i++)
        v[i].clear();
    n = read();
    gets(foo);
    for(int i = 0; i < n; i++){
        gets(foo);
        int len = strlen(foo);
        string tmp = "";
        //eprintf("\ni = %d\n", i);
        for(int j = 0; j <= len; j++){
            //eprintf("%c, (%s)\n", foo[j], tmp.c_str());
            if(j == len || foo[j] == ' '){
                //eprintf("in!!\n");
                //eprintf("(%s)\n", tmp.c_str());
                v[i].push_back(tmp);
                tmp = "";
            }else{
                tmp += foo[j];
            }
        }
    }
}

int solve(){
    read_inp();
    static unordered_map<string, int> id;
    id.clear();
    int ptr = 0;
    for(int i = 0; i < n; i++){
        ids[i].clear();
        for(string s: v[i]){
            if(id.count(s) == 0){
                id[s] = ++ptr;
            }
            ids[i].push_back(id[s]);
        }
    }
    int best = inf;
    for(int mask = 0; mask < (1 << (n - 2)); mask++){
        vector<int> tp(ptr + 1, 0);
        for(int i = 0; i < n; i++){
            int c = 0;
            if(i == 0) c = 1;
            else if(i == 1) c = 2;
            else{
                if(mask & (1 << (i - 2)))
                    c = 1;
                else
                    c = 2;
            }
            for(int x: ids[i])
                tp[x] |= c;
        }
        int cur = 0;
        for(int i = 1; i <= ptr; i++){
            if(tp[i] == 3){
                //eprintf("%s\n", e.first.c_str());
                cur++;
            }
        }
        //eprintf("pass!!\n");
        umin(best, cur);
    }
    return best;
}

int main(){

#ifdef KAZAR
    freopen("f.input","r",stdin);
    freopen("f.output","w",stdout);
    //freopen("error","w",stderr);
#endif

    int t = read();

    for(int i = 1; i <= t; i++){
        printf("Case #%d: %d\n", i, solve());
        eprintf("test = %d\n", i);
    }

    return 0;
}
