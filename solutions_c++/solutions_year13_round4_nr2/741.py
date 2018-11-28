#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <deque>
#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

/* DEFINITION */
#define REP(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define REPab(i,a,b) for (int (i)=a; (i) <= (int) b; (i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

#define DEBUG(X) cout << '>' << #X << ':' << X << endl

#define MX(A,B) (A)>(B)?(A):(B)
#define MN(A,B) (A)>(B)?(B):(A)

#define INF (1<<29)
#define max_comb 200

/* TYPEDEF */
typedef long long int ll;
typedef unsigned long long int ull;
typedef double dd;
typedef unsigned int uint;
typedef unsigned char uchar;

int main()
{
	int T;
	cin >> T;
	
	REPab (t,1,T)
	{
		int N;
		ll P;
		cin >> N >> P;
		
		ll n = 1;
		ll worst = 0;
		ll best = 0;
		
		REP (j, N)
		{
			n =n* (ll) 2;
		}
		
		n -= (ll) 1;
		
		ll a = 0;
		ll b = n;
		ll c = (a+b+1)/2;
		while (b!=a)
		{
			ll t = 0;
			ll s = (c+1)/2;
			int ct = 0;
			while (s>0)
			{
				s /= 2;
				ct++;
			}
			REP(j, ct)
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
		int max = 0;
		a = 0;
		b = n;
		c = (a+b+1)/2;
		while (a!=b)
		{
			ll temp = 0;
			ll s = (n - c + 1)/2;
			int ct = 0; //cout << c << " " << s << endl;
			while (s>0)
			{
				s /= 2;
				ct++;
			}
			//cout << ct <<endl;
			REP(i,ct)
				temp += ((ll)1)<<(N-1-i);
			
			temp = n - temp;
			
			if (temp<P)
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
		
		cout << "Case #" << t << ": " << worst << " " << best << endl;
	}
	
	return 0;
}