#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <vector>

#define forn(i,n) for(int i = 0; i < (n); i++)
#define forsn(i,s,n) for(int i = (s); i < (n); i++)
#define pb push_back
#define x first
#define y second

using namespace std;

typedef long long int tint;

int main()
{
	int test;
	double r,t;
	tint res;
	double aux;

	cin >> test;
	forn(caso,test){
		cin >> r >> t;
		/*tint sup = (tint) sqrt(t);
		sup++;
		inf = 0;
		while((sup - inf) >= 1)
		{
			med = (sup + inf) / 2;
			
			aux = PI * ( (med+1) * (2*r+1+med) );
		
			cout << aux << " " << med << endl;

			if(aux > t){
				sup = med;
			}
			else{
				inf = med;
			}
		}

		if(sup == inf){
			res = sup;
		}
		else{
			aux = ( (inf+1) * (2*r+1+inf) );
			if(aux > t) res = inf;
			else res = sup;
		}*/
		double lim = sqrt((2*r+3)*(2*r+3) - 16*r - 8 + 8*t) - (2*r + 3);
		lim = lim / (4 + 0.0);
		res = (tint) lim;
		res++;
		if( (res + 2)*(2*r + 1+ 2*(res+1)) <= t ) res++;
		if( res * (2*r + 2*res - 1) > t ) res--;
		cout << "Case #" << (caso+1) << ": " << res << endl;
	}
	return 0;
}
