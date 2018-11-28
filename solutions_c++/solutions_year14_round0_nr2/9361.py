#include <iostream>
#include <fstream>

using namespace std;

double c,f,x;

double calc(double curt,double gain)
{
    cout << fixed;
    cout.precision(7);
    double time;
	if(x/gain > x/(gain+f) + c/gain) {
        time = curt + c/gain;
		return calc(time,gain+f);
	} else {
	    time = curt + x/gain;
		return time;
	}
}

int main()
{
	int t;
	ofstream out;

    out.open("output.txt",ios::out);

	cin >> t;
	for(int i=1; i<=t; i++) {
		cin >> c >> f >> x;
		out << fixed;
		out.precision(7);
		out << "Case #" << i << ": " << calc(0.000000,2.000000) << endl;
	}

	return 0;
}