#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

int main()
{
	ifstream f1("A-small-attempt2.in");
	ofstream f2("out.txt");
	int T;
	f1>>T;
	for(int tt=0;tt!=T;++tt)
	{
		f2<<"Case #"<<tt+1<<": ";
		int a1,a2;
		f1>>a1;
		int line1[4][4],line2[4][4];
		for(int i=0;i!=4;++i)
		{
			for(int j=0;j!=4;++j)
			{
				f1>>line1[i][j];
			}
		}
		f1>>a2;
		for(int i=0;i!=4;++i)
		{
			for(int j=0;j!=4;++j)
			{
				f1>>line2[i][j];
			}
		}
		int count=0;
		int ans;
		for(int i=0;i!=4;++i)
		{
			for(int j=0;j!=4;++j)
			{
				if(line1[a1-1][i]==line2[a2-1][j])
				{
					count++;
					ans=line1[a1-1][i];
				}
			}
		}
		if(count==1)
		{
			f2<<ans<<endl;
		}
		if(count>1)
		{
			f2<<"Bad magician!"<<endl;
		}
		if(count==0)
		{
			f2<<"Volunteer cheated!"<<endl;
		}
	}
	return 1;
}