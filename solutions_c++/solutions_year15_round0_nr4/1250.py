/* Ominus Omino
 * CodeJam 2015
 * Google
 * Date : 12/04/2015
 * Only for small input
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

enum players { richard = 1,gabriel = 2};

void swap(int &a,int &b)
{
	int t = a;
	a  = b;
	b = t;
}

int winner(int x,int r,int c )
{
	if( r > c ) swap(r,c );
	if( (r * c ) % x != 0) return richard;
	if( x < 3 ) return gabriel;

	bool winner = false;

	winner |= ( x==3) && (r==2) && (c==3);
	winner |= ( x==3) && (r==3) && (c==3);
	winner |= ( x==3) && (r==3) && (c==4);
	winner |= ( x==4) && (r==3) && (c==4);
	winner |= ( x==4) && (r==4) && (c==4);

	if( winner ) return gabriel;
	else return richard;
}

int main(void)
{
	int t,x,r,c;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%d%d%d",&x,&r,&c);
		if( winner(x,r,c) == richard )
			printf("Case #%d: RICHARD\n",i);
		else 
			printf("Case #%d: GABRIEL\n",i); 
	}	
	return 0;
}
/********************************* END OF PROGRAM **************************/
