# include "iostream"
# include "fstream"
# include "iomanip"
using namespace std;

void main()
{
	ifstream inf("B-large.in", ios::in);
	ofstream outf("B-large.out", ios::out);
	int test = 0;
	double multiplier = 2;
	double c = 0, f=0, x=0;
	double time = 0, time1 = 0, time2 = 0, time3 = 0;
	bool flag = false;

	inf>>test;

	for(int i= 0; i<test; i++)
	{
		inf>>c;
		inf>>f;
		inf>>x;

		flag = false;
		multiplier = 2;
		time = 0, time1 = 0, time2 = 0, time3 = 0;	

		time1 = x/multiplier;

		while (!flag)
		{
			time2 += c/multiplier;
			time3 = time2;
			multiplier += f; 
			time2+= x/multiplier;

			if(time2 > time1)
			{
				time = time1;
				break;
			}

			time1=time2;
			time2 = time3;
		}

		outf<<"Case #"<<i+1<<": "<<fixed<<setprecision(7)<<time<<endl;
	}

	

}