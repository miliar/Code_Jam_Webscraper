#include <bits/stdc++.h>
using namespace std;

#define file "file"
#define mp make_pair
#define pb push_back
#define xx real()
#define yy imag()
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef complex<double> point;

#define DEBUG 0
#define dout if(DEBUG) cout

const int MAXN = 13;
const int LIM = 1 << MAXN;
set<pair<pii, int> > st;
char ans[LIM + 10];
int n, r, p, s, top;
bool good;

void rec_sol(int n, ll a, ll b, ll c){
    if(!n){
        if(a == r && b == p && c == s){
            good = 1;
        }
        return;
    }
    rec_sol(n - 1, a + b, b + c, c + a);
}

string dfs(int n, int a, int b, int c){
    if(!n){
        if(b){
            return "P";
        }
        else if(a){
            return "R";
        }
        else{
            return "S";
        }
    }
    if(b){
        string s1 = dfs(n - 1, 0, 1, 0);
        string s2 = dfs(n - 1, 1, 0, 0);
        if(s2 < s1) swap(s1, s2);
        return s1 + s2;
    }
    else if(c){
        string s1 = dfs(n - 1, 0, 1, 0);
        string s2 = dfs(n - 1, 0, 0, 1);
        if(s2 < s1) swap(s1, s2);
        return s1 + s2;
    }
    else if(a){
        string s1 = dfs(n - 1, 1, 0, 0);
        string s2 = dfs(n - 1, 0, 0, 1);
        if(s2 < s1) swap(s1, s2);
        return s1 + s2;
    }
}

void solve(){
    scanf("%d%d%d%d", &n, &r, &p, &s);
    string cur[3];
    int topc = 0;
    good = 0;
    rec_sol(n, 1, 0, 0);
    if(good){
       cur[topc++] = dfs(n, 1, 0, 0);
    }
    good = 0;
    rec_sol(n, 0, 1, 0);
    if(good){
       cur[topc++] = dfs(n, 0, 1, 0);
    }
    good = 0;
    rec_sol(n, 0, 0, 1);
    if(good){
       cur[topc++] = dfs(n, 0, 0, 1);
    }
    if(!topc){
        printf("IMPOSSIBLE"); return;
    }
    sort(cur, cur + topc);
    for(int i = 0; i < (1 << n); i++){
        ans[i] = cur[0][i];
    }
    ans[(1 << n)] = '\0';
    printf("%s", ans);
}

int main()
{
	#ifdef NASTYA
    assert(freopen("input.txt","r",stdin));
    assert(freopen("output.txt","w",stdout));
    #else
    //assert(freopen(file".in","r",stdin)); assert(freopen(file".out","w",stdout));
    #endif
	int t = 1;
	int cs = 1;
	cin >> t;
	while(t--){
        printf("Case #%d: ", cs++);
		solve();
        printf("\n");
	}
	return 0;
}
