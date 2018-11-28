#include <fstream>
using namespace std;

#define  zero 0.00000000000
int main()
{
	fstream file_in,file_out;
	file_in.open("B-large.in",ios::in);
	file_out.open("output.txt",ios::out);
	file_out.setf(ios::fixed,ios::floatfield);
	file_out.precision(7);
	int T;
	file_in>>T;

	for (int case_num =0; case_num < T;case_num++)
	{
		file_out<<"Case #"<<case_num+1<<": ";
		double C,F,X;
		file_in>>C>>F>>X;

		float rate = 2.0;
		int buy = (X*F-C*rate)/(C*F);
		double time1=zero,time2=zero;
		if (buy <= zero)
		{
			time1 = X/rate;
			time2 = X/(rate+F)+C/rate;
		}
		else
		{
			
			
			for (int buy_num =0;buy_num < buy;buy_num++)
			{
				time1 += C/(rate+buy_num*F);
			}
			time1 += X/(rate + buy*F);

			for (int buy_num =0;buy_num< buy+1;buy_num++)
			{
				time2 += C/(rate+buy_num*F);
			}

			time2 += X/(rate + (buy+1)*F);
		}
	
		if (time1 - time2 >zero)
		{
			file_out<<time2<<endl;
		}
		else
		{
			file_out<<time1<<endl;
		}


	}

	return 0;
}