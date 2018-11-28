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

map<char, char> defeats;

string cad(char c, int rounds)
{
    if (rounds == 0)
        return string(1,c);
    string a = cad(c, rounds-1);
    string b = cad(defeats[c], rounds-1);
    return min(a+b, b+a);
}

int main()
{
    defeats['R'] = 'S';
    defeats['S'] = 'P';
    defeats['P'] = 'R';
    int totalCasos;
	cin >> totalCasos;
	forn(caso,totalCasos)
	{
        tint N,R,P,S;
        cin >> N >> R >> P >> S;
        string ret = "Z";
        for (char c : "RPS")
        {
            string s = cad(c, N);
            tint sR = count(all(s), 'R');
            tint sP = count(all(s), 'P');
            tint sS = count(all(s), 'S');
            if (sR == R && sP == P && sS == S)
                ret = min(ret, s);
        }
        if (ret == "Z") ret = "IMPOSSIBLE";
		cout << "Case #" << caso + 1 << ": " << ret << endl;
		cerr << "Case #" << caso + 1 << ": " << ret << endl;
	}
	return 0;
}
