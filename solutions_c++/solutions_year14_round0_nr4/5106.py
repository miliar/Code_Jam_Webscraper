
#include <vector>
#include <stack>
#include <cmath>
#include <algorithm>
#include <functional>
#include <vector>
#include <deque>
#include <sstream>
#include <iostream>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <set>
#include <cstring>
#include <climits>
#include <map>
#define LOGMAXN 20
#define EPS 0.000001
using namespace std;

vector < vector <int> > s;
vector <pair <int, int> > res;
vector <double> a,b;
int dp[1LL<<10][1LL<<10][11];
int n;


struct node
{
	int val;
	struct node *next;
};


struct node *head;


void fun ( int n )
{
	struct node *p;
	p = head;

	cin >> p->val;
	n--;
	while ( n-- ) {

		p->next = ( struct node* ) malloc ( sizeof ( struct node ) );
		p = p->next;
		cin >> p->val;
		p->next = NULL;
	}

	return;
}


bool kuhn (int v, vector <bool> &used, vector <int> &pair)
{
    if (used[v]) {
        return false;
    }
    int i;
    used[v] = true;
    for (i = 0; i < s[v].size(); i++) {
        int to = s[v][i];
        if (pair[to] == -1 || kuhn (pair[to], used, pair)) {
            pair[to] = v;
            return true;
        }
    }
    return false;
}

int bpm(int n, int k)
{
    vector <int> pair (k, -1);
    vector <bool> used (n, false);
    res.clear();
    int i;
    for (i = 0; i < n; i++) {
        fill (used.begin(), used.end(), false);
        kuhn (i, used, pair);
    }
    int sum=0;

    for (i = 0; i < k; i++) {
        if (pair[i] != -1) {
            res.push_back (make_pair (pair[i], i));
            sum++;
        }
    }
    return sum;
}


int matrix_chain_multiplication (int i, int j)
{
    if (i == j)
        return 0;

    int ret;

    if (ret != -1)
        return ret;

    ret = 0;
    for (int k = i; k < j; k++) {
        int temp = matrix_chain_multiplication(i, k) + matrix_chain_multiplication(k + 1, j);
        ret = min (temp, ret);
    }

    return ret;
}


int result1( vector <double> a, vector <double> b)
{
    s.clear();
    s.resize (55);

    int i,j;
    for (i = 0; i < a.size(); i++) {
            for (j = 0; j < b.size(); j++) {
                    if (a[i] > b[j]) {
                        s[i].push_back (j);
                    }
            }
    }
    return bpm (11,11);
}



bool check (int mask , int x)
{
    x = (1LL<<x);
    int xx = (mask | x);
    return (mask == xx);
}
int coin_change (vector<int>& s, int m, int n)
{

    if (n == 0)
        return 1;

    if (m < 0 || n < 0)
        return 0;

    int ret;
    //cout << n << "   " << ret << endl;
    if (ret != -1)
        return ret;

    ret = 0;
    ret = ret + coin_change(s, m, n - s[m]) + coin_change(s, m - 1, n);

    return ret;
}
int f (int aa, int bb, int flag)
{
    if (bb == (1LL<<n)-1) {
    if (flag != 0) {
        return 0;
    }
    return 0;
}
        int &result = dp[aa][bb][flag];
if (dp[aa][bb][flag] != -1) {        return result;
}    int i;
result = 0;    if (flag == 0) {
        for (i = 0; i < n; i++) {
        if (check (aa, i)) {
            continue;
        }
        result = max (result, f (aa|(1LL<<i), bb, i+1));
    }
    return result;
} else {            result = 10000000;

    for (i = 0; i < n; i++) {
        if (check (bb, i)) {
            continue;
        }
        if (b[i] > a[flag-1]) {
            result = min (result, f (aa, bb|(1LL<<i), 0));
            continue;
        }
        result = min (result, 1+f (aa, bb|(1LL<<i), 0));
    }
    return result;
}    return -1;}

int ff( vector <double> a, vector <double> b)
{
    memset (dp, -1, sizeof(dp));
    return f (0, 0, 0);
}

int main()
{
    //    freopen ("input.txt", "r", stdin);
    freopen ("D-small-attempt0.in", "r", stdin);
    freopen ("output.txt", "w", stdout);

    int t;
 cin >> t;
    int ii = 1;
    while (t--) {
        cout << "Case #" << ii++ << ": ";
        cin >> n;a.resize (n);b.resize (n);int i;
        for (i = 0; i < n; i++) {cin >> a[i];}
        for (i = 0; i < n; i++) {cin >> b[i];}
        int sum = result1 (a, b);cout << result1(a,b) << " ";cout << ff(a, b) << endl;
    }

    return 0;
}
