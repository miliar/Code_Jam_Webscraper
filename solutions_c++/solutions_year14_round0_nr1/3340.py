#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	ifstream fin("C://Users/dmx/Desktop/A-small-attempt1.in");
	ofstream fout("C://Users/dmx/Desktop/answer.txt");
	int t;
	fin>>t;
	int i1, i2, j1, j, s, n, answer;
	int ans[16];
	for(j1 = 0; j1<t; j1++)
	{
		n = 0;
		fin>>i1;
		for(j = 0; j < 16; j++)
		{
			fin>>ans[j];
		}
		fin>>i2;
		for(j = 0; j < 16; j++)
		{
			fin>>s;
			if(j>=(i2-1)*4 && j<i2*4)
			{
				int i = 0;
				for(i = 0; i < 4; i++)
				{
					if(s == ans[(i1-1) * 4 +i])
					{
						n++;
						answer = s;
					}
				}
			}
		}
		if (n == 0)
			fout<<"Case #"<<j1+1<<": Volunteer cheated!"<<endl;
		else
		{
			if(n > 1)
				fout<<"Case #"<<j1+1<<": Bad magician!"<<endl;
			else
				fout<<"Case #"<<j1+1<<": "<<answer<<endl;
		}
	}
	fout.close();
	fin.close();
	return 0;
}