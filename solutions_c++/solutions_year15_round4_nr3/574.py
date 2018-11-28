#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstring>
#include <fstream>
#include <ctime>
#include <iomanip>
#define LL long long
#define ULL unsigned long long
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FO(i,a,b) for(int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FOD(i,a,b) for(int i=a;i>b;i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define debug cout << "YES" << endl
#define REP(i, n) for (int i = 0; i < (int)(n); ++i)

using namespace std;

typedef pair<int, int>II;
typedef pair<int,II>PII;
template<class T> T gcd(T a, T b) {T r; while(b!=0) {r=a%b;a=b;b=r;} return a;}
template<class T> T lcm(T a, T b) { return a / gcd(a, b) * b; }
template<class T> int getbit(T s, int i) { return (s >> i) & 1; }
template<class T> T onbit(T s, int i) { return s | (T(1) << i); }
template<class T> T offbit(T s, int i) { return s & (~(T(1) << i)); }

const long double PI = 2*acos(0.0);
const long double eps = 1e-12;
const int infi = 1e9;
const LL Linfi = (LL) 1e18;
const LL MOD = 1000000007;
const int c1 = 31;
const int c2 = 37;
#define maxn 1505

const int N = 20;

vector<string> all;
vector<string> line[N];
vector<int> ids[N];
string s[25];
int n, answer;
int english[N * 1000], french[N * 1000];

void dfs(int iter) {
    if (iter == n) {
        int cnt = 0;
        for (int i = 0; i < all.size(); ++i) {
            cnt += english[i] && french[i];
        }
        answer = min(answer, cnt);
    } else {
        for (int i = 0; i < ids[iter].size(); ++i) {
            int id = ids[iter][i];
            english[id]++;
        }
        dfs(iter + 1);
        for (int i = 0; i < ids[iter].size(); ++i) {
            int id = ids[iter][i];
            english[id]--;
            french[id]++;
        }
        dfs(iter + 1);
        for (int i = 0; i < ids[iter].size(); ++i) {
            int id = ids[iter][i];
            french[id]--;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    #ifndef ONLINE_JUDGE
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    #endif
    int tn;
    cin >> tn;
    for (int ti = 1; ti <= tn; ++ti) {
        cin >> n; cin.ignore(1); all.clear();
        FO(i,0,n) {
            line[i].clear();
            getline(cin, s[i]);
            s[i] += ' ';
            string tmp = "";
            FOR(j,0,s[i].size()-1){
                if(s[i][j] == ' '){
                    line[i].pb(tmp);
                    tmp = "";
                }
                else tmp += s[i][j];
            }
            sort(line[i].begin(), line[i].end());
            line[i].erase(unique(line[i].begin(), line[i].end()), line[i].end());
            all.insert(all.end(), line[i].begin(), line[i].end());
        }

        sort(all.begin(), all.end());
        all.erase(unique(all.begin(), all.end()), all.end());


        for (int i = 0; i < n; ++i) {
            ids[i].clear();
            for (int j = 0; j < line[i].size(); ++j) {
                string str = line[i][j];

                int p = lower_bound(all.begin(), all.end(), str) - all.begin();
                ids[i].push_back(p);
            }
            sort(ids[i].begin(), ids[i].end());
            ids[i].erase(unique(ids[i].begin(), ids[i].end()), ids[i].end());
        }
        memset(english, 0, sizeof(english));
        memset(french, 0, sizeof(french));
        for (int i = 0; i < ids[0].size(); ++i) {
            int id = ids[0][i];
            english[id]++;
        }
        for (int i = 0; i < ids[1].size(); ++i) {
            int id = ids[1][i];
            french[id]++;
        }
        answer = 1e9;
        dfs(2);
        cout << "Case #" << ti << ": " << answer << '\n';
    }
}

