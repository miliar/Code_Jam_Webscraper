#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <fstream>

using namespace std;
double eps = 1e-7;
int main()
{
	int t;
	//ifstream fin("B-small-attempt0.in");
	FILE *in, *out;
	in = fopen("B-large.in", "r");
	out = fopen("B-large.out", "w");
	//ifstream fin("in.txt");
	//fin >> t;
	fscanf(in, "%d\n", &t);
	//ofstream fout("B-small-attempt0.out");
	for (int test = 1; test <= t; test++) {
		double c, f, x;
		fscanf(in, "%lf %lf %lf\n", &c, &f, &x);
		//cin >> c >> f >> x;
		long double cookies = 0;
		long double produce = 2;
		long double time = 0;
		long double time_farm = 0; 
		long double limit = (x - c) * f / c;
		while (produce < limit - eps) {
			time_farm = c / produce;
			time += time_farm;
			produce += f;
		}
		time += x / produce;
		fprintf(out, "Case #%d: %.7f\n", test, time);
	//	fout << "Case #%" << test << ": " << time << endl;
	}
	//fout.close();
	return 0;
}
