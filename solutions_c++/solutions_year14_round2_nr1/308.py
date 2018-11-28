#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <ctime>
#include <deque>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i ++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i --)
#define mp make_pair
#define pb push_back
#define fs first
#define sc second
#define pi 3.1415926535897932384626433832795l

typedef long long ll;
typedef long double ld;

vector <char> get(const string& s){
    vector <char> obr;
    for (int i = 0; i < int(s.size());){
        
        int j = i;
        for (; j < int(s.size()) && s[i] == s[j]; ++ j);
        obr.pb(s[i]);
        i = j;     
    }
    return obr;
}

vector <int> get2(const string& s){
    vector <int> obr;
    for (int i = 0; i < int(s.size());){
        int j = i;
        for (; j < int(s.size()) && s[i] == s[j]; ++ j);
        obr.pb(j - i);
        i = j;    
    }
    return obr;
}


string s[110];
int n;
vector <int> help[110];

int main(){
#ifdef SG
    freopen ("input.txt","rt",stdin);
  freopen ("output.txt","wt",stdout);
#endif
    int t;
    cin >> t;
    forn(qqq, t){
        int n;
        cin >> n;
        forn(i, n){
            help[i].clear();
        }
        string tra;
        printf ("Case #%d: ", qqq + 1);
        getline(cin, tra);
        forn(i, n){
            getline(cin, s[i]);
        } 
        vector <char> obr = get(s[0]);
        bool q = true;
        
        forn(i, n){
            if (get(s[i]) != obr){
/*                vector <char>obr1 = get(s[i]);
                forn(j, obr1.size())
                    cerr << obr1[j];
                cerr << endl;*/
                puts("Fegla Won");
                q = false;   
                break;
            }
            help[i] = get2(s[i]); 
        }
        if (!q)
            continue;

        int kol = int(help[0].size());
        int ans = 0;
        forn(i, kol){
            vector <int> res;
            forn(j, n){
                res.pb(help[j][i]);    
            } 
            sort(res.begin(), res.end());
            forn(i, res.size()){
                ans += abs(res[i] - res[int(res.size()) / 2]);
            }
        }
        cout << ans << endl;
    } 

    return 0;
}
