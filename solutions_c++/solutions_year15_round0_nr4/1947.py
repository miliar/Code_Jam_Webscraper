#include <iostream>
#include<fstream>
using namespace std;
int main()
{
	int x,r,c,t,co=0;
		ofstream fout;
	fout.open("output.txt");
	cin>>t;
	while(t--)
	{
		co++;
		cin>>x>>c>>r;

		if(x==1)
		{
			fout<<"Case #"<<co<<": "<<"GABRIEL\n";	

		}
		else 
		{
			if((r%x==0 && c>=(x-1)) || (c%x==0 && r>=(x-1)))
			{
				fout<<"Case #"<<co<<": "<<"GABRIEL\n";	
			}
			else
			{
				fout<<"Case #"<<co<<": "<<"RICHARD\n";
			}


		}
	}
	fout.close();
}
