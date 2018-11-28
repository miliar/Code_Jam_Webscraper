#include <iostream>
#include <string>
#include <fstream>
#include <iomanip> 

using namespace std;

double c, f, x;

double farmtime(double r) {
	double t1, t2;
	double res = 0;
	/*
	t1 = x / r;
	t2 = c / r + x / (r + f);
	if (t1 <= t2)
		return t1;
	else
		return (c / r + farmtime(r + f));
		*/
	while (true) {
		t1 = x / r;
		t2 = c / r + x / (r + f);
		if (t1 <= t2) {
			res += t1;
			break;
		}
		else {
			res += c / r;
			r = r + f;
		}
	}

	return res;
}

int farm() {
	int t;
	ofstream fileoutput("output.txt");
	ifstream fileinput("input.txt");
	fileinput >> t;
	int count = 0;
	double res;

	while (count < t) {
		fileinput >> c >> f >> x;
		res = farmtime(2.0);
		count++;
		fileoutput << "Case #" << count << ": " << fixed << setprecision(7) << res << endl;
	}
	
	return 0;
}