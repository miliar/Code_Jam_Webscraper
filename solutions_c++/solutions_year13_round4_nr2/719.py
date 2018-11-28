#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <map>
#include <queue>
#include <ctime>
#include <cmath>

using namespace std;

#define FORN(I,N) for (int I=0; I<N; I++)
#define FORAB(I,A,B) for (int I=A; I<=B; I++)
#define FOREACH(I,A) for (__typeof__(A)::iterator I=A.begin(); I<A.end(); I++)
#define pb push_back
#define mp make_pair

#define INF (1073676287)

typedef long long int ll;

int main()
{
	int T;
	cin >> T;
	
	FORN (i, T)
	{
		int N;
		ll P;
		cin >> N >> P;
		
		ll n = 1;
		ll worst = 0;
		ll best = 0;
		FORN (j, N)
		{
			n *= (ll) 2;
		}
		
		n -= (ll) 1;
		
		ll a = 0;
		ll b = n;
		ll c = (a+b+1)/2;
		while (b!=a)
		{//cout << a << " " << b << " " << c << endl;
			ll t = 0;
			ll s = (c+1)/2;
			int ct = 0;
			while (s>0)
			{
				s /= 2;
				ct++;
			}
			FORN(j, ct)
			{
				t += ((ll)1)<<(N-1-j);
			}
			
			if (t<P)
			{
				a = c;
				c = (a+b+1)/(ll)2;
			}
			else
			{
				if (b==c)
					c--;
				b = c;
				c = (a+b+1)/(ll)2;
			}
		}
		worst = c;
		
		a = 0;
		b = n;
		c = (a+b+1)/2;
		while (a!=b)
		{
			ll t = 0;
			ll s = (n - c + 1)/2;
			int ct = 0; //cout << c << " " << s << endl;
			while (s>0)
			{
				s /= 2;
				ct++;
			}
			//cout << ct <<endl;
			FORN(j,ct)
			{
				t += ((ll)1)<<(N-1-j);
			}
			t = n - t;
			
			if (t<P)
			{
				a = c;
				c = (a+b+1)/(ll)2;
			}
			else
			{
				if (b==c)
					c--;
				b = c;
				c = (a+b+1)/(ll)2;
			}
		}
		best = c;
		
		cout << "Case #" << i+1 << ": " << worst << " " << best << endl;
	}
	
	return 0;
}