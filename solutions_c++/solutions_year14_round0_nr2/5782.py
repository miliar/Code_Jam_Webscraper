#include <iostream>
#include <cmath>
#include <iomanip>
#include <cstring>
#include <algorithm>
#include <utility>
using namespace std;

#define EPS 1e-6

int main()
{
	int t, teste=1;
	double c, f, x, tempo_espera, atual=2;

	cin >> t;
	while(t-- > 0)
	{
		cin >> c >> f >> x;
		
		atual=2;
		tempo_espera=0;
		while( c/atual+x/(atual+f) < x/atual )
		{
			tempo_espera+=c/atual;
			atual+=f;
		}
		tempo_espera+=x/atual;
		cout << "Case #" << teste++ << ": " << std::fixed << std::setprecision(7) << tempo_espera << endl;
	}
	return 0;
}
