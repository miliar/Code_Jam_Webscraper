#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

int main(void)
{

	ifstream inp;
	ofstream outp;
	inp.open("B-large.in");
	outp.open("output.txt");
	int i, n, j, k, N;
	double cost, costn, costnp1;
	double X, F, C, D;
	inp >> N;
	for (i = 1; i <= N; i++)
	{
		inp >> C;
		inp >> F;
		inp >> X;
		costn = X / 2;
		costnp1 = (C / 2) + X / (F + 2);
		n = 2;
		while (costn > costnp1)
//		for (k = 0; k < 10; k++)
		{
			cost = 0;
			D = 2;
			for ( j = 0; j < n; j++)
			{
				cost += C / D;
				D += F; 
			}
			cost += X / D;
			costn = costnp1;
			costnp1 = cost;
			n++;
//			cout << fixed << setprecision(7) << costn << '\t';
		}
		outp << "Case #" << i << ": " << fixed << setprecision(7) << costn << endl;
	}
	outp.close();
	inp.close();
	return 0;
}
