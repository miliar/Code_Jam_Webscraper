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

int solve();//1 - yes, 0 - no;
int getres(int a, int b);

int main()
{
	freopen( "input.txt", "r" , stdin);
	freopen( "output.txt", "w" , stdout);

	int t;
	scanf("%d", &t);
	for (int i = 0;i < t; i++)
	{
		int a = solve();
		printf("Case #%d: ", i + 1);
		if (a == 1)
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}

int solve()
{
	int l, x;
	scanf("%d %d", &l, &x);
	char *str = new char[l + 10];
	scanf("%s", str);
	string sstr = "";
	for (int i = 0;i < x; i++)
	{
		sstr += str;
	}
//	int length = strlen(str);
	int *nstr = new int[l * x];
	for (int i = 0; i < l * x; i++)
	{
		if (sstr[i] == 'i')
			nstr[i] = 2;
		if (sstr[i] == 'j')
			nstr[i] = 3;
		if (sstr[i] == 'k')
			nstr[i] = 4;
	}
//	int *hash = new int[l * x+4];
	vi hash(l * x, 0);
	hash[0] = nstr[0];
	for (int i = 1; i < l * x; i++)
	{
		hash[i] = getres(hash[i - 1], nstr[i]);
	}
	if (hash[l * x - 1] != -1)
		return 0;
	for (int i = 0; i < l * x; i++)
	{
		if (hash[i] == 2 && i != l * x - 1)
		{
			vi hash1(l * x, 0);
			hash1[i + 1] = nstr[i + 1];
			for (int j = i + 2; j < l * x; j++)
			{
				hash1[j] = getres(hash1[j - 1], nstr[j]);
			}
			for (int j = i + 1; j < l * x; j++)
			{
				if (hash1[j] == 3)
				{
					int res = 1;
					for (int k = j + 1; k < l * x; k++)
					{
						res = getres(res, nstr[k]);
					}
					if (res == 4)
					{
						return 1;
					}
				}
			}
		}
	}
// 	for (int i = 0;i < l * x; i++)
// 		cout << hash[i] << " ";
	return 0;
}


int getres(int a, int b)
{
	int res = 0;
	if (abs(a) == 2 && b == 3)
		res = 4;
	if (abs(a) == 2 && b == 4)
		res = -3;


	if (abs(a) == 3 && b == 2)
		res = -4;
	if (abs(a) == 3 && b == 4)
		res = 2;


	if (abs(a) == 4 && b == 2)
		res = 3;
	if (abs(a) == 4 && b == 3)
		res = -2;


	if (abs(a) == b)
		res = -1;
	if (abs(a) == 1)
		res = b;

	if (a < 0)
		res = 0 - res;
	return res;
}