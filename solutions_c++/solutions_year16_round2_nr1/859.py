#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <cstring>
#include <deque>
#include <stack>
#include <stdio.h>
#include <map>
#include <set>
#include <time.h>
#include <string>
#include <fstream>
#include <queue>
#include <bitset>
#include <cstdlib>
#define X first
#define Y second
#define mp make_pair
#define pb push_back
#define pdd pair<double,double>
#define pii pair<ll,ll>
#define PI 3.14159265358979323846
#define MOD 1000000007
#define MOD2 1000000009
#define INF (1LL+(ll)1e+9)
#define x1 fldgjdflgjhrthrl
#define x2 fldgjdflgrtyrtyjl
#define y1 fldggfhfghjdflgjl
#define y2 ffgfldgjdflgjl
#define SQ 500400
#define CI 43534
#define N 228228
#define eps 1e-9
typedef long long ll;
typedef long double ld;
using namespace std;
ll n, k,j,i,m,q,ii,timer,x1,x,y,l,nodes_sz;
ll a[100500];
ll ans[50];
string s;
void do_magic(string s, char c, ll n)
{
	ll k = a[c];
	ans[n] += k;
	for (int i = 0; i < s.size(); i++)
		a[s[i]] -= k;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	ll tests;
	cin >> tests;
	for (int ii = 0; ii < tests; ii++)
	{
		for (i = 'A'; i <= 'Z'; i++)
			a[i] = 0;
		cin >> s;
		for (i = 0; i < 10; i++)
			ans[i] = 0;
		for (i = 0; i < s.size(); i++)
			a[s[i]]++;
		do_magic("ZERO",'Z',0);
		do_magic("TWO",'W',2);
		do_magic("SIX",'X',6);
		do_magic("EIGHT",'G',8);
		do_magic("SEVEN",'S',7);
		do_magic("FIVE",'V',5);
		do_magic("FOUR",'U',4);
		do_magic("NINE",'I',9);
		do_magic("THREE",'H',3);
		do_magic("ONE",'O',1);
		printf("Case #%d: ", ii+1);
		for (i = 0; i < 10; i++)
			for (j = 0; j < ans[i]; j++)
				cout << i;
		cout << endl;
	}
	return 0;
}
