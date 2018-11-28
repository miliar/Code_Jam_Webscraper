#include<bits/stdc++.h>
using namespace std ;
#define pb push_back
#define mp make_pair
#define infile() freopen("large.in","r",stdin);
#define output() freopen("output.txt","w",stdout);
set <long long  > s ; 
set <long long >::  iterator it  ; 
long long func(long long n)
{
	long long i , j , k, l  , t , temp ; 
//	printf("n == %lld size == %d\n" , n ,s.size())  ;
	while(n)
	{
		temp = n%10 ; 
		n/=10 ; 
		it = s.find(temp) ; 
		if(it == s.end())
		continue  ; 
		else
		{
			s.erase(it) ; 
			if(s.size() == 0)
			return 1 ; 
		}
	}
	if(s.size() == 0)
	return 1  ; 
return  0 ; 
}
int main()
{
long long i , j , k  , l , m, n ,t , ans , temp , x; 
infile() ; 
output() ; 
scanf("%lld",&t) ; 
int cas = 1 ; 
while(t--)
{
	scanf("%lld",&n) ; 
	for(i = 0; i <= 9 ; i++)
	s.insert(i) ; 
	if(n == 0)
	{
		printf("Case #%d: INSOMNIA\n",cas++)  ;
	}
	else
	{
		j = 2 ; 
		x =  n ; 
		while(1)
		{
			temp = func(x) ; 
			if(temp == 1)
			break ; 
			x  = n*j ; 
			j++ ; 
		}
		printf("Case #%d: %lld\n",cas++,x) ; 
	}
}
return 0 ;
}

