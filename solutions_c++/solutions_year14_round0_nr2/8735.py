#include <iostream>
#include <algorithm>
#include <iomanip>
#include <cmath>
#include <cstdio>

using namespace std;

int main(int argc, char const *argv[])
{
	int T=0;
	cin >> T;
	int count=1;
	const int epsilon = 1e-6;

	while ( count <= T){
		double c,f,x;
		cin >> c >> f >> x;
		//cout <<" c: " << c << " f: " << f << " x: " << x << endl;
		double cookiepresec=2;

		double result=0;

		while ( true){
			double timeatcurrentRate= x/cookiepresec;
			double timatNextrate = c/cookiepresec + x/(cookiepresec+f);

			if ( timatNextrate <timeatcurrentRate){
				result += c/cookiepresec;
				cookiepresec += f;
			}else{
				result += timeatcurrentRate;
				break;
			}
		}

		printf("Case #%d: %.7f\n",count, result) ;
		count++;
	}
	return 0;
}