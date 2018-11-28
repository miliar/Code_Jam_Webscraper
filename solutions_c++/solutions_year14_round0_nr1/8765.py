#include <iostream>
#include <sstream>
#include <cstdio>
#include <climits>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
#include <deque>
#include <bitset>
#include <map>
#include <set>
#include <stack>
#include <list>
#include <vector>
#include <queue>

using namespace std;

#define CLR(a) memset(a, 0, sizeof(a))
#define ABS(X) ( (X) > 0 ? (X) : ( -(X) ) )
#define SZ(V) (int )V.size()
#define ALL(V) V.begin(), V.end()
#define RALL(V) V.rbegin(), V.rend()
#define FORN(i, n) for(i = 0; i < n; i++)
#define FORAB(i, a, b) for(i = a; i <= b; i++)
#define si(n) scanf("%d",&n)
#define ss(s) scanf("%s",s)
#define prin(n) printf("%d\n",n)
#define pll pair < long long int, long long int >
#define pii pair < int, int >
#define psi pair < string, int >
#define PB push_back  
#define MP make_pair
#define F first
#define S second
#define MOD 1000000007LL
#define sieve(a) ({int b=ceil(sqrt(a));vector<int> d(a,0);vector<int> e;int f=2;e.push_back(2);e.push_back(3);for(int x=1;x<b+1;x++){for(int y=1;y<b+1;y++){int n=(4*x*x)+(y*y);if(n<=a&&(n%12==1||n%12==5)){d[n]^=1;}n=(3*x*x)+(y*y);if(n<=a&&n%12==7){d[n]^=1;}n=(3*x*x)-(y*y);if(x>y&&n<=a&&n%12==11){d[n]^=1;}}}for(int r=5;r<b+1;r++){if(d[r]){for(int i=r*r;i<a;i+=(r*r)){d[i]=0;}}}for(int c=5;c<a;c++){if(d[c]){e.push_back(c);}}e;})

typedef pair<int,int> PII;
typedef pair<double, double> PDD;
typedef long long LL;


int gcd(int a, int b)
{
	int temp;
	while(b)
	{
		temp = a % b;
		a = b;
		b = temp;
	}

	return(a);
}
LL pow(LL n,LL p){ 
	LL a=1,x=n;
	while(p>0){
		if(p&1){
			a*=x;
		}   
		x=x*x;
		p/=2;
	}   
	return a;
}
int main()
{
	int T,r1,r2,flag,ans;
	int arr[4][4];
	int dp[4];
	cin >> T;
	for(int t=1;t<=T;t++)
	{
		cin >> r1;flag=0;
		r1--;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				cin >> arr[i][j];
		for (int i = 0; i < 4; ++i)
			dp[i]=arr[r1][i];
		cin >> r2;
		r2--;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				cin >> arr[i][j];
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				if (dp[i]==arr[r2][j])
					flag++,ans = dp[i];
		if(flag==0)
			cout <<"Case #" << t <<": Volunteer cheated!"<< endl;
		else if(flag>1)
			cout <<"Case #" << t <<": Bad magician!"<< endl;
		else
			cout <<"Case #" << t <<": "<< ans << endl;
	}
	return 0;
}
