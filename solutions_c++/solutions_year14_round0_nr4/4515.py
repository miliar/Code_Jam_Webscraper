#include <fstream>
#include <ostream>
#include <iostream>
bool resolver(std::ostream* out, int a, int b);
int caselogic(std::istream& istr, int &a, int &b);
void oput(std::ostream* out, int a,int b, int casenum)
{
	*out<<"Case #"<<casenum<<": ";
	if(!resolver(out, a, b))
		std::cerr<<"error on case "<<casenum;
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
	int a, b;
	istr>>cases;
	if(cases>0)
	{	
		while(casenum<cases)
		{
			++casenum;caselogic(istr,a,b);
			oput(ostr,a,b,casenum);
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
int cmp(const void *a, const void *b)
{
	int out;
	double x=*(double*)a;
	double y=*(double*)b;
	if(x<y)
		out=-1;
	else if(x==y)
		out= 0;
	else
		out= 1;
	//std::cout<<out;
	return out;
}
int caselogic(std::istream& istr, int &a, int &b)
{
	int blocks;
	double *p1;
	double *p2;
	istr>>blocks;
	a=0;b=0;
	p1=new double[blocks];
	p2=new double[blocks];
	for(int i=0;i<blocks;++i)
	{
		istr>>p1[i];
	}
	for(int i=0;i<blocks;++i)
	{
		istr>>p2[i];
	}
	std::qsort(p1,blocks,sizeof(double),cmp);
	//std::cout<<'\n';
	std::qsort(p2,blocks,sizeof(double),cmp);
	//std::cout<<'\n';
	/*
	for(int i=0;i<blocks;++i)
		std::cout<<p1[i]<<' ';
	std::cout<<'\n';
	for(int i=0;i<blocks;++i)
		std::cout<<p2[i]<<' ';
	std::cout<<'\n';
	//*/

	int tmp=0;
	int tmp2=blocks-1;
	for(int i=blocks-1;i>-1;--i)
	{
		if(p1[i]>p2[tmp2])
		{
			++tmp;

		}
		else
		{
			--tmp2;
		}
	}
	b=tmp;
	tmp=0;
	for(int i=0;i<blocks;++i)
	{
		if(p1[i]<p2[tmp])
		{
			
		}
		else
		{
			++tmp;

		}
	}
	a=tmp;
	delete[] p1;
	delete[] p2;
	return 0;
}
bool resolver(std::ostream* out, int a, int b)
{
	//varies by problem
	if(a<0||b<0)
		return false;
	
	*out<<a<<' '<<b;
	return true;

}