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

int solve(int A, int B, int K)
{
    int res = 0;
    For(old, A)
    {
        For(new_num, B)
        {
            res += ((old&new_num) < K);
        }
    }
    return res;
}

int main ()
{
    int T, A, B, K;
    cin >> T;
    For(test, T)
    {
        cin >> A >> B >> K;
        int res = solve(A, B, K);
        printf("Case #%d: %d\n", test + 1, res);
    }
    return 0;
}

