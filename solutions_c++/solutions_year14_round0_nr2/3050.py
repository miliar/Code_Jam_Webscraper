#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;
int main()
{
	ifstream in_f;
	in_f.open("B-large.in",ios::in);
	ofstream out_f;
	out_f.open("B-large.out",ios::out);
	long long N;
	in_f>>N;
	long double C,F,X;
	for(long long CC=1;CC<=N;CC++)
	{
		in_f>>C>>F>>X;
		long double curr_prod=2,future_prod=2;
		long double time_reqX,time_waitedF,time_afterF;
		long double own=0;
		long double own0=0;
		long double sec=0;
		while(1)
		{
			if(own<X)
				time_reqX=(X-own)/curr_prod;
			else
				time_reqX=0;

			if(own<C)
				time_waitedF=(C-own)/curr_prod;
			else
			{
				time_waitedF=0;
				own-=C;
			}
			future_prod+=F;
			if(own<X)
			time_afterF=(X-own)/future_prod;
			else
			{
				time_afterF=0;
				own-=C;
			}

			if(time_reqX<=(time_waitedF+time_afterF))
			{
				sec+=time_reqX;
				own0=own0+time_reqX*curr_prod;
				own0-=X;
				own=own0;
				out_f<<"Case #"<<CC<<": "<<std::fixed<< std::setprecision(7)<<sec<<endl;
				break;
			}
			else
			{
				sec+=time_waitedF;
				own0=own0+time_waitedF*curr_prod;
				own0-=C;
				own=own0;
				curr_prod+=F;
			}
		}
	}
	return 0;
}