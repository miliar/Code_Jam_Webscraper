#include <fstream>
#include <ostream>
#include <iostream>
bool resolver(std::ostream* out, int opt);
int caselogic(std::istream& istr);
void oput(std::ostream* out, int opt, int casenum)
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
int caselogic(std::istream& istr)
{
	int a[4],b[4];
	int c=0;
	int choice;
	int tmp;
	istr>>choice;
	for(int i=0;i<choice;++i)
	{
		for(int j=0;j<4;++j)
		{
			istr>>a[j];
		}
	}
	for(int i=choice;i<4;++i)
	{
		for(int j=0;j<4;++j)
		{
			istr>>tmp;
		}
	}
	istr>>choice;
	for(int i=0;i<choice;++i)
	{
		for(int j=0;j<4;++j)
		{
			istr>>b[j];
		}
	}
	for(int i=choice;i<4;++i)
	{
		for(int j=0;j<4;++j)
		{
			istr>>tmp;
		}
	}
	for(int i=0;i<4;++i)
	{
		for(int j=0;j<4;++j)
		{
			if(a[i]==b[j])
			{
				if(c!=0)
				{
					return -1;
				}
				c=a[i];
			}
		}
	}
	return c;
}
bool resolver(std::ostream* out, int opt)
{
	//varies by problem
	if(opt==0)
	{
		*out<<"Volunteer cheated!";
		return true;
	}
	if(opt==-1)
	{
		*out<<"Bad magician!";
		return true;
	}
	if(opt>0&&opt<17)
	{
		*out<<opt;
		return true;
	}

	return false;

}