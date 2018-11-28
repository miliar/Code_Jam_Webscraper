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
#include <sstream>

#define forn(i,n) for(int i = 0; i < (n); i++)
#define forsn(i,s,n) for(int i = (s); i < (n); i++)
#define pb push_back
#define x first
#define y second


using namespace std;

typedef long long int tint;


bool palind(tint n)
{
	stringstream s;
	s << n;
	string aux, auxx;
	aux = s.str();
	tint m = aux.size();
	auxx = aux;
	forn(i,m / 2){
		auxx[i] = aux[m-1-i];
		auxx[m-1-i] = aux[i];
	}
	return(auxx == aux);
}

int main()
{
	bool fairsquare[1100] = {false};
	for(tint i = 1; i < 32; i++){
		if(palind(i) and palind(i*i) and (i*i <= 1000) ){ fairsquare[i*i] = true; }
	}
	int t;
	tint a,b,l,h;
	int res;
	cin >> t;
	forn(caso,t){
		cin >> a >> b;
		res = 0;
		l = (tint) sqrt(a);
		h = (tint) sqrt(b);
		if(l*l < a) l++;
		h++;
		forsn(i,a,b+1) if(fairsquare[i]) {res++;}
		/*for(tint i = l; i < h; i++){
			if((i*i >= a) and (i*i < b) and fairsquare[i*i]) res++;
		}*/
		cout << "Case #" << (caso+1) << ": " << res << endl;
	}
	return 0;
}
