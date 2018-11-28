// بسم الله الرحمن الرحیم

#include <cstdio>
#include <sstream>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <set>
#include <queue>
#include <sstream>
#include <stack>
#include <list>
#include <iostream>
#include <fstream>
#include <numeric>
#include <string>
#include <vector>
#include <cstring>
#include <map>
#include <iterator>

using namespace std;

typedef long long ll;
typedef unsigned int ul;
typedef unsigned long long ull;
typedef vector <int> vi;
typedef set<int> si;
typedef set<string> ss;
typedef map<string,int>	msi;
typedef map<string,string> mss;
typedef map<int, vector<int> > mvii;
typedef map<string, vector <string> > mvss;
typedef map<char,int> mchi;
typedef map<int,char> mich;
typedef map<int, int> mii;
typedef queue <int> qi;
typedef map <int, vector<string> > mvis;
typedef map <string, vector<int> > mvsi;
typedef vector <string> vs;
typedef pair <int, int> pii;

#define MP make_pair
#define SORT(a) sort (a.begin(), a.end())
#define REVERSE(a) reverse (a.begin(), a.end())
#define PI acos(-1)
#define ms(x,y) memset (x, y, sizeof x)
#define INF 2000000
#define pb push_back
#define MAX (ll)524290
#define debug cout<<"A"<<endl;
#define prnt(a) cout<<a<<endl
#define mod 1000000009

//~ int gcd(int a, int b)
//~ {
	//~ while(b)
		//~ b^=a^=b^=a%=b;
	//~ return a;
//~ }

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w",stdout);
	vi ans;
	int test, first[5][5], second[5][5], n, m, cases=1;
	cin>>test;
	while (test--)
	{
		cin>>n;
		for (int i=0; i<4; i++)
			for (int j=0; j<4; j++)
				cin>>first[i][j];
		cin>>m;
		for (int i=0; i<4; i++)
			for (int j=0; j<4; j++)
				cin>>second[i][j];
		for (int i=0; i<4; i++)
		{
			for (int j=0; j<4; j++)
			{
				if (first[n-1][i]==second[m-1][j])
					ans.pb(first[n-1][i]);
			}
		}
		printf("Case #%d: ", cases++);
		if (ans.size()==0)
			cout<<"Volunteer cheated!"<<endl;
		else if (ans.size()>1)
			cout<<"Bad magician!"<<endl;
		else if (ans.size()==1)
			cout<<ans[0]<<endl;
		ans.clear();
	}
	return 0;
}

