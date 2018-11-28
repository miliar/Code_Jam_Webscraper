#include<fstream>
using namespace std;
int main()
{
	ifstream fin("A-small-attempt2.in");
	ofstream fout("A-small-attempt0.out");
	int t,ans1,ans2,ans3;
	int a[4][4],b[4][4];
	fin>>t;
	int tt=t;
	while (t)
	{
		int ans=0;
		fin>>ans1;
		int i,j;
		for (i=0;i<4;i++)
		for (j=0;j<4;j++)
		fin>>a[i][j];
		fin>>ans2;
		for (i=0;i<4;i++)
		for (j=0;j<4;j++)
		fin>>b[i][j];
		for (i=0;i<4;i++)
		for (j=0;j<4;j++)
		if (a[ans1-1][i]==b[ans2-1][j]){ans++;ans3=b[ans2-1][j];}
	   if (ans==1)
		{
			fout<<"Case #"<<tt-t+1<<": "<<ans3<<endl;
		}
		if (ans>1)
		{
			fout<<"Case #"<<tt-t+1<<": "<<"Bad magician!"<<endl;
		}
		if (ans==0)
		{
			fout<<"Case #"<<tt-t+1<<": "<<"Volunteer cheated!"<<endl;
		}
		t--;
		ans=0;
		
	}
	fin.close();
	fout.close();
	return 0;
}
