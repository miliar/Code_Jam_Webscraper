
//{{{
#define DEF
#ifdef DEF
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <functional>
#include <stack>
#include <vector>
#include <list>
#include <map>
#include <cctype>
#include <queue>
#include <cstring>
#include <cmath>
#include <set>
#include <deque>


//-----------------------------------------------------


using namespace std;
typedef unsigned int uint;
typedef long long int llint;
typedef unsigned long long int ullint;

typedef pair<int,int> Pii;
typedef pair<llint,llint> Pll;

#define mrepp(i,n,x)  for(int i = n-1; i >= x; i--)
#define mrep(i,n) mrepp(i,n,0)
#define repp(i,x,n)  for(int i = x; i < n; i++)
#define rep(i,n) repp(i,0,n)
#define pb        push_back
#define all(vec)  (vec).begin(),(vec).end()
#define each(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
//#define reach(i,c) for(__typeof((c).rbegin()) i=(c).rbegin();i!=(c).rend();i++)
#define fst         first
#define scd         second

#define sz(v)     ((llint)(v).size())
//#define bit(n)    (1ll<<(li)(n))
//#define mkP        make_pair

//-----------------------------------------------------
#endif
//}}}

llint a,b;
const llint MAX_X = 10000100;
llint pds[41] = 
{1 ,4 ,9 ,121 ,484 ,10201 ,12321 ,14641 ,40804 ,44944 ,1002001 ,1234321 ,4008004 ,100020001 ,102030201 ,104060401 ,121242121 ,123454321 ,125686521 ,400080004 ,404090404 ,10000200001 ,10221412201 ,12102420121 ,12345654321 ,40000800004 ,1000002000001 ,1002003002001 ,1004006004001 ,1020304030201 ,1022325232201 ,1024348434201 ,1210024200121 ,1212225222121 ,1214428244121 ,1232346432321 ,1234567654321 ,4000008000004 ,4004009004004 ,100000020000001 };

bool palindrome(llint a){
	char temp[100];
	int n = sprintf(temp,"%lld",a);
	rep(i,n/2) if( temp[i] != temp[n-1-i] ) return false;
	return true;
}

int main(){
	int T;cin >> T;
	rep(t,T){
		printf("Case #%d: ",t+1);
		cin >> a >> b;
		int e = 0;int s=-1;
		for(;  b >= pds[e] ; e++)
			if( a > pds[e] ) s = e;
		cout << e - s -1<< endl;
		
	}
	
	/*
	for(llint x = 1; x < MAX_X; x++)
		if( palindrome(x) && palindrome(x*x) ) cout << x*x << endl;
	*/
	
	return 0;
}
