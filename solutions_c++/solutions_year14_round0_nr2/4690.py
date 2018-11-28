#include <fstream>
#include <ostream>
#include <iostream>
#include <iomanip>
bool resolver(std::ostream* out, double opt);
double caselogic(std::istream& istr);
void oput(std::ostream* out, double opt, int casenum)
{
	*out<<"Case #"<<casenum<<": ";
	if(!resolver(out,opt))
		std::cerr<<"error on case "<<casenum<<" opt value: "<<opt;
	*out<<'\n';
}
int main(int argc, char* argv[])
{
	bool ofe=false;
	char fname[]="test.txt";
	std::ostream* ostr=&std::cout;
	std::ifstream ifile;
	std::ofstream ofile;
	ifile=std::ifstream(fname,std::ios_base::in);
	if(argc==2||argc==3)
	{
		ofe=true;
		ofile=std::ofstream(argv[1],std::ios::out);
		ostr=&ofile;
	}
	if(argc==3)
	{
		ifile.close();
		ifile=std::ifstream(argv[2],std::ios::in);
	}
	std::istream& istr=ifile;
	int cases=0;
	int casenum=0;
	istr>>cases;
	if(cases>0)
	{	
		while(casenum<cases)
		{
			++casenum;
			oput(ostr,caselogic(istr),casenum);
		}
	}
	else
	{
		std::cerr<<cases<<" cases is less than 1\n";
	}
	if(ofe)
	{
		ofile.close();
	}
	ifile.close();
	return 0;
}
double step(double t, double C, double F, double X,double cookies);
double caselogic(std::istream& istr)
{
	double t=0;
	double C,F,X;
	istr>>C;
	istr>>F;
	istr>>X;
	if(C>X)
	{
		return X/2;
	}
	t=step(t,C,F,X,2);
	return t;
}
double step(double t, double C, double F, double X,double cookies)
{
	double tmp=(X-C)/cookies;
	t+=C/cookies;
	if(X/(cookies+F)<tmp)
	{
		return step(t,C,F,X,cookies+F);
	}
	return t+=tmp;
}
bool resolver(std::ostream* out, double opt)
{
	//varies by problem
	out->precision(7);
	*out<<std::fixed<<opt;
	if(out<0)
		return false;
	return true;
}