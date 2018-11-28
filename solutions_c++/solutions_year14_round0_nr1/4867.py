#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>

using namespace std;


int main()
{
	ifstream fin("magictrick.in");
	int T;
	fin>>T;

	ofstream fout("magictrick.out");
	for(int i=0;i<T;i++)
	{
		fout<<"Case #"<<(i+1)<<": ";
		int r1,r2;
		vector<bool> a1(16,false);
		vector<bool> a2(16,false);
		fin>>r1;
		for(int k=0;k<16;k++)
		{
			int inp;
			fin>>inp;
			a1[inp-1] = (r1-1)*4<=k && k<r1*4;
		}
		fin>>r2;
		for(int k=0;k<16;k++)
		{
			int inp;
			fin>>inp;
			a2[inp-1] = (r2-1)*4<=k && k<r2*4;
		}

		int cnt = 0;
		int idx = -1;
		for(int k=0;k<16;k++)
		{
			if(a1[k] && a2[k])
			{
				cnt++;
				idx = k+1;
			}
		}

		switch(cnt)
		{
			case 0:
				fout<<"Volunteer cheated!"<<endl;
				break;
			case 1:
				fout<<idx<<endl;
				break;
			default:
				fout<<"Bad magician!"<<endl;
				break;
		}

/*		cout<<endl;
		for(int k=0;k<16;k++)
			cout<<a1[k];
		cout<<endl;
		cout<<endl;
		for(int k=0;k<16;k++)
			cout<<a2[k];
		cout<<endl;
*/	}

	return 0;
}
