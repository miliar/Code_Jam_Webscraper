#include <iostream>
#include <fstream>
#include <iomanip> 

using namespace std;

int main(int argc, char *argv[])
{
    ifstream in(argv[1]);
    int n;

    in >> n;

    for (int i = 1; i <= n; i++) {
	double C, F, X;
	double r = 0;
	double prod = 2;
	in >> C >> F >> X;
//	cout << C << " " << F << " " << X << endl;

	double time1, time2;
	while(1) {
	    time1 = X / prod;
	    time2 = C / prod + X / (prod + F);
//	    cout << time1 << " " << time2 << " " << r << endl;
	    if (time1 > time2) {
		r += C / prod;
		prod += F;
	    }
	    else {
		r += time1;
		break;
	    }
	}

	cout << "Case #" << i << ": " << fixed << setprecision(7) << r << endl;
//	printf("Case #%d: %0.7f\n", i, r);
    }

    return 0;
}
