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

#define forall(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define dforall(i,c) for(typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)
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

const int MAXN = 256;
const int MAXW = 2300;

vector<int> linea[MAXN];
vector<int> words[MAXW];
int c[2][MAXW];

map<string, int> idWord;

int cres;
int res;

void backtracking(int i)
{
    if (i < 2)
    {
        res = min(res, cres);
        return;
    }
    forn(k, 2)
    {
        for (auto x : linea[i])
        {
            if (c[k][x] == 0 && c[!k][x] > 0) cres++;
            c[k][x]++;
        }
        backtracking(i-1);
        for (auto x : linea[i])
        {
            c[k][x]--;
            if (c[k][x] == 0 && c[!k][x] > 0) cres--;
        }
    }
}

int main()
{
	int totalCasos;
	cin >> totalCasos;
	forn(caso,totalCasos)
	{
        int maxW = 0;
        idWord.clear();
        int N; cin >> N;
        string s;
        getline(cin, s);
        forn(i,N)
        {
            linea[i].clear();
            getline(cin, s);
            istringstream inpu(s);
            string word;
            while (inpu >> word)
            {
                if (!esta(word, idWord))
                {
                    words[maxW].clear();
                    idWord[word] = maxW++;
                }
                linea[i].push_back(idWord[word]);
                words[idWord[word]].push_back(i);
            }
        }
        res = maxW;
        forn(k,2)
        {
            forn(i,maxW) c[k][i] = 0;
            for(auto x : linea[k]) c[k][x] = 1;
        }
        cres = 0;
        forn(x,maxW) cres += c[0][x] && c[1][x];
        backtracking(N-1);
        cout << "Case #" << caso + 1 << ": " << res << endl;
	}
	return 0;
}
