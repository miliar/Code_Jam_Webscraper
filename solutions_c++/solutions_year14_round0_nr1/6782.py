#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <queue>
#include <assert.h>
#include <cctype>
#include <string.h>
using namespace std;

#define INF_MAX 2147483647
#define INF_MIN -2147483647

#define pi acos(-1.0)
#define INF 1e9
#define ll long long

#define For(i, a, b) for( int i = (a); i < (b); i++ )
#define Fors(i, sz) for( size_t i = 0; i < sz.size (); i++ )
#define Fore(it, x) for(typeof (x.begin()) it = x.begin(); it != x.end (); it++)
#define mem(a, s) memset(a, s, sizeof (a))
#define Read() freopen("1.txt", "r", stdin)
#define Write() freopen("2.txt", "w", stdout)
#define sz(c) ((int)(c).size())
#define pb push_back
#define mp make_pair
#define all(v) v.begin(),v.end()
#define vi vector<int>
typedef pair<int,int> PAIR;
typedef pair<PAIR ,int> PAIR2;
string tostring(long long n){ostringstream ss; ss << n; return ss.str();}
long long tonumber(string str){stringstream ss; ss << str; long long n; ss >>n; return n;}

int main()
{
	freopen("1.txt", "r", stdin);
	freopen("2.txt", "w", stdout);
	int t;
	cin >> t;
	for (int Case = 0; Case < t; Case++)
	{
		int n1,n2;
		cin >> n1;
		bool ok1[17],ok2[17];
		mem(ok1,false);
		mem(ok2,false);
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				int x;
				cin >>x;
				if(i==n1-1)
					ok1[x]=true;
			}
		}
		cin >> n2;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				int x;
				cin >>x;
				if(i==n2-1)
					ok2[x]=true;
			}
		}
		bool more=false,pre=false;
		int res;
		for (int i = 1; i < 17; i++)
		{
			if(ok1[i]==true&& ok2[i]==true){
				if(pre==true){
					more=true;
					break;
				}
				pre=true;
				res=i;
			}
		}
		cout << "Case #"<<Case+1<<": ";
		if(pre==false)
			cout <<"Volunteer cheated!\n";
		else
		{
			if(more==true)
				cout <<"Bad magician!\n";
			else
				cout <<res << endl;
		}
	}
	return 0;
}