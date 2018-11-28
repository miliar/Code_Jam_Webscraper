#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <numeric>
#include <functional>
#include <algorithm>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)
#define dforn(i,n) for(int i=(n)-1;i>=0;i--)
#define dforsn(i,s,n) for(int i=(n)-1;i>=(int)(s);i--)

#define forall(i,c) for(auto i = (c).begin(); i != (c).end(); i++)
#define dforall(i,c) for(auto i = (c).rbegin(); i != (c).rend(); i++)
#define all(c) (c).begin(),(c).end()

#define esta(x,c) ((c).find(x) != (c).end())
#define zMem(c) memset((c),0,sizeof(c))

typedef long long tint;
typedef long double tdbl;

typedef pair<int,int> pint;
typedef pair<tint,tint> ptint;

typedef vector<int> vint;
typedef vector<vint> vvint;
typedef vector<string> vstr;


string f(string s)
{
    if (s.empty()) return "";
    char maxi = *max_element(all(s));
    int L = find(all(s), maxi) - s.begin();
    string ms = string(count(all(s), maxi), maxi);
    string rest = s.substr(L);
    int rL = 0;
    forn(i,rest.size())
    if (rest[i] != maxi)
        rest[rL++] = rest[i];
    rest.resize(rL);
    return ms + f(s.substr(0,L)) + rest;
}

int main()
{	int totalCasos;
	cin >> totalCasos;
	forn(caso,totalCasos)
	{
        string s; cin >> s;
        string res = f(s);
		cout << "Case #" << caso + 1 << ": " << res << endl;
		cerr << "Case #" << caso + 1 << ": " << res << endl;
	}
	return 0;
}
