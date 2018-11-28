#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <ctime>
#include <iomanip>
#include <iterator>
#include <set>
#include <string>

#define ii <int , int>


#define mp make_pair
#define all(v) v.begin(),v.end()
#define loop(i, n) for (int i = 0; i < n; i++)
#define pb push_back
#define sz(v) v.size()


using namespace std;

typedef long long ll;
typedef vector<int > vi;
typedef vector<vi> vii;
typedef pair ii pii;
typedef map ii mii;
typedef set <int > si;
typedef multiset <int > msi;
typedef multimap <int , int> mmi;

const ll nInf = -1000000000;
const ll pInf = 1000000000;
const ll mod  = 1000000007;

int solve();
int main()
{
	freopen( "input.txt", "r" , stdin);
	freopen( "output.txt", "w" , stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0;i < t; i++)
	{
		int res = solve();
		printf("Case #%d: %d\n", i + 1, res);
	}
	return 0;
}

int solve()
{
	int d;
//	int *diners = new int [d];
	scanf("%d", &d);
	multiset <int, std::greater<int>> diners;
	multiset <int, std::greater<int>> diners1;
	for (int i = 0;i  < d; i++)
	{
		int a;
		scanf("%d", &a);
		diners.insert(a);
		diners1.insert(a);
//		cout << setw(5) << a << " ";
	}
	int minres = pInf;
	int a = 1000;
	int i = 0;
//	minres = min(minres, (*diners.begin()));
	while (a != 1)
	{
		multiset<int, std::greater<int>>::iterator it = diners.begin();
		a = (*it);

		diners.erase(it);
		minres = min(minres, a + i);
		int newd1= 0, newd2 = 0;
		newd1 = a / 2;
		newd2 = a - newd1;
		diners.insert(newd1);
		diners.insert(newd2);
		i++;
	}
	a = 100;
	i = 0;
	while (a != 1)
	{
		multiset<int, std::greater<int>>::iterator it = diners1.begin();
		a = (*it);

		diners1.erase(it);
		minres = min(minres, a + i);
		if (a == 9)
		{
			diners1.insert(3);
			diners1.insert(3);
			diners1.insert(3);
			i += 2;
		}
		else
		{
			int newd1= 0, newd2 = 0;

			newd1 = a / 2;
			newd2 = a - newd1;
			diners1.insert(newd1);
			diners1.insert(newd2);
			i++;
		}
	}
	return minres;
}