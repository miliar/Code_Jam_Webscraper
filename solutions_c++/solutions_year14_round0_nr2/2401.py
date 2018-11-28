#include <iostream>
using namespace std;
//#define LATTE
bool cmp(double x,double f,double s,double w)
{
	if ((w / s) > (x/s+w / (f + s)))
	{
		return true;
	}
	else
		return false;
}

void main()
{
#ifdef LATTE
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("out.out", "w", stdout);
#endif // LATTE
	int t;
	cin >> t; int t1=0;
	while (t--)
	{
		double timetotal=0.0;
		double x, f, s, w;
		s = 2.0;
		cin >> x >> f >> w;
		while (cmp(x,f,s,w))
		{
			timetotal += x / s;
			s += f;
		}
		timetotal += w / s;
		t1++;
		cout.setf(ios::fixed);
		cout.precision(7);
		cout << "Case #"<<t1<<": "<<timetotal << endl;
	}
}
//
//#include<iostream>
//#include<cstdio>
//#include<fstream>
//using namespace std;
//#define N 5
//double c, f, x, s;
//int judge()
//{
//	double temp = (c / s) + (x / (s + f));
//	if (x / s > temp)
//		return 1;
//	else
//		return 0;
//}
//int main()
//{
//	freopen("B-small-attempt0.in", "r", stdin);
//	freopen("B-large.out","w",stdout);
//	int k;
//	cin >> k;
//	string ans[N] = { "Case #", ": " };
//	for (int time = 1; time <= k; time++)
//	{
//		s = 2.0;
//		double tot = 0, tt = 0;
//		cin >> c >> f >> x;
//		while (judge())
//		{
//			tt += c / s;
//			s += f;
//		}
//		tt += x / s;
//		printf("Case #%d: %.7lf\n", time, tt);
//	}
//	return 0;
//}
