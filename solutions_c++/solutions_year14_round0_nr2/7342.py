#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	int cs, csi;
	csi ^= csi;
	cin >> cs;
	while (csi++ < cs)
	{
		double C, F, X;
		double Tsum, Fnow;
		double Tnow, Tbuy, Tnext;
		cin >> C >> F >> X;
		Tsum = 0;
		Fnow = 2;
		Tnow = X / Fnow;
		while (1)
		{
			Tbuy = C / Fnow;
			Tnext = X / (Fnow + F);
			if ((Tnext + Tbuy) < Tnow)
			{
				Fnow += F;
				Tsum += Tbuy;
				Tnow = Tnext;
			}
			else
			{
				Tsum += Tnow;
				break;
			}
		}
		cout << "Case #" << csi << ": ";
		cout << setiosflags(ios::fixed) << setprecision(7) << Tsum << endl;
	}
	return 0;
}