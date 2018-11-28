#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;
typedef long long ll;
typedef long double ld;
#define sz(x) ((int)(x).size())

int palindrome(ll inum)
{
	ll n, num,digit, rev = 0;
	 num = inum;
     n = num;
     do
     {
         digit = num%10;
         rev = (rev*10) + digit;
         num = num/10;
     }while (num!=0);
     if(n==rev)
     	return 1;
     else 
     	return 0;
     
}

int main()
{
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("C.out","wt",stdout);
	
	ll N;
	scanf("%lld",&N);
	for(ll T = 1; T <= N; ++T)
	{
		ll count = 0;
		ll A, B;
		scanf("%lld",&A);
		scanf("%lld",&B);
		
		for(ll a = A ; a <=B ;++a)
		{	
			ll temp = a;
			if(palindrome(temp))
		    {
				 ll c =  sqrt(temp);
				 if(temp == c*c)
				 {  if(palindrome(c))
				 	count++;
				 }
			}			
		}
		printf("Case #%lld: %lld\n", T, count);
		
	}
	return 0;
}

