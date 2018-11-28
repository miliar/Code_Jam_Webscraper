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
	freopen("input3.in","r",stdin);
	freopen("output.txt","w",stdout);
	int cases;
	cin>>cases;
	REP(c1,cases)
	{
		int x,r,c;
		cin>>x>>r>>c;
		int f=0;
		if(x==1)
		{
			f=1;
		}
		else if(x==2)
		{
			if(r%2==0 || c%2==0)
				f=1;
		}
		else if(x==3)
		{
			if((r==2 && c==3) || (r==3 && c==2) || (r==3 && c==3) || (r==3 && c==4) || (r==4 && c==3))
				f=1;
		}
		else
		{
			if((r==4 && c==3) || (r==4 && c==4) || (r==3 && c==4))
				f=1;
		}
		cout<<"Case #"<<c1+1<<": ";
		if(f)
			cout<<"GABRIEL\n";
		else
			cout<<"RICHARD\n";
	}
}

