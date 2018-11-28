#include<iostream>
#include<cstring>
#include<fstream>
#include<vector>
using namespace std;
int a[4][4],b[4][4],ans1,ans2;
int bit[17];
ifstream fin("in.txt");
ofstream fout("out.txt");
void solver(int no)
{
	memset(bit,0,sizeof(bit));
	fin>>ans1;
	for(int i=0;i<4;i++)
	  for(int j=0;j<4;j++)
		fin>> a[i][j];
	fin>>ans2;
	for(int i = 0 ;i < 4; i++)
		for(int j = 0 ;j < 4 ;j++)
			fin>> b[i][j];
	ans1--;ans2--;
	for(int j=0;j<4;j++)
		bit[a[ans1][j]]++;
	for(int j=0;j<4;j++)
		bit[b[ans2][j]]++;
	vector<int> ans;
	for(int i=1;i<=16;i++)
		if (bit[i]==2){
			ans.push_back(i);
		}
	if (ans.size()>1) fout<<"Case #"<<no<<": "<< "Bad magician!"<<endl;
		else if(ans.size()==0)
			fout<<"Case #"<<no<<": "<< "Volunteer cheated!"<<endl;
			else 
				fout<<"Case #"<<no<<": "<< ans[0]<<endl;
}
int main()
{
	int T;
	
	fin>>T;
	for(int i=1;i<=T;i++)
	{
		solver(i);
	}
	
	return 0;
}
