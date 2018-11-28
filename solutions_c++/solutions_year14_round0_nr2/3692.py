#include<iostream>
#include<iomanip>
#include<cstdio>

using namespace std;

double t[100001];
double cps[100001];

int main()
{
	int nCase;
	double c, f, x;
	double min;
	double ct;
	int l = 100000;

	cout << setprecision(7) << fixed;
	cin >> nCase;
	for (int z = 1; z <= nCase; ++z)
	{
		cin >> c >> f >> x;
		//scanf("%lf%lf%lf",&c,&f,&x);
		t[0] = 0;
		cps[0] = 2;
		for (int i = 1; i <= l; ++i)
		{
			cps[i] = 2 + f*i;
			t[i] = t[i-1] + c/(double) cps[i-1];
		}
		
		min = x / 2;
		for (int i = 1; i <= l; ++i)
		{
			ct = t[i] + x/cps[i];
			if (ct < min)
				min = ct;
		}
		cout << "Case #" << z << ": " << min << endl;
	}
	return 0;
}