#include <cmath>
#include <sstream>
#include<cstring>
#include<cstdlib>
#include <set>
#include <cstdio>
#include<map>
#include <cmath>
#include <map>
#include<fstream>
#include<algorithm>
#include <iostream>
#include<numeric>
#include<utility>
#include<functional>
#include<stdio.h>
#include<assert.h>
#include<memory.h>
#include<bitset>
#include <stack>
#include <queue>
#include <vector>
#include <unordered_map>
#include <iterator>
#include <math.h>
#include<cstring>
#define fast std::ios_base::sync_with_stdio(false);
#define LL long long
#define lp(i,n) for(int i=0;i<(int)n;i++)
#define endl "\n"
#define sz(v)   ((int)((v).size()))
#define PI 3.1415926536
#define read(file) freopen (file,"r",stdin)
#define write(file) freopen (file,"w",stdout)
#define ll long long
using namespace std;
LL gcd(LL a, LL b) { if(b==0) return a;   return gcd(b,a%b);  }
LL lcm (LL a, LL b) {   return a*(b/(gcd(a,b)));  }
inline int toInt(string s){int v; istringstream sin(s);sin>>v;return v;}
inline LL toLL(string s){LL v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) { ostringstream sout; sout << x; return sout.str();}

int P[105];
int n;
void solve()
{
	int sum = 0;
	vector<pair<int,char> > v;
	for(int i = 0 ; i < n ; i++)
	{
		v.push_back(make_pair(P[i],i+'A'));
		sum += P[i];
	}
	while(sum > 0)
	{
		sort(v.rbegin(),v.rend());
		int rest = 0;
		for(int i = 2 ; i < n ; i++) rest +=v[i].first;
		// case remove 2 from first
		int f_first = v[0].first - 2;
		if(v[1].first <= f_first + rest)
		{

			cout << " " << v[0].second << v[0].second;;
			sum -= 2;
			v[0].first -=2;
			continue;
		}
		// case remove one and one
		if(rest == 0 && v[0].first == v[1].first)
		{
			sum -= 2;
			cout << " " << v[0].second << v[1].second;
			v[0].first--; v[1].first--;
			continue;

		}
		sum--;
		v[0].first--;
		cout <<" " <<v[0].second;
	}
}
int main()
{
	fast
	int t;
	write("sol3.txt");
	memset(P,0,sizeof(P));
	cin >> t;
	int a;
	int tc = 1;
	while(t--)
	{
		cin >> n;
		memset(P,0,sizeof(P));
		for(int i = 0 ; i < n ; i++)
		{
			cin >> a;

			P[i] += a;
		}
		cout << "Case #"<<(tc++)<<":";
		solve();
		cout << endl;
	}
}
