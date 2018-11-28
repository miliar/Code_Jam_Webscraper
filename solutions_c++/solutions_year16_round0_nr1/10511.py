#pragma region CONST_DEF

    #include <cstring>
    #include <string.h>
    #include <map>
    #include <deque>
    #include <queue>
    #include <stack>
    #include <sstream>
    #include <iostream>
    #include <iomanip>
    #include <cstdio>
    #include <cmath>
    #include <cstdlib>
    #include <ctime>
    #include <algorithm>
    #include <vector>
    #include <set>
    #include <complex>
    #include <list>

    using namespace std;

    #define pb push_back
    #define all(v) v.begin(),v.end()
    #define rall(v) v.rbegin(),v.rend()
    #define sz size()
    #define rep(i,m) for(int i=0;i<(int)(m);i++)
    #define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
    #define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
    #define mem(a,b) memset(a,b,sizeof(a))
    #define mp make_pair
    #define dot(a,b) ((conj(a)*(b)).X)
    #define X real()
    #define Y imag()
    #define length(V) (hypot((V).X,(V).Y))
    #define vect(a,b) ((b)-(a))
    #define cross(a,b) ((conj(a)*(b)).imag())
    #define normalize(v) ((v)/length(v))
    #define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
    #define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)
    //#define len(array) (sizeof((array))/sizeof((array[0])))

    typedef stringstream ss;
    typedef pair<int, int> pii;
    typedef vector<pii> vpii;
    typedef vector<string> vs;
    typedef vector<int> vi;
    typedef vector<double> vd;
    typedef vector<vector<int> > vii;
    typedef long long ll;
    typedef long double ld;
    typedef complex<double> point;
    typedef pair<point, point> segment;
    typedef pair<double, point> circle;
    typedef vector<point> polygon;

    const int oo = (int) 1e9;
    const double PI = 2 * acos(0);
    const double eps = 1e-9;

    inline int comp(const double &a, const double &b) {
        if (fabs(a - b) < eps)
            return 0;
        return a > b ? 1 : -1;
    }
#pragma endregion

bool isVeryTrue(bool dig[]) {
    rep(i, 10) {
        if(!dig[i]) return false;
    }
    return true;
}

void registerDig(long n, bool (&tab)[10]) {
    while(n >= 10) {
        tab[n%10] = true;
        n /= 10;
    }
    tab[n%10] = true;
}

long getLastNum(int start) {
    if(start == 0)
        return -1;
        
    bool dig[10];
    rep(i, 10) {
        dig[i] = false;
    }
    
    int n = 1;
    while(!isVeryTrue(dig)) {
        registerDig(start*n++, dig);
    }
    return (n-1) * start;
}

int main() {
    //freopen("in", "rt", stdin);
    freopen("A-large.in", "rt", stdin);
    freopen("A-large.out", "wt", stdout);

    long T, N;
    cin >> T;

    rep(t, T) {
        cin >> N;
		cout << "Case #" << t + 1 << ": ";
        if(N == 0)
            cout << "INSOMNIA"<< endl;
        else
            cout << getLastNum(N) << endl;        
    }
    return 0;
}