
#include <iostream>
#include <cstdio>
#include <string.h>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
using namespace std;

#define fr( i , c , n ) for( int i = (c) ; i < (n) ;i++ )
#define clr( a , c ) memset( a , c , sizeof a )
#define P pair<int , int>
#define ULL unsigned long long

#define maxn 1001

bool isPa[maxn];
int nrPa[maxn];
bool isPalindrome( int a )
{
	int aback = a;
	int b = 0;
	do
	{
		b = b*10 + a%10;
		a/= 10;
	}while(a);
	return aback == b;
}
void generate()
{
	clr( isPa , false );
	for( int i = 1 ; i*i < maxn ; i++ )
		if( isPalindrome( i ) && isPalindrome(i*i) )
			isPa[i*i] = true;
	nrPa[0] = 0;
	fr( i , 1 , maxn )
		nrPa[i] = nrPa[i-1] + isPa[i];
}
/*
bool isPalindrome( string a )
{
	int n = a.size();
	fr( i , 0 , n/2 )
		if( a[i] != a[n-1-i] )return false;
	return true;
}
string pow2( string a )
{
	string m;
	for( int i = a.size()-1 ; i >= 0 ; i-- )
	{
		int carry = 0;
		string ans;
		for( int j = a.size()-1 ; j >= 0 ;j-- )
		{
			int d = (a[j] - '0')*(a[i] - '0') + carry;
			ans= "" + '0'+d%10+ans;
			carry = d/10;
		}
		if( carry )
			ans = "" + '0'+ carry + ans;
	}
}
void generate()
{
	for( int i = 1 ; i < 50 ; i++ )// tedad ragham haye in palindrome
	{
	}
}*/
int main()
{
	generate();
	int T; cin >> T;
	fr( i , 1 , T+1 )
	{
		int a , b; cin >> a >> b;
		printf("Case #%d: %d\n", i , nrPa[b]  -nrPa[a-1] );
	}
	return 0;
}