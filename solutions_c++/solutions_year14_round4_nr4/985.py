/* Divanshu Garg */

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <climits>
#include <cctype>
#include <cassert>

using namespace std;

#define ull unsigned long long
#define ill long long int
#define pii pair<int,int>
#define pb(x) push_back(x)
#define F(i,a,n) for(int i=(a);i<(n);++i)
#define FD(i,a,n) for(int i=(a);i>=(n);--i)
#define FE(it,x) for(it=x.begin();it!=x.end();++it)
#define V(x) vector<x>
#define mod 1000000007
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%llu",&x)
#define M(x,i) memset(x,i,sizeof(x))
#define debug(i,sz,x) F(i,0,sz){cout<<x[i]<<" ";}cout<<endl
#define MAX(a,b) ((a)>(b)?(a):(b))
int ABS(int a) { if ( a < 0 ) return (-a); return a; }
#define fr first
#define se second

/* Relevant code begins here */

/* Input from file or online */

void input() {
#ifndef ONLINE_JUDGE
    // freopen("input.txt","r",stdin);
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
#endif
}

#define INF 10000000

int m,n;
vector <string> s;
int ddd[1LL<<10][11];
int dp[1LL<<10][11];
int dd[1LL<<10];

int f (int mask, int n)
{
    if (n == 0) {
        return 0;
    }



    int &result = ddd[mask][n];
    if (result != -1) {
        return result;
    }
    result = 1;
    int i;

    for (i = 1; i < (1LL<<m); i++) {
        if ((i&mask) != 0) {
            continue;
        }

        int nn = (i|mask);

        if (n == 1 && nn != ((1LL<<m)-1)) {
            continue;
        }

        result = max (result, dd[i]+f(nn, n-1));

    }

    return result;
}



int ff (int mask, int n)
{
    if (n == 0) {
        return 1;
    }

    int &result = dp[mask][n];
    if (result != -1) {
        return result;
    }
    result = 0;
    int i;

    for (i = 1; i < (1LL<<m); i++) {
        if ((i&mask) != 0) {
            continue;
        }

        int nn = (i|mask);

        if (n == 1 && nn != ((1LL<<m)-1)) {
            continue;
        }

        if (dd[i]+f(nn,n-1) == f(mask, n)) {
            result += ff (nn, n-1);
            result = result%mod;
        }


    }

    return result;
}


struct node
{
    char ch;
    struct node *next[26];
};
typedef struct node node;
struct node *head;
int sss;

void insert (string b, int index, struct node **s)
{
    if (index == b.size()) {
        return;
    }

    if ((*s) == NULL) {
        sss++;
        (*s) = (node*)malloc(sizeof(node));
        for (int i = 0; i < 26; i++) {
            (*s) -> next[i] = NULL;
        }
    }
    if (index+1 == b.size()) {
        return;
    }
    insert (b, index+1, &((*s)->next[b[index+1]-'A']));
}

int get (vector <string> a)
{
    head = NULL;
    sss = 1;

    head = (node*)malloc(sizeof(node));
    for (int i = 0; i < 26;  i++) {
        head->next[i] = NULL;
    }

    int i;
    for (i = 0; i < a.size(); i++) {
        insert (a[i], 0, &(head->next[a[i][0]-'A']));
    }

    return sss;
}



int main() {
    input();
    int t;
    cin >> t;
    int tst = 1;
    while ( t-- ) {
        cout << "Case #" << tst++ << ": ";
        S (m);
        S (n);


        s.clear();      s.resize (m);
        int i,j;
        F (i, 0, m) {
            cin >> s[i];
        }


        for (i = 0; i < (1LL<<m); i++) {
            vector <string> a;
            for (j = 0; j < m; j++) {

                if ( ((1<<j)&i) != 0 ) {

                    a.pb (s[j]);
                }

            }
            dd[i] = get(a);
        //    cout << i << " " << a.size() << " ==------ " << dd[i] << endl;
        }

        memset (ddd, -1, sizeof(ddd));
        int x = f (0, n);

        cout << x << " ";
        memset (dp, -1, sizeof(dp));

        cout << ff (0, n) << endl;
    }
    return 0;
}