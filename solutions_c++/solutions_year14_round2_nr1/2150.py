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

string remove_duplicates(string v)
{
    v.resize(unique(v.begin(),v.end())-v.begin());
    return v;
}

bool impossible(vector<string> v)
{
    int n = (int)v.size();
    string unique = remove_duplicates(v[0]);
    for(int i = 1; i < n; ++i)
    {
        string cur = remove_duplicates(v[i]);
        if(unique != cur) return true;
    }
    return false;
}

vector<int> freq(string s)
{
    string unique = remove_duplicates(s);
    vector<int> res;
    int index = 0, n = (int)s.size();
    For(i, (int)unique.size())
    {
        int cur = 0;
        while((index < n) && (unique[i] == s[index]))
        {
            ++index;
            ++cur;
        }
        res.push_back(cur);
    }
    return res;
}

int dif(string a, string b)
{
    vector<int> A = freq(a), B = freq(b);
    int res = 0;
    assert((int)A.size() == (int)B.size());
    int n = (int)A.size();
    For(i, n) res += abs(A[i] - B[i]);
    return res;
}


int main ()
{
    int T;
    cin >> T;
    For(test, T)
    {
        int n;
        string ans;
        cin >> n;
        vector<string> v(n);
        For(i, n) cin >> v[i];
        bool im = impossible(v);
        if(im)
            ans = "Fegla Won";
        else{
            int res = INT_MAX;
            vector<string> candidates = v;
            string unique = remove_duplicates(v[0]);
            candidates.push_back(unique);
            for(string target: candidates)
            {
                int cur = 0;
                For(j, n)
                {
                    cur += dif(v[j], target);
                }
                res = min(res, cur);
            }
            ans = _itos(res);
        }
        printf("Case #%d: %s\n", test + 1, ans.c_str());
    }
    
//    string v[] = {"aaaabbbccccddbb", "abc", "gcj", "gggcccwwgg"};
//    For(i, 4)
//    {
//        vector<int> f = freq(v[i]);
//        db(v[i]);
//        out(f);
//    }
    return 0;
}

