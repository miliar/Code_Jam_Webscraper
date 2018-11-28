/* Dijkstra
 * CodeJam 2015
 * Google
 * Date : 11/04/2015
 */
#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<cstring>
using namespace std;

typedef long long ll;

const ll MAX = 10002;

bool mulSign(char x,char y)
{
	if( x == '1' && y == '1') return false;
	if( x == '1' || y == '1') return false;
	if( x == y ) return true;
	if( (x == 'i' && y == 'k') || (x == 'j' && y == 'i') || ( x == 'k' && y == 'j' )) return true;
	return false; 	
}
char mul(char x,char y)
{
	if( x == '1') return y;
	if( y == '1') return x;
	if( x == y ) return '1';
	switch(x)
	{
		case 'i': 
			if( y == 'j') return 'k';
			if( y == 'k') return 'j';
		case 'j':
			if( y == 'i') return 'k';
			if( y == 'k') return 'i';
		case 'k':
			if( y == 'i') return 'j';
			if( y == 'j') return 'i';
	}
}

bool isPossible(char *s,ll l,ll x)
{
	bool isNegative = false;
	bool iFound = false;
	bool jFound = false;
	char current = '1';
//	cout<<s<<endl;
	for( ll i = 0; i < x;i++)
	{
		for(ll j=0; j < l; j++)
		{
			//multiplying 
			isNegative = isNegative ^ mulSign(current,s[j]);
			current = mul(current, s[j]);

			// 1 * [i]  == i
			if( !isNegative	&& current == 'i') iFound = true;
			// i * [j] == k
			if( !isNegative && iFound && current == 'k') jFound = true;
		}
	}
	// k * [-k]  == 1
	if( iFound && jFound && isNegative && current == '1') return true;
	else return false;

}
int main(void)
{
	ll t,l,x;
	char s[MAX];
	scanf("%lld",&t);
	for(ll i=1;i<=t;i++)
	{
		scanf("%lld%lld",&l,&x);
		scanf("%s",s);
		if( isPossible(s,l,x) )
			printf("Case #%lld: YES\n",i);
		else
			printf("Case #%lld: NO\n",i);
	}
	return 0;
}
/********************************* END OF PROGRAM **************************/
