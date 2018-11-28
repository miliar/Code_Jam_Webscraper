#include<fstream>
using namespace std;

int main()
{
	ifstream fin("inp.in");
	ofstream fout("out.txt");
	int t,k,x,r,c,prod;
	fin>>t;
	for(k=1;k<=t;k++)
	{
		fin>>x>>r>>c;
		fout<<"Case #"<<k<<": ";
		prod=r*c;
		if(prod%x !=0)
			fout<<"RICHARD\n";
		else
		{
			if(x==1 || x==2)
				fout<<"GABRIEL\n";
			else if(x==3)
			{
				if(prod==3)
					fout<<"RICHARD\n";
				else
					fout<<"GABRIEL\n";
			}
			else
			{
				if(prod==4 || prod==8)
					fout<<"RICHARD\n";
				else
					fout<<"GABRIEL\n";
			}
		}
	}
}