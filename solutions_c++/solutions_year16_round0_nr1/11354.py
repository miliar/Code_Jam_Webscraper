#include <bits/stdc++.h>
using namespace std;

#define ALL(g) (g).begin(),(g).end()
#define REP(i, x, n) for(int i = x; i < n; i++)
#define rep(i,n) REP(i,0,n)
#define F(i,j,k) fill(i[0],i[0]+j*j,k)
#define P(p) cout<<(p)<<endl;
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define INF 1<<25
#define pb push_back
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

typedef vector<int> vi;
typedef vector<long long> vl;
typedef vector<double> vd;
typedef pair<int,int> pii;
typedef pair<long,long> pll;
typedef long long ll;
// function //
template<class T> T gcd(T a,T b)
{
    if(a<0) return gcd(-a,b);
    if(b<0)return gcd(a,-b);
    return (b==0)?a:gcd(b,a%b);
}
template <class T> T lcm(T a,T b)
{
    return a*(b/gcd(a,b));
}
template<class T> inline vector<pair<T,int> > factorize(T n)
{
    vector<pair<T,int> > R;
    for (T i=2; n>1;)
    {
        if (n%i==0)
        {
            int C=0;
            for (; n%i==0; C++,n/=i);
            R.push_back(make_pair(i,C));
        }
        i++;
        if (i>n/i) i=n;
    }
    if (n>1) R.push_back(make_pair(n,1));
    return R;
}
template<class T> inline bool isPrimeNumber(T n)
{
    if(n<=1)return false;
    for (T i=2; i*i<=n; i++) if (n%i==0) return false;
    return true;
}
template<class T> inline T eularFunction(T n)
{
    vector<pair<T,int> > R=factorize(n);
    T r=n;
    for (int i=0; i<R.size(); i++)r=r/R[i].first*(R[i].first-1);
    return r;
}
template<class T> string toString(T n)
{
    ostringstream ost;
    ost<<n;
    ost.flush();
    return ost.str();
}
int toInt(string s)
{
    int r=0;
    istringstream sin(s);
    sin>>r;
    return r;
}

// ostream //
// pair
template<typename T1, typename T2> ostream& operator<<(ostream& s, const pair<T1, T2>& p) {return s << "(" << p.first << ", " << p.second << ")";}
// vector
template<typename T> ostream& operator<<(ostream& s, const vector<T>& v) {
    int len = v.size();
    for (int i = 0; i < len; ++i) {
        s << v[i]; if (i < len - 1) s << " ";
    }
    return s;
}

// 2 dimentional array
template< typename T, size_t N, size_t M >
void printArray( T(&theArray)[N][M]  ) {
    for ( int x = 0; x < N; x ++ ) {
        for ( int y = 0; y < M; y++ ) {
            cout << theArray[x][y] << " ";
        }
    }
}

// 2 dimentional vector
template<typename T> ostream& operator<<(ostream& s, const vector< vector<T> >& vv) {
    int len = vv.size();
    for (int i = 0; i < len; ++i) {
        s << vv[i] << endl;
    }
    return s;
}
// map
template<typename T1, typename T2> ostream& operator<<(ostream& s, const map<T1, T2>& m) {
    s << "{" << endl;
    for (auto itr = m.begin(); itr != m.end(); ++itr) {
        s << "\t" << (*itr).first << " : " << (*itr).second << endl;
    }
    s << "}" << endl;
    return s;
}

/* input example start
input example end */


ll N;
int idx[10],ans;

string s;
int num = 0;

void solve(){
    bool flag=false;
    for (int i = 1; i < 100; ++i)
    {
        int sum = 0;

        // add if new number in N*i
        s = to_string(i*N);
        for (int j = 0; j < (int)s.size(); ++j)
        {
            char ch = s[j];
            int iNum = (int)(unsigned char)(ch - '0');
            idx[iNum] = 1;
        }

        for (int j = 0; j < 10; ++j)
        {
            sum += idx[j];
        }
        if (sum == 10) {
            flag = true;
            ans = i * N;
            break;
        }
    }
    if (flag) {
        cout << ans << endl;
    }
    else {
        cout << "INSOMNIA" << endl;
    }
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    while(cin >> N){
        if (num != 0) {
        for (int i = 0; i < 10; ++i)
            {
                idx[i] = 0;
            }
        cout << "Case #";
        cout << num << ": ";
        solve();
        }
    num++;
    }
    return 0;
}
















