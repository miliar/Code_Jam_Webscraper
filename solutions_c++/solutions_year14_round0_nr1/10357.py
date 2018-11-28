#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	fstream input("A-small-attempt0.in");
	ofstream output;
	output.open("A-small-attempt0.out",ios::out);
	int T;
	input>>T;
	for (int i=0;i<T;i++)
	{
		int a1,a2,c1[4][4],c2[4][4];
		input>>a1;
		for (int j=0;j<4;j++)
			for (int k=0;k<4;k++)
				input>>c1[j][k];
		input>>a2;
		for (int j=0;j<4;j++)
			for (int k=0;k<4;k++)
				input>>c2[j][k];
		int cnt=0,found=-1;
		for (int j=0;j<4;j++)
			for (int k=0;k<4;k++)
				if (c1[a1-1][j]==c2[a2-1][k])
				{
					cnt++;
					found=c1[a1-1][j];
				}
		if (cnt==0)
			output<<"Case #"<<i+1<<": "<<"Volunteer cheated!\n";
		else if (cnt == 1)
			output<<"Case #"<<i+1<<": "<<found<<"\n";
		else if (cnt>1)
			output<<"Case #"<<i+1<<": "<<"Bad magician!\n";
	}
	output.close();
	return 0;
}