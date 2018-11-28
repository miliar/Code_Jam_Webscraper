#include<iostream>  
#include<cstdio>  
#include<fstream> 
#include<iomanip>  
using namespace std;
#define N 5  
double c, f, x, s;
int judge()
{
	double temp = (c / s) + (x / (s + f));
	if (x / s > temp)
		return 1;
	else
		return 0;
}
int main()
{
	ofstream fout("hello.out");
	
	int k;
	cin >> k;
	string ans[N] = { "Case #", ": " };
	for (int time = 1; time <= k; time++)
	{
		s = 2.0;
		double tot = 0, tt = 0;
		cin >> c >> f >> x;
		while (judge())
		{
			tt += c / s;
			s += f;
		}
		tt += x / s;
		fout << "Case #" << time<<": " << setiosflags(ios::fixed) << setprecision(7) << tt << endl;
	//	printf("Case #%d: %.7lf\n", time, tt);
	}
	return 0;
}