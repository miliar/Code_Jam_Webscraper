#include <cstdlib>
#include <iostream>
#include <stdint.h>
#include <cmath>

using namespace std;
// Yeah: totally fucked this one up. :/

#define forl(i,a,b) for(int i = a; i < b; ++i)

/*
 * pi * (r+R)^2 - pi * (r)^2
 * = pi * (r+R)(r+R) - (r)(r)
 * = pi * (r^2 + 2Rr + R^2 - r^2)
 * = pi * 2Rr + R^2
 *
 * So: to draw a black circle of radius "r" cm, we need 2r+1 ml of paint
 *
 * We need to draw y black circles, each with radius R+2i cm, i = 0..n
 * So paint needed t = 2(R+2i)+1 ml, i=0..n
 * = 2(Rn + n*(n+1))+n ml
 * = n(2R + 2(n+1) + 1) ml
 * = n^2 + n(2R + 2 + 1) ml
 * t - n^2 = n(2R + 2 + 1)
 * (t - n^2)/(2R + 2 + 1) = n
 * t/(2R+2+1) = n - n^2/(2R+2+1)
 * t/n(2R+2+1) = 1 - n(2R+2+1)
 * t
 * n^2 = t - n(2R + 2 + 1)
 * n = 2R + 2 + 1?
 */

/*#define SIZE 808080

uint64_t bigasscache[SIZE];

uint64_t areabit(uint64_t n)
{
	if (n > SIZE-1)
	{
		uint64_t acc = areabit(SIZE-1);
		for (uint64_t i = SIZE-1; i <= n; ++i)
		{
			acc += 2*(2*i);
		}
		return acc;
	}
			
	if (bigasscacheidx < n)
	{
		for (uint64_t i = bigasscacheidx+1; i <= n; ++i)
		{
			bigasscache[i] = bigasscache[i-1] + 2*(2*i);
		}
	}
	return bigasscache[n];
}
*/
//uint64_t

int main()
{
	int numCases;
	cin >> numCases;
	forl(i,1,numCases+1)
	{
		uint64_t r, t;
		cin >> r >> t;
		uint64_t r_squared = r*r;
		//uint64_t ans = /* floor */ ( t / (2*R+2+1 );
		uint64_t ans = 0;
		while (true)
		{

			uint64_t area = 2*(2*ans) +2*(r)+1;
//			cerr << "area (" << ans << ") = " << area << endl;
			if (area > t) break;
			t -= area;
			++ans;
		}
		cout << "Case #" << i << ": " << ans << endl;
	}
}
