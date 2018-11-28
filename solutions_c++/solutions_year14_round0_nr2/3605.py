#include <iostream>
#include <iomanip>
using namespace std;

double solve(double c, double f, double x)
{
    double cps = 2;
    double time = 0;

    if (x < c) return x/cps;
    while (1) {
        time+=c/cps;
        x-=c;
        if ((x/cps) < ((x+c)/(cps+f))) {
            time += x/cps; break;
        } else {
            x+=c;
            cps+=f;
        }
    }
    return time;
}

int main()
{
	int T;
	int case_;
	cin >> T;
	for (case_=1; case_<=T; ++case_) {
		double c,f,x;
		cin>>c; cin>>f; cin>>x;
		cout << setprecision(8) << "Case #" << case_ << ": " << solve(c,f,x) << endl;
	}
	return 0;
}
