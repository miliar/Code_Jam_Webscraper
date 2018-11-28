

//STL includes
#include <vector>
#include <algorithm>
#include <list>
#include <map>
#include <deque>
#include <queue>
#include <set>
#include <stack>
#include <string>


//C includes
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>


//Other includes
#include <iomanip>
#include <iostream>
#include <sstream>
#include <fstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>

#define sqr(x) ( (x)*(x) )
#define size(a) int((a).size()) 
#define pb push_back
#define all(c) (c).begin(),(c).end() 
#define SORT(x) sort(all(x))
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define inf 1000000	
#define mod 1000000007

typedef long long int ll;
typedef long double ld;
typedef unsigned int ui;
using namespace std;

int ps(int n);
bool pal(int num);

int main()
{
	int t,a,b;
	scanf("%d",&t);
	for(int i=1;i <= t;i++)
	{
		int c=0;
		scanf("%d%d",&a,&b);

		for (int x =a; x <=b; x++) 
		{
			if(!pal(x))
			{
				continue;
			}
			int res=ps(x);
			if(res!=0)
			{
				if( pal(res))
				{
					c++;
				}
			}
		}
		printf("Case #%d: %d\n",i,c);
	}
		
	
	return 0;
}

int ps(int n)
{
	int h = n & 0xF; // last hexidecimal "digit"
	if (h > 9)
		return 0; // return immediately in 6 cases out of 16.

	// Take advantage of Boolean short-circuit evaluation
	if ( h != 2 && h != 3 && h != 5 && h != 6 && h != 7 && h != 8 )
	{
		//                 // take square root if you must
		int t = (int) floor( sqrt((double) n) + 0.5 );
		//return t*t == n;
		if(t*t==n)
		{
			return t;
		}
	}
	return 0;
}

bool pal(int num)
{
	int n, digit, rev = 0;
	n = num;
	do
	{
		digit = num%10;
		rev = (rev*10) + digit;
		num = num/10;
	}while (num!=0);
	if (n == rev)
	{
		return true;
	}
		
	else
	{
		return false;
	}
}
