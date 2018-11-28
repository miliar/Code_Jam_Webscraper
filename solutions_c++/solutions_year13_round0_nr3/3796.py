#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <ctime>
#include <math.h>
#include <algorithm>
#include <iomanip>
#include <assert.h>
#include <map>
#include <queue>
#include <cstring>
#include <set>
using namespace std;

typedef unsigned long long int ull;
typedef long long int ll;
#define vi vector<int>
#define vvi vector< vector<int> >
#define vd vector<double>
#define vb vector<bool>
#define vs vector<string>
#define pi pair<int,int>
#define pb push_back
#define out(a) cout<<(a)<<endl
#define pout(a,b) cout<<(a)<<' '<<(b)<<endl
#define sz(c) (int)(c).size()
#define foreach(n,i) for(int (i)=0;(i)<(n);(i)++)
#define range(s,e,i) for(int (i)=(s);(i)<=(e);(i)++)
#define all(c) (c).begin(),(c).end()
template<typename typ> void vout(vector<typ>& v){for(int vint=0;vint<sz(v);vint++)cout<<(v)[vint]<<' ';cout<<endl;}
template<typename typ> void arrout(typ* arr,int l){for(int i=0;i<l;i++)cout<<arr[i]<<' ';cout<<endl;}

#define debug
#ifdef debug
#define dbg(a) cout << #a << ' ' << a << endl
#endif
#ifndef debug
#define dbg(a)
#endif

bool ispalindrome(int);
int main()
{
    int T;
    cin >> T;
    for(int t = 1 ; t <= T ; ++t)
    {
    	printf("Case #%d: ",t);
    	int a,b;
    	cin >> a >> b;
    	a = int(ceil( sqrt(a) ));
    	b = int( floor(sqrt(b)) );
    	int ans = 0;
    	for(int n = a ; n <= b ; ++n)
    	{
    		if( ispalindrome(n) && ispalindrome(n * n) )
    			++ans;
    	}
    	cout << ans << endl;
    }
}

bool ispalindrome(int n)
{
	vi num;
	while(n)
	{
		num.pb(n % 10);
		n /= 10;
	}
	for(int i = 0 ; i < sz(num) ; ++i)
		if( num[i] != num[sz(num) - i - 1] )
			return false;
	return true;
}