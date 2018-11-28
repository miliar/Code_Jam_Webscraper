#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>
#include <set>
#include <fstream>
using namespace std;

typedef vector<int> VI;
typedef long long LL;

#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) __typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second
int main (int argc, char * const argv[]) {

	fstream wejscie;
	
	wejscie.open("A-small-practice.in",ios::in);
	if( wejscie.good() == true )
	{
		cout << "Uzyskano dostep do wejscia!" << std::endl;
	} else cout << "Dostep do pliku wejscia zostal zabroniony!" << endl;
	
	fstream wyjscie;
	wyjscie.open("odpowiedziii.txt", ios::out);
	if( wyjscie.good() == true )
	{
		cout << "Uzyskano dostep do wyjscia!" << std::endl;
	} else cout << "Dostep do pliku wyjscia zostal zabroniony!" << endl;
	int t;
	long double c,f,x;
	
	
	wejscie>>t;
	FOR(num_of_test_case,1,t){
		 double cookiesPerSec=2;//long
		 double time=0,resztaTime;
		wejscie>>c>>f>>x;
		 double minimum;
		minimum=x/cookiesPerSec;
		while (1) {
			//dodaje fabryke
			time+=c/cookiesPerSec;
			cookiesPerSec+=f;
			resztaTime=x/cookiesPerSec;
			//trzeba jakos odjac od x
			if(time+resztaTime<minimum) minimum=time+resztaTime;
				else break;
		}
		cout<<"Case #"<<num_of_test_case<<": ";
		//cout << minimum;
		printf("%.8lf",minimum);
		cout<<endl;
		//wyjscie<<"Case #"<<num_of_test_case<<": "<<minimum<<endl;
	}
    
	return 0;
}
