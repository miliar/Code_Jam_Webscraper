#include<iostream>
#include<fstream>

using namespace std;

void main()
{
	ifstream fin;
	ofstream fout;
	int n=1,no;
	int a,b,k,i,j;
	unsigned long int sol;
	fin.open("B.in",ios::in);
	fout.open("out.txt",ios::out);
	fin>>no;

	while(n<=no)
	{
		fin>>a>>b>>k;
		
		sol=0;
		
		for(i=0;i<a;i++)
		{
			for(j=0;j<b;j++)
			{
				if((i&j)<k)
					sol++;
			}
		}
		fout<<"Case #"<<n<<": "<<sol<<endl;
		n++;
	}

	fin.close();
	fout.close();
}
