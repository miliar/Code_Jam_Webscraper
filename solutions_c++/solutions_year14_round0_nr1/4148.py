#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

int main(int argc, char *argv[])
{

	ifstream ip;
	ip.open(argv[1]);

	ofstream op;
	op.open("A-output.txt");

	int t;
	ip>>t;

	for(int iter=1; iter<=t; iter++)
	{
		op<<"Case #"<<iter<<": ";
		int a[4][4];

		int row;

		ip>>row;
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				ip>>a[i][j];
			}
		}
	
		vector<int> options;
		for(int i=0; i<4; i++)
			options.push_back(a[row-1][i]);
	


		ip>>row;
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				ip>>a[i][j];
			}
		}

		int hits=0;
		int remember = 0;
		for(int i=0;i<4;i++)
		{
			for(int j=0; j<4; j++)
			{
				if(a[row-1][j] == options[i])
				{
					remember = options[i];
					hits++;
				}
			}
		}

		if(hits==1)
		{
			op<<remember<<endl;
		}
		if(hits>1)
		{
			op<<"Bad magician!"<<endl;
		}
		if(hits<1)
		{
			op<<"Volunteer cheated!"<<endl;
		}
		options.clear();
	}

	return 0;
}
