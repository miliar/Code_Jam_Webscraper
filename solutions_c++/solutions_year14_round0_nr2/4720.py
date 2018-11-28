#include <iostream>
#include <cmath>

using namespace std;

int T;
long double c, f, x;

int main()
{
    cin >> T;
    for (int k=1; k<=T; ++k) {
	cin >> c >> f >> x;

	long double last = 5000, n = 0, latter = 0;
	while (1) {
	    long double v = x / ( 2 + n * f);
	    if (n) {
		latter += c / ( 2 + (n-1) * f );
	    }
	    v += latter;
	    if (v >= last) break;

	    n += 1;
	    last = v;
	}

	printf("Case #%d: %.6Lf\n", k, last);
    }
    
    return 0;
}
