#include <vector>
#include <queue>
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
#include <string.h>
#include <ctime>

using namespace std;

#define REP(i,n) for(int i=0; i<n; i++)
#define FOR(i,x,y) for(int i=x; i<=y; i++)

typedef long long ll;
main() {
	freopen("input1.in","r",stdin);
	freopen("output.txt","w",stdout);
	int cases;
	cin>>cases;
	REP(c,cases)
	{
		int n,res=0,ret=0;
		cin>>n;
		string a;
		cin>>a;
		REP(i,n+1)
			if(a[i]!='0')
			{
				ret+=max(0,i-res);
				res+=a[i]-'0'+max(0,i-res);
			}
		cout<<"Case #"<<c+1<<": "<<ret<<"\n";
	}
}

