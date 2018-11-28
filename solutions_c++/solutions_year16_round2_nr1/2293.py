//******************************************************************
// Author: Huynh Nhat Minh
// Name of Problem:
// Verdict:
//******************************************************************
#include <bits/stdc++.h>

using namespace std;

#define fr(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define dw(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define rep(i,n) for (int i = 0, _n = (n); i < _n; i++)
#define sz(s) (int)s.size()
#define read(x) cin >> x
#define read2(x,y) cin >> x >> y
#define read3(x,y,z) cin >> x >> y >> z
#define out(x) cout << x
#define DEBUG(x) cout << #x << " = " << x << endl

#define ull unsigned long long
#define ll long long
#define all(ar) ar.begin(), ar.end()
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

//8 huong
//int dx[] = {-1,-1,-1, 0, 0, 1, 1, 1};
//int dy[] = {-1, 0, 1,-1, 1,-1, 0, 1};

//horse
//int dx[] = {-2,-2,-1,-1, 1, 1, 2, 2};
//int dy[] = {-1, 1,-2, 2,-2, 2,-1, 1};

const int dx[] = {-1, 0, 0, 1};
const int dy[] = { 0,-1, 1, 0};

typedef pair<int,int> ii;
typedef pair<int, ii> iii;
typedef vector<ii> vii;
typedef vector<int> vi;

#define BIT(n) (1<<(n))
#define AND(a,b) ((a) & (b))
#define OR(a,b) ((a)  (b))
#define XOR(a,b) ((a) ^ (b))
#define sqr(x) ((x) * (x))

#define PI 3.1415926535897932385
#define INF 1000111222
#define eps 1e-7
#define maxN 100000
#define mod 1000000007

string s, a;
int cnt[300];
int num[10];
string numString[] = {"ZERO", "TWO", "FOUR", "ONE", "FIVE", "SIX", "SEVEN", "EIGHT", "THREE", "NINE"};
string n = "0241567839";
string uni = "ZWUOFXSGHE";

int main()
{
    #ifndef ONLINE_JUDGE
    freopen("i.inp","r",stdin);
    freopen("o.out","w",stdout);
    #endif

    int tcs;
    read(tcs);

    fr(t,1,tcs) {
        read(s);
        rep(i,300) cnt[i] = 0;

        rep(i,sz(s)) {
            cnt[s[i]]++;
        }

        string ans = "";
        rep(i,10) {
//            fr(k,'A','Z') cout << cnt[k] << " ";
//            cout << endl;
            rep(j, cnt[uni[i]]) ans += n[i];
            rep(j, sz(numString[i])) {
                if(numString[i][j] == uni[i]) continue;
                cnt[numString[i][j]] -= cnt[uni[i]];
//                cout << (char) numString[i][j] << " ";
            }
            cnt[uni[i]] = 0;
//            cout << endl;
        }
        sort(all(ans));
        printf("Case #%d: ",t);
        cout << ans << endl;
    }

    return 0;
}

//Look at my code it's amazing !!!
