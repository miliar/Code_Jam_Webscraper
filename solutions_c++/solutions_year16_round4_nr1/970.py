#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string.h>
using namespace std;

void useFile(const string& str = "")
{
    if(str != "" && str != "std"){
        freopen( (str+".in").c_str(), "r", stdin );
        freopen( (str+".out").c_str(), "w", stdout);
    }
}

const int MAXN = 1<<14;

string min_seq[3][13];
map<char, int> mp;

void init(){
mp['P'] = 0;
mp['R'] = 1;
mp['S'] = 2;

}

void calcMin(string& ans, char A, char B, int i)
{
    int a = mp[A];
    int b = mp[B];
    auto& x = min_seq[a][i-1];
    auto& y = min_seq[b][i-1];
    if (x < y){
        ans = x + y;
    }else{
        ans = y + x;
    }
}

void calcMin()
{
    min_seq[0][0] = "P";
    min_seq[1][0] = "R";
    min_seq[2][0] = "S";
    for (int i = 1; i < 13; i++){
        calcMin(min_seq[0][i], 'P', 'R', i);
        calcMin(min_seq[1][i], 'R', 'S', i);
        calcMin(min_seq[2][i], 'S', 'P', i);
    }
}

void calc(int n, int P, int R, int S, std::string& ans)
{
    for (int x = 0; x < 3; x++){
        const auto& cur = min_seq[x][n];
        int p = 0, r = 0, s = 0;
        for (auto w : cur){
            switch (w){
                case 'R' : r++; break;
                case 'S' : s++; break;
                case 'P' : p++; break;
            }
        }
        bool ret = ((r == R) && (p == P) && (s == S));
        if (ret && ans > cur) {
            ans = cur;
        }
    }
}

int main(){
    useFile("A4");
    init();
    calcMin();
    int T = 0;
    cin >> T;
    int N, P, R, S;
    vector<char> win {'P', 'R' ,'S'};

    for(int ca = 1; ca <= T; ca++){
        cin >> N >> R >> P >> S;
        string ans = "Z";

        for (auto w : win){
            calc(N, P, R, S, ans);
        }
        if (ans == "Z") {
            ans = "IMPOSSIBLE";
        }
        cout << "Case #" << ca << ": " << ans << endl;
    }
}
