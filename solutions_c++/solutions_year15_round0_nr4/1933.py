#include <iostream>
#include <fstream>
using namespace std;
ofstream fout;
int main()
{
	int t,x,r,c;

	fout.open("output3.txt");
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>x>>r>>c;
		if(x==1)
		{
			fout<<"Case #"<<i<<": "<<"GABRIEL\n";
		}
		else
		{
			if((r%x==0&&c>=(x-1))||(c%x==0&&r>=(x-1)))
			{
				fout<<"Case #"<<i<<": "<<"GABRIEL\n";
			}
			else
			{
				fout<<"Case #"<<i<<": "<<"RICHARD\n";
			}
		}

	}
}