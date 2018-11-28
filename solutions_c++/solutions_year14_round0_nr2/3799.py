#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

// Constants
const int INF = 1000000000;
const long double EPS = 1e-10L;
const long double PI = acos(-1.0);

#define For(i,b) for(int i = 0; i < (int)b; ++i)
#define Fori(i,a,b) for(int i = a; i < (int)b; ++i)
#define Ford(i,a,b) for(int i = a; i >=b; --i)
#define All(t) t.begin(),t.end()
#define Sort(a) sort(All(a))
#define Fill(a,b) memset(a,b,sizeof(a))
#define Forstl(it,x) for(typeof(x.begin()) it=x.begin(); it!=x.end(); ++it)
#define pb push_back
#define mp make_pair
#define db(x) cout << #x << " = " << x << endl
#define mod(A, B) ((((A) % (B)) + (B)) % (B))
#define ARRSIZE(x) (sizeof(x)/sizeof(x[0]))
#define Exist(container, element) (find(All(container),element) != container.end())
#define sz(a) int((a).size())
#define rad(a) ((1.*(a)*PI)/180.)
#define sqr(a) ((a)*(a))
#define bet(a,b,c) (((a)<=(b))&&((b)<=(c)))

using namespace std;

template <class T>
void out(vector<T> v)
{
    cout << "{";
    For(_i,v.size()) {if(_i) cout<<","; cout<<v[_i];}
    cout<<"}"<<endl;
}

// convert int to string
string _itos (int i) {stringstream s; s << i; return s.str();}

// convert string to int
int _stoi (string s) {istringstream in(s); int ret; in >> ret; return ret;}

/*
double get(double C, double F, double X)
{
    double res = X / 2.0;
    db(res);
    double rem = C / 2.0;
    int farms = 1;
    int cnt = 1000;
    while(--cnt)
    {
        double cur = rem + X / (2.0 + farms * F);
        db(cur);
        res = min(res, cur);
        rem += C / (2.0 + farms * F);
        ++farms;
    }
    return res;
}
*/

double get(double C, double F, double X, int farms)
{
    double res = 0.0;
    For(i, farms)
        res += C / (2.0 + F * i);
    res += X / (2 + F * farms);
    return res;
}

double ternary_search(double C, double F, double X)
{
    int l = 0, r = 1000000;
    For(it, 1000)
    {
        int m1 = l + (r - l) / 3, m2 = r - (r - l) / 3;
        double f1 = get(C, F, X, m1), f2 = get(C, F, X, m2);
        if(f1 < f2)
            r = m2;
        else
            l = m1;
        
    }
    //db(l), db(r);
    double res = get(C, F, X, l);
    for(int i = l + 1; i <= r; ++i)
    {
        double cur = get(C, F, X, i);
        res = min(res, cur);
    }
//    for(int i = 99900; i <= 1000000; i += 1000)
//    {
//        double cur = get(C, F, X, i);
//        printf("%d %.7f\n", i, cur);
//    }
    return res;
}

int main ()
{
    int T;
    double C, F, X;
    cin >> T;
    For(test, T)
    {
        cin >> C >> F >> X;
        double res = ternary_search(C, F, X);
        printf("Case #%d: %.7f\n", test + 1, res);
    }
    return 0;
}

