#include <algorithm>
#include <assert.h>
#include <bitset>
#include <complex>
#include <cstring>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>
using namespace std;
template <class T> int size(const T &x) { return x.size(); }
#define rep(i,a,b) for (decltype(a) i=(a); i<(b); ++i)
#define iter(it,c) for (decltype((c).begin()) it = (c).begin(); it != (c).end(); ++it)
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
const int INF = ~(1<<31); // 2147483647

const double EPS = 1e-9;
const double pi = acos(-1);
typedef unsigned long long ull;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
template <class T> T smod(T a, T b) { return (a % b + b) % b; }

struct node
{
	char data;
	node* left, * right;
	node(char d, node* l = NULL, node* r = NULL) : data(d), left(l), right(r) {}
	~node() { if(!isleaf()) { delete left; delete right; } }
	bool isleaf() { return left == NULL; }
};

int p = 0, s = 0, r = 0;
void genrounds(node* win, int rounds)
{
	if(rounds == 0) return;
	else
	{
		if(win->data == 'P')
		{
			win->left = new node('P');
			win->right = new node('R');
			r++;
		}
		else if(win->data == 'R')
		{
			win->left = new node('R');
			win->right = new node('S');
			s++;
		}
		else if(win->data == 'S')
		{
			win->left = new node('P');
			p++;
			win->right = new node('S');
		}
		genrounds(win->left, rounds-1);
		genrounds(win->right, rounds-1);
	}
}

string balance(node* n)
{
	if(n->isleaf()) return string(1,n->data);
	else
	{
		string left = balance(n->left);
		string right = balance(n->right);
		if(right < left) return right+left;
		else return left+right;
	}
}

int main()
{
	int t;
	cin >> t;
	rep(i,0,t)
	{
		string res = "Z";
		int n, nr, np, ns;
		cin >> n >> nr >> np >> ns;
		node* win = new node('P');
		p = 1, r = 0, s = 0;
		genrounds(win, n);
		string bal = balance(win);
		if(np == p && nr == r && ns == s) res = min(res, bal);
		delete win;
		win = new node('R');
		p = 0, r = 1, s = 0;
		genrounds(win, n);
		bal = balance(win);
		if(np == p && nr == r && ns == s) res = min(res, bal);
		delete win;
		win = new node('S');
		p = 0, r = 0, s = 1;
		genrounds(win, n);
		bal = balance(win);
		if(np == p && nr == r && ns == s) res = min(res, bal);
		delete win;
		if(res == "Z") res = "IMPOSSIBLE";
		cout << "Case #" << (i+1) << ": " << res << endl;
	}

	return 0;
}