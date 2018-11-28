#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cmath>
#include <cctype>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <queue>
#include <utility>
#include <algorithm>
#include <bitset>

using namespace std;

/*
#define VI vector<int>
#define PII pair<int, int>
#define VPI vector<PII>
#define MII map<int, int>
#define LLI long long int
*/
#define SZ(x) ((int) (x).size())
#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)
#define MS(x, v) memset(x,v,sizeof(x))
#define FOR(n) for(int (i)=0;(i)<(n);++(i))
#define FORI(n) for(int (i)=1;(i)<=(n);++(i))
#define LGN 20
#define SZN 105
#define MXN 1005
#define _ ios_base::sync_with_stdio(0); // do not use scanf or printf with this

typedef long long int LLI;
typedef map<int, int> MII;
typedef pair<int, int> PII;
typedef vector<PII> VPI;
typedef vector<int> VI;

const int inf = 0x3f3f3f3f;
const double eps = 1e-6;
const double pi = acos(-1.0);

/* structs */

/* globals */
vector<string> words;
string str;

/* function declarations */
void dfs(int, string);


/* Problem */
int main() { _ // disable sync with stdio
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        cin >> str;
        string tmp(1, str[0]);
        dfs(1, tmp);
        sort(words.begin(), words.end());
        cout << words[words.size() - 1] << "\n";
        words.clear();
    }

    return 0;
}

void dfs(int index, string s) {
    if (index == str.length()) {
        words.push_back(s);
        return;
    }
    string c(1, str[index]);
    dfs(index+1, c+s);
    dfs(index+1, s+c);
}
