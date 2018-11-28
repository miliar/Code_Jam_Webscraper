#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <math.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <deque>
#include <map>
#include <list>
#include <set>
#include <cstdlib>
using namespace std;

//Google Code Jam 2014 Qualification Round, Problem B code.google.com/codejam
//Disable warning messages C4996.
#pragma warning(disable:4996)

#define INPUT_FROM 0
#if INPUT_FROM
#define fromc from
#else
#define fromc cin
#endif

//long long fr(vector<long long>&, long long);

int main(int argc, char **argv)
{
	//ifstream from;
	const int nmin=1, nmax=1000, amax=100000;
	int test, cases, n, m, mt, res, rt, i, j, k, t, ax;
	int i0, i1, j0, j1;
	int k0, k1, k2;
	long long a, f, c, x, y;
	//char ch;
	//string sres[2]={"YES", "NO"};
	//string s, st, sr;
	long double dt, dt0, dt1;
	long double dc, df, dx, dy;


	//if(INPUT_FROM) from.open("test.txt");
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);

	//vector<int> vi;
	//deque<long long> dq;
	//vector<set< pair<int,int> > > vs0, vs1;
	//set< pair<int,int> >::iterator it;
	//map<int, int> mi;
	//typedef map<string, long long>::const_iterator CI;

	a = 200000LL;
	//scanf("%lld\n", &cases);
	fromc>>cases;
	for(int test=1;test<=cases;test++){
		//scanf("%lld\n", &n);
		fromc>>dc>>df>>dx;

		c = int(dc*amax);
		f = int(df*amax);
		x = int(dx*amax);

		//cout<<dc<<' '<<df<<' '<<dx<<endl;
		//printf("%.5Lf %.5Lf %.5Lf\n", dc, df, dx);
		//cout<<c<<' '<<f<<' '<<x<<endl;

		//a*t = x
		//(a+k*f)*t1 = x;
		//t0 = c*(1/a+1/(a+f)+...+1/(a+(k-1)*f))
		//t0 + t1 < t
		//k*c/a + x/(a+k*f) -> min_k
		//c/a = x*f/(a+k*f)^2
		//k = (sqrt(x*a*f/c)-a)/f;
		//k = (100*sqrt(x*20*f/c)-200000)/f;
		//c*(a+2*k*f)+c/a*(k*f)^2 = x*f


		//delta t0 = c/(a+k*f) < -delta t1 = -x*(1/(a+(k+1)*f) - 1/(a+k*f))
		//c/(a+k*f)<x*f/[(a+k*f)*(a+(k+1)*f)]
		//c*(a+(k+1)*f) < x*f

		//k = int((100.0*sqrt(x*20.0*f/c)-200000.0)/f);

		//cout<<x*f<<endl;
		//k=0;
		/*dt = 0.0; y = a; //dt0 = (0.0+x)/y;
		while(c*(y+f) <= x*f){
			//k++;
			//dt += (0.0+c)/y;
			dt += 1.0/(0.0+y);
			y+=f;
		}

		dt*=(0.0+c);

		dt += (0.0+x)/(0.0+y);*/

		dt = 0.0; dy = 2.0;
		while(dc*(dy+df) < dx*df){
			dt += 1.0/dy;
			dy+=df;
		}

		dt*=dc;

		dt += dx/dy;

		//if(dt0<dt) cout<<"error"<<endl;

		/*ax = 0;
		for(t=max(k-100,0);(t<k+100)&&(ax==0);++t){
			dt0 = (0.0+t*c)/a + (0.0+x)/(a+t*f);
			dt1 = (0.0+(t+1)*c)/a + (0.0+x)/(a+(t+1)*f);
			if(dt0<dt1){
				k0 = t-1;
				k1 = t;
				k2 = t+1;
				ax=1;

				dt = dt0;
			}
		}*/

		//cout<<k<<' '<<k0<<' '<<k1<<' '<<k2<<endl;
		//cout<<dt<<endl;

		//cout<<"Case #"<<test<<": "<<sres[1-ax]<<endl;
		printf("Case #%d: %.7Lf\n", test, dt);

		//cout<<"Case #"<<test<<": "<<sres[1-ax]<<endl;

	}

	return 0;
}
