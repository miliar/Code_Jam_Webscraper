#include <iostream>
#include <fstream>
#include <cstdio>
#include <sstream>
#include <string>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <iomanip>
#include <cstring>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
#define SZ size()
#define PB push_back
#define SORT(a) sort((a).begin(), (a).end())
#define REV(a) reverse((a).begin(), (a).end())
#define FOR(i, a, b) for(int i = (a); i < (b); i++)
#define TR(i, a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define DEBUG(a) cout << #a << ": " << (a) << endl;
#define DEBUG1D(a, x1, x2) { cout << #a << ":"; for(int _i = (x1); _i < (x2); _i++){ cout << " " << a[_i]; } cout << endl; }
#define DEBUG2D(a, x1, x2, y1, y2) { cout << #a << ":" << endl; for(int _i = (x1); _i < (x2); _i++){ for(int _j = (y1); _j < (y2); _j++){ cout << (_j > y1 ? " " : "") << a[_i][_j]; } cout << endl; } }

const int oo = 777777777;

vector<string> dict;

struct node
{
    bool hasWord;
    int children[26];
    node()
    {
        hasWord = false;
        FOR(i, 0, 26) children[i] = -1;
    }
};

node T[1333333];
int size;

void insertWord(string word)
{
    int ind = 0;
    FOR(i, 0, word.SZ)
    {
        int letter = int(word[i] - 'a');
        if(T[ind].children[letter] == -1)
        {
            T[ind].children[letter] = size;
            T[size] = node();
            size++;
        }
        ind = T[ind].children[letter];
    }
    T[ind].hasWord = true;
}

string S;
int s[4444], f[4444][5], n;

int changeCnt;
inline void tryWords(int ind, int i, int prevChangeInd)
{
    //cout << ind << " " << i << " " << prevChangeInd << " " << changeCnt << "     " << T[ind].hasWord << endl;
    if(i >= n) return;
    if(ind != 0 and T[ind].hasWord)
    {
        int prev = (i - prevChangeInd >= 4 ? 4 : i - prevChangeInd);
        f[i][prev] = min(f[i][prev], changeCnt);
        //cout << "!!!" << "  " << prev << " " << f[i][prev] << "  " << changeCnt << endl;
    }
    if(i + 1 - prevChangeInd >= 5)
    {
        FOR(letter, 0, 26) if(letter != s[i + 1] and T[ind].children[letter] != -1)
        {
            changeCnt++;
            tryWords(T[ind].children[letter], i + 1, i + 1);
            changeCnt--;
        }
    }
    if(T[ind].children[s[i + 1]] != -1)
    {
        tryWords(T[ind].children[s[i + 1]], i + 1, prevChangeInd);
    }
}

int solve()
{
    n = S.SZ + 1;
    FOR(i, 0, n) s[i + 1] = int(S[i] - 'a');
    FOR(i, 0, n) FOR(j, 0, 5) f[i][j] = oo;
    FOR(j, 0, 5) f[0][j] = 0;

    FOR(i, 0, n) FOR(j, 0, 5)
    {
        changeCnt = f[i][j];
        tryWords(0, i, i - j);
    }

    int res = oo;
    FOR(j, 0, 5) res = min(res, f[n - 1][j]);
    return res;
}

int main()
{
    T[0] = node();
    size = 1;
    ifstream fin("dict.txt");
    string word;
    while(fin >> word) insertWord(word);
    fin.close();

    freopen("Clarge.in", "r", stdin);
    freopen("Clarge.out", "w", stdout);
    int testCnt;
    cin >> testCnt;
    FOR(testNo, 1, testCnt + 1)
    {
        cin >> S;
        cout << "Case #" << testNo << ": " << solve() << endl;
    }
}
