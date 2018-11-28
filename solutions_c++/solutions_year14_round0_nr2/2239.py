#include<conio.h>
#include<iostream>
#include<fstream>
#include<iomanip>

using namespace std;

ifstream in("test.txt");
ofstream out("result.txt");

class Cookie{
	double c, f, x;

public:
	void getData()
	{
		in >> c;
		in >> f;
		in >> x;

	}
	void check(int & caseNo);
	
};

int main()
{
	static int T = 100;
	Cookie caseArr[100];
	int noc;
	in >> noc;
	int i;
	for (i = 0; i < noc; i++)
	{
		caseArr[i].getData();
	}
	for (i = 0; i < noc; i++)
	{
		caseArr[i].check(i);
	}

	return 0;
}

void Cookie::check(int &caseNo)
{
	double ttx, nttx, prev_time, nrate, rate = 2.000000,nprev_time, time=0;
	double xr, cr;
	
	while (1)
	{
		xr = x/rate;
		cr = c / rate;
		ttx = time+ xr;

		nrate = rate + f;
		nttx = x / nrate + time + cr;
		if (nttx < ttx)
		{
			time = time + cr;
			rate = nrate;
		}
		else{
			time = time + xr;
			break;
		}
	}
	out << "Case #" << caseNo + 1 << ": " <<fixed <<setprecision(7)<< time << endl;
}