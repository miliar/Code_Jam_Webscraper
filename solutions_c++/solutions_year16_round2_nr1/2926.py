#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <cstring>
#include <climits>
#include <cstdio>
#include <stack>

using namespace std;
typedef pair<int,int> pi;
typedef set<int> si;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef long long ll;
#define sz size()
#define mp make_pair
#define pb push_back
#define ri(a, b) for(int i=((int)(a)); i < ((int)(b)); i++)                // i -> [a, b)
#define rie(a, b) for(int i=((int)(a)); i <= ((int)(b)); i++)            // i -> [a, b]
#define rj(a, b) for(int j=((int)(a)); j < ((int)(b)); j++)               // j -> [a, b)
#define rje(a, b) for(int j=((int)(a)); j <= ((int)(b)); j++)           // j -> [a, b]
#define rk(a, b) for(int k=((int)(a)); k < ((int)(b)); k++)           // k -> [a, b)
#define rke(a, b) for(int k=((int)(a)); k <= ((int)(b)); k++)       // k -> [a, b]
#define fi(b) for(int i=0; i < ((int)(b)); i++)                             // i -> [0, b)
#define fie(b) for(int i=0; i <= ((int)(b)); i++)                         // i -> [0, b]
#define fj(b) for(int j=0; j < ((int)(b)); j++)                            // j -> [0, b)
#define fje(b) for(int j=0; j <= ((int)(b)); j++)                        // j -> [0, b]
#define fk(b) for(int k=0; k < ((int)(b)); k++)                        // k -> [0, b)
#define fke(b) for(int k=0; k < ((int)(b)); k++)                      // k -> [0, b]
#define fle(b) for(int l=0; l <= ((int)(b)); l++)                        // l -> [0, b]

map<int, char> dc;
map<int, string> ds;

pair<string, int> remove(string s, int d){
    string p = ds[d], t;
    int count = 0, n = s.size();
    fi(n) if(s[i] == dc[d]) count++;
    if(count == 0) return make_pair(s, 0);
    map<char, int> mc, tc;
    for(char c : p){
        mc[c] = 0;
        if(tc.count(c)) tc[c]++;
        else tc[c] = 1;
    }
    for(char c : s){
        if(p.find(c) != string::npos && mc[c] < tc[c]*count) mc[c]++;
        else t.push_back(c);
    }
    // cout<<"remove on "<<s<<" for "<<d<<" = "<<count<<","<<t<<endl;
    return make_pair(t, count);
}

int main(){

    int n, t;
    string s, ans;
    cin>>t;

    dc[0] = 'Z';
    dc[1] = 'N';
    dc[2] = 'W';
    dc[3] = 'R';
    dc[4] = 'U';
    dc[5] = 'F';
    dc[6] = 'X';
    dc[7] = 'V';
    dc[8] = 'G';
    dc[9] = 'I';

    ds[0] = "ZERO";
    ds[1] = "ONE";
    ds[2] = "TWO";
    ds[3] = "THREE";
    ds[4] = "FOUR";
    ds[5] = "FIVE";
    ds[6] = "SIX";
    ds[7] = "SEVEN";
    ds[8] = "EIGHT";
    ds[9] = "NINE";

    rke(1, t){
        cin>>s;
        map<int, int> count;
        vi v = {0, 2, 4, 6, 8, 5, 7, 9, 1, 3};        

        for(int a : v){
            pair<string, int> p = remove(s, a);
            s = p.first;
            count[a] = p.second;
        }
        ans.clear();
        fi(10){
            fj(count[i]) ans += to_string(i);
        }
        // cout<<"final string is "<<s<<endl;
        cout<<"Case #"<<k<<": "<<ans<<endl;
    }
}
// END CUT HERE 
