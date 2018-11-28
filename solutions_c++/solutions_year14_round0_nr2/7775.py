#include<iostream>
#include<fstream>
#include<iomanip>

using namespace std;

int main()
{
	ifstream in("B-large.in");
	cin.rdbuf(in.rdbuf());

	ofstream out("out.txt");
	cout.rdbuf(out.rdbuf());

	int T;
	double C,F,X;


	cin>>T;
	for(int t =0;t<T;t++)
	{
		cin>>C>>F>>X;
		int Len = (X/C)+1;
			
		double resultMin = -1.0;
		for(int i = 0;i<=Len;i++)
		{
			double base = 2.0;
			double power = base;
			double result = 0.0;
			for(int a = 0;a < i;a++)
			{
				result += C/power;
				power += F;
			}
			result += X/power;

			if(result < resultMin || resultMin == -1.0)
			{
				resultMin = result;
			}

		}

		cout<<fixed<<setprecision(7)<<"Case #"<<t+1<<": "<<resultMin<<endl;
	}



	return 0;
}