#include <string>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <fstream>
#include <sstream>
#include <iomanip>

using namespace std;

double cookieclicker(double C, double F, double X)
{
	double p_prime = F*(X-C)/C;
	if (p_prime<2)
		return X/2;
	int n = (p_prime-2)/F;

	double T = 0;
	for (int i = 0; i < n; ++i)
	{
		T += C/(2+i*F);
	}
	double t1 = X/(2+n*F);
	double t2 = C/(2+n*F)+X/(2+(n+1)*F);
	return T+min(t1,t2);
}

int main(int argc, char* argv[])
{
	ifstream in("B-small-attempt0.in");
	ofstream out("result.txt");
	int T;
	double C, F, X;
	in >> T;
	for (int i = 0; i < T; ++i)
	{
		in >> C >> F >> X;
		out << "Case #" << i+1 << ": " << fixed << setprecision(7) << cookieclicker(C,F,X) << endl;
	}

	in.close();
	out.close();
	return 0;
}