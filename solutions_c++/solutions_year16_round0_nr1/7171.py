#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;
 
#define REPEAT(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) REPEAT(i,0,n)
#define RREP(i,n) for(int i=n-1;i>=0;--i)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define sz size()
#define mkp make_pair
typedef long long ll;
#define EPS 1e-12

int go(int x)
{
	set <int> visited;
	REPEAT(i, 1, 100)
	{
		int t = x*i;
		int n = t;
		while(n){
			visited.insert(n%10);
			n/=10;
			}
		if(visited.sz == 10)
			return t;
	}

	return -1;
}

int main()
{
	int T;
	cin >> T;
	REP(c,T)
	{
		int N; 
		cin >> N;
		int ret = go(N);
		cout << "Case #" << c+1 << ": ";
		ret == -1 ? cout << "INSOMNIA\n" : cout << ret << "\n";
	}

	return 0;
}
	

	
