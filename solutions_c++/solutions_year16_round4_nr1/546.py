#include <cassert>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;

#define debug(args...) {vector<string> _v = split(#args, ','); err(_v.begin(), args); puts("");}
vector<string> split(const string& s, char c) {vector<string> v; stringstream ss(s); string x; while (getline(ss, x, c)) v.emplace_back(x); return move(v);}
void err(vector<string>::iterator it) {}
template<typename T, typename... Args> void err(vector<string>::iterator it, T a, Args... args) {cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << ", "; err(++it, args...);}

#define pb push_back
#define mp make_pair
#define all(x)  (x).begin(),(x).end()
#define tr(c, it)   for(auto it=c.begin(); it!=c.end(); it++)
#define clr(a, b)   memset(a, b, sizeof(a))

int T;
int n, p, r, s;

string fun(string ss, int n)
{
    for(int i=0; i<n; i++)
    {
        //debug(ss);
        string tmp = "";
        int len = 1 << i;

        for(int l=0; l<ss.size(); l+=2*len)
        {
            string s1 = ss.substr(l, len);
            string s2 = ss.substr(l+len, len);
            //debug(s1, s2);

            if (s1 < s2) tmp += s1 + s2;
            else tmp += s2 + s1;
        }

        ss = tmp;
    }
    return ss;
}




int main()
{
#ifdef LOCAL
    //freopen("in", "r", stdin);

    //freopen("A-small-attempt3.in", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("out", "w", stdout);
#endif

    int cas = 1;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        scanf("%d%d%d",&r, &p, &s);

        printf("Case #%d: ", cas++);

        // r
        string res = "R";
        int rr = 1, ss = 0, pp = 0;
        for(int i=0; i<n; i++)
        {
            int tmpr = rr + pp;
            int tmps = rr + ss;
            int tmpp = ss + pp;
            rr = tmpr;
            ss = tmps;
            pp = tmpp;

            string tmpres = "";

            for(int j=0; j<res.size(); j++)
            {
                if(res[j] == 'R') tmpres += "RS";
                if(res[j] == 'S') tmpres += "PS";
                if(res[j] == 'P') tmpres += "PR";
            }
            res = tmpres;
        }


        if(r == rr && p == pp && s == ss)
        {
            res = fun(res, n);
            cout << res << endl;
            continue;
        }

        // s
        res = "S";
        rr = 0, ss = 1, pp = 0;
        for(int i=0; i<n; i++)
        {
            int tmpr = rr + pp;
            int tmps = rr + ss;
            int tmpp = ss + pp;
            rr = tmpr;
            ss = tmps;
            pp = tmpp;

            string tmpres = "";

            for(int j=0; j<res.size(); j++)
            {
                if(res[j] == 'R') tmpres += "RS";
                if(res[j] == 'S') tmpres += "PS";
                if(res[j] == 'P') tmpres += "PR";
            }
            res = tmpres;
        }

        if(r == rr && p == pp && s == ss)
        {
            res = fun(res, n);
            cout << res << endl;
            continue;
        }

        // p
        res = "P";
        rr = 0, ss = 0, pp = 1;
        for(int i=0; i<n; i++)
        {
            int tmpr = rr + pp;
            int tmps = rr + ss;
            int tmpp = ss + pp;
            rr = tmpr;
            ss = tmps;
            pp = tmpp;

            string tmpres = "";

            for(int j=0; j<res.size(); j++)
            {
                if(res[j] == 'R') tmpres += "RS";
                if(res[j] == 'S') tmpres += "PS";
                if(res[j] == 'P') tmpres += "PR";
            }
            res = tmpres;
        }

        if(r == rr && p == pp && s == ss)
        {
            res = fun(res, n);
            cout << res << endl;
            continue;
        }

        cout << "IMPOSSIBLE" << endl;




    }
    return 0;
}
