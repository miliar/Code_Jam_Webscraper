// In the Name Of God

#include <iostream>
#include <fstream>

#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <istream>
#include <queue>
#include <cmath>
#include <stack>

#define inf (int)(~0u/2)
#define ll_inf (long long)1ll << 62
//#define int long long
#define float double
#define eps (1e-8)
#define for2(i, a, b) for ( int (i) = (a); (i)<(b); (i)++ )
#define mp make_pair
#define f1 first
#define f2 second
#define pb push_back
#define pii pair<int,int>
#define vpii vector <pii>
#define vi vector<int>
#define sz(a) (int) a.size( )
#define fillArr(n, a) for2(i, 0, n) cin >> a[i];
#define print(a) cout << #a << endl;
#define umax(a,b) a = max ( a, b )
#define umin(a,b) a = min ( a, b )
#define all(k) k.begin ( ), k.end( )
#define rall(k) k.rbegin ( ), k.rend( )
#define ll long long
#define clean(k) memset( k, 0, sizeof(k) )
using namespace std;

int a[20000];

void main ( ){
	int TTT;
	freopen ( "A-large.in", "r", stdin );
	freopen ( "A2.txt", "w", stdout );
	cin >> TTT;
	for2 ( LLL, 0, TTT ){
		int n, x;
		cin >> n >> x;
		for2 ( i, 0, n )
			cin >> a[i];
		sort ( a, a + n );
		int num = 0;
		int st = 0, e = n-1;
		while ( 1 ){
			if ( st == e ){
				num++;
				break;
			}
			if ( st > e ){
				break;
			}
			if ( a[e] + a[st] <= x ){
				num++;
				e--;
				st++;
			}
			else{
				num++;
				e--;
			}
		}
		cout << "Case #" << LLL+1 << ": " << num << endl;
	}
}