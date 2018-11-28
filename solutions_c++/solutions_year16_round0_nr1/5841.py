#include <stack>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <math.h>
#include <vector>
#include <string.h>
#include <iostream>
#include <stdio.h>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <iostream>  
#include <string>
#include <iomanip>
#include <ctime>
using namespace std;

#define EPS 1e-9
#define ABS(a) ( (a) < 0 ? -(a) : (a) )

const double PI = 4 * atan(1.0);
const int MAXN  = (int)(210);

typedef long long ll;
const ll INF = (int)1E9 + 10;
const int MOD = (int)(1001017);
const int P = 31;

#define mp make_pair 
#define FOR(i,s,f) for(int i=s; i<f; i++)

//  prime -> 1001017
//int dir[2][4] = {{ -1, 0, 1, 0 }, { 0, 1, 0, -1 }}; 
//************************************************

bool used[10];

bool check(ll n)
{
	while(n)
	{
		used[ n%10 ] = 1;
		n /= 10;
	}

	FOR(i,0,10)
	{
		if( !used[i] ) return false;
	}
	return true;
}

int main()
{
//freopen("A-large.in", "rb", stdin); 
//freopen("out.txt", "wt", stdout);
//unsigned int start_time =  clock();

/*cout << 5000 << endl;
FOR(i,995000,1000000)
	cout << i << endl;*/

int t; cin >> t;
FOR(i,0,t)
{

ll n; cin >> n;
memset(used,0,sizeof(used));

if(n != 0) 
{
	ll k=n, j=2;

	while(1)
	{
		if( check(k) ) break;

		k=n*j; j++;
	}

	n=k;
}

cout << "Case #"<< i+1 << ": ";
if( n == 0 ) cout <<"INSOMNIA\n";
else cout << n << "\n";

}

	return 0;
}

