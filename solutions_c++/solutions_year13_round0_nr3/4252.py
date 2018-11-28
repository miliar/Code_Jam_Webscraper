#include <string>
#include <vector>
#include <list>
#include <iostream>
#include <set>
#include <queue>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <map>

#define FOR(i,a,b) for(int (i) = (a); (i) < (b); ++(i))  
#define RFOR(i,a,b) for(int (i) = (a)-1; (i) >= (b); --(i))  
#define CLEAR(a) memset((a),0,sizeof(a))  
#define INF 1000000000  
#define PB push_back  
#define ALL(c) (c).begin(), (c).end()  
#define pi acos(-1.0)  
#define SQR(a) (a)*(a)  
#define MP make_pair  
#define MAX 1e+9
#define MOD 1000000007

using namespace std;

vector<long long> v;

bool p(long long x)
{
 long long r=0;
 long long rr=x;
 while (x>0)
 {
	 r=r*10+x%10;
	 x/=10;
 }
 return (r==rr);
}

long long f2(long long x)
{
long long r=x;
while (x>0)
	{
		r*=10;
		r+=x%10;
		x/=10;
	}
return r;
}

long long f3(long long x,int t)
{
long long r=x*10+t;
while (x>0)
	{
		r*=10;
		r+=x%10;
		x/=10;
	}
return r;
}

int main()
{	
 freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);

	FOR(i,1,1001)
	{
		if (p(f2(i)*f2(i))) 
			v.PB(f2(i)*f2(i));
			//cout << f2(i) << " " << f2(i)*f2(i) << endl;
	
		FOR(j,0,10)
			if (p(f3(i,j)*f3(i,j)))
			v.PB(f3(i,j)*f3(i,j));
				//cout << f3(i,j) << " " << f3(i,j)*f3(i,j) << endl;

	}
	
	FOR(i,1,10) if (p(i*i)) v.PB(i*i);
sort(ALL(v));
	//FOR(i,0,v.size())
	//	cout << v[i] << endl;

long long a,b;
int t,sol;
cin >> t;
	FOR(i,1,t+1)
	{
		cin >> a >> b;
		sol=0;
		FOR(j,0,v.size())
			if (v[j]>=a && v[j]<=b) sol++;

		cout << "Case #" << i << ": " << sol << endl;
	}

return 0;
}