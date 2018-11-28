#include<iostream>
#include<cmath>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<bitset>
#include<map>
#include<utility>
#include<string>
#include<cstring>
#include<queue>
#include<sstream>

using namespace std ;

int main ()
{
	freopen ("test.txt","w",stdout);

	double c,f,x ,s , rate  ;
	int t , cnt =0 ;

	cin>>t;

	while(t--)
	{
		cnt ++ ;
		cin>>c>>f>>x;

		s =0 ;
		rate= 2.0;

		while(1)
		{
			if(s + x/rate < s + c/rate + x/(rate+f))
			{
				s += x/rate ;
				break ;
			}

			s+= c/rate ;
			rate += f;
		}

		printf("Case #%d: %.7f\n",cnt,s);
	}

	return 0;
}
