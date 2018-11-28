#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

#define ff first
#define ss second

#ifndef ONLINE_JUDGE
#define dbg(args...)            {debug,args; cerr<<endl;}
#else
#define dbg(args...)
#endif

struct debugger
{
    template<typename T> debugger& operator , (const T& v)
	{
	    cerr<<v<<" ";
	    return *this;
	}
} debug;


string RPS = "RPS";
string out[15][3];

void solve(){
    int N, R, P, S;
    cin >> N >> R >> P >> S;
    string cur = string(P, 'P') + string(R, 'R') + string(S, 'S');
    string res;
    for (int j = 0; j < 3; j++){
        string ref = out[N][j];
        sort(ref.begin(), ref.end());
        if (ref == cur){
            cout << out[N][j] << endl;
            return;
        }
    }
    cout << "IMPOSSIBLE" << endl;
}

string gen(int lvl, string cur){
    if (lvl == 0) return cur;

    string cons = "";
    for (char c : cur){
        string left, right;
        if (c == 'R') {
            left = gen(lvl - 1, "R");
            right = gen(lvl - 1, "S");
        } else if (c == 'P'){
            left = gen(lvl - 1, "P");
            right = gen(lvl - 1, "R");
        } else {
            left = gen(lvl - 1, "P");
            right = gen(lvl - 1, "S");
        }
        if (right < left) swap(left, right);
        cons += left;
        cons += right;
    }
    return cons;
}

int main(){
    std::ios_base::sync_with_stdio(false);
    for (int i = 1; i <= 12; i++){
        for (int j = 0; j < 3; j++){
            out[i][j] = gen(i, string(1, RPS[j]));
        }
    }

    int tc; cin >> tc;
    for (int cs = 1; cs <= tc; cs++){
        cout << "Case #" << cs << ": ";
        solve();
    }


    return 0;
}
