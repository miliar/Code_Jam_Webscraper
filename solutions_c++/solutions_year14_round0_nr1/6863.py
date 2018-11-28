#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>

using namespace std;

int main()
{
	ifstream inp("A-small-attempt0.in");
	ofstream out("output.out");
	int t;
	inp>>t;
	for(int caset=1;caset<=t;caset++)
	{
		vector<vector<int> > values1(5,vector<int>(5)),values2(5,vector<int>(5));
		int a1,a2;
		inp>>a1;
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
				inp>>values1[i][j];
		inp>>a2;
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
				inp>>values2[i][j];
		int ans=0,ans1; 
		vector<int> check1,check2;
		for(int i=1;i<=4;i++)
		{
			check1.push_back(values1[a1][i]);
			check2.push_back(values2[a2][i]);
		}
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(check1[i]==check2[j])
					ans++,ans1=check1[i];
			}
		}
		if(ans==0)
			out << "Case #" << caset << ": " << "Volunteer cheated!" << endl;
		else if(ans==1)
			out << "Case #" << caset << ": " << ans1 << endl;
		else
			out << "Case #" << caset << ": " << "Bad magician!" << endl;
	}
	return 0;
}