#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
	ofstream output;
	ifstream input;

	input.open("input.in");
	output.open("Out.txt");
	//output.clear();


	int T;
	int y=0;
	bool flag=0;
	int num;
	input>>T;
	for(int t=1; t<=T; t++)
	{
		int n1=0;

		input>>n1;
		int S1[4][4];
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				input>>S1[i][j];
			}
        int n2=0;
		input>>n2;
		int S2[4][4];
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				input>>S2[i][j];
					
			}
			for(int i=0;i<4;i++)
			{
				for(int j=0;j<4;j++)
					if(S1[n1-1][i]==S2[n2-1][j])
						if(flag!=1)
						{
							y=1;
							flag=1;
							num=S1[n1-1][i];
						}
						else
						{
							y=2;
						}
			}
            if(flag!=1)
				y=3;
			if(y==1)
			output<<"Case #"<<t<<": "<<num<<endl;
			if(y==2)
				output<<"Case #"<<t<<": "<<"Bad magician!"<<endl;
			if(y==3)
				output<<"Case #"<<t<<": "<<"Volunteer cheated!"<<endl;
			flag=0;
			y=0;
			num=0;
	}
	//char t;
	//cin>>t;
	output.close();
	input.close();
	return 0;
}

