#include<iostream>
#include <string>
#include<fstream>
#include<ostream>
#include<vector>
#include<algorithm>
#include<set>
#include<deque>
#include<map>
#include<math.h>
using namespace std;

#define InputOutputToFile

int main(void)
{
#ifdef InputOutputToFile
	
	//cin redirection
	std::ifstream fin("cin.txt");
	std::streambuf *inbuf = std::cin.rdbuf(fin.rdbuf());

	//cout redirection
	std::streambuf* cout_sbuf = std::cout.rdbuf(); // save original sbuf 
	std::ofstream   fout("cout.txt"); 
	std::cout.rdbuf(fout.rdbuf()); // redirect 'cout' to a 'fout' 
	//std::cout.rdbuf(cout_sbuf); // restore the original stream buffer 

	//cout.txt file using c library
	FILE* fp=fopen("C:\\Programming_VS2010\\InterviewStreet\\InsertionSort\\cout.txt","w");
#endif

	int run = 0;
	cin>>run;
	int cs = 1;
	/*
	long double d =100.0000000;
	long double i=6.0000000;
	long double j=d/i;
	cout<<"j :: "<<j<<endl;
	printf("j :: %f\n",j);
	*/

	double c=0.0000000;
	double f=0.0000000;
	double x=0.0000000;
	double tt=0.0000000;
	double r=2.0000000;
	double tmp1=0.0000000;
	double tmp2=0.0000000;
	bool flag=true;

	bool itrFlg = false;
	while(run--)
	{
		if(itrFlg)
		{
			c=0.0000000;
			f=0.0000000;
			x=0.0000000;
			r=2.0000000;
			tt=0.0000000;
			tmp1=0.0000000;
			tmp2=0.0000000;
			flag=true;
			//cout<<endl;
			fprintf(fp,"\n");
		}
		itrFlg = true;
		
		cin>>c>>f>>x;

		if( c>x )
		{
			tt=x/r;
			flag=false;
		}
		
		while(flag)
		{
			tmp1=0.0000000;
			tmp2=0.0000000;

			tmp1=x/r;
			tmp2=(c/r)+(x/(r+f));

			if(tmp1>tmp2)
			{
				tt=tt+(c/r);
				r=r+f;
			}
			else
			{
				flag=false;
				tt=tt+tmp1;
			}

		}


		//cout<<"Case #"<<cs<<": "<<tt;

		fprintf(fp,"Case #%d: %.7f",cs,tt);
		cs++;
	}
	fflush(fp);
	fclose(fp);
	return 0;
}