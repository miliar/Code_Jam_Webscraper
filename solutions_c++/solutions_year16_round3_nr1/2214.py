/*
 *
 * Copyright(c) 2016 Taikai Takeda <297.1951@gmail.com> All rights reserved.
 *
 */
//include
//------------------------------------------
#include <bits/stdc++.h>
using namespace std;

//conversion
//------------------------------------------
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

//math
//-------------------------------------------
template<class T> inline T sqr(T x) {return x*x;}

//typedef
//------------------------------------------
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long ll;

//container util
//------------------------------------------
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())

//repetition
//------------------------------------------
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define RFOR(i,a,b) for(int i=(b-1);i>=(a);--i)
#define REP(i,n)  FOR(i,0,n)

//constant
//--------------------------------------------
const double EPS = 1e-10;
const double PI  = acos(-1.0);
const int MOD = 1000000007;

//clear memory
#define CLR(a) memset((a), 0 ,sizeof(a))


//debug
#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;


char itoa[] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};

int solve(int ith)
{
    int n, max_p = 1000;
    cin >> n;

    VI p(n), q(n, 0);
    REP(i,n)
        cin >> p[i];

    int sum = 0;

    REP(i,n)
        sum+=p[i];

    vector<string> ans;

    int cnt = 0;
    string str="";
    REP(i,n){
        if(p[i] > 0){
            p[i]--;
            q[i]++;
            cnt++;
            sum--;
            str += itoa[i];
        }
        if(cnt==2)
            break;
    }
    ans.push_back(str);
    while(sum>0){
        str = "";
        REP(i,2){
            int min_i = -1, min = 1000001;
            REP(i,n){
                if(p[i]>0 && q[i] < min){
                    min = q[i];
                    min_i = i;
                }
            }
            str += itoa[min_i];
            p[min_i]--;
            q[min_i]++;
            sum--;
            if(sum == 0)
                break;
        }
        ans.push_back(str);
    }
    int k = ans.size();

    cout << "Case #" << ith << ":";
    REP(i, k){
        cout << ' ' << ans[k-i-1];
    }
    cout << endl;

    return 0;
}


int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);

    int t;
    int i = 0;

    cin >> t;
    while(t--){
        i++;
        solve(i);
    }

    return 0;
}
