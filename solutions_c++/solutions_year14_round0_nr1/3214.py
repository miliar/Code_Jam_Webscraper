#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	int t,ans1,ans2,arr1[4][4],arr2[4][4],answer=0,temp;
	ifstream fin("a1.in");
	ofstream fout("a_small.out");
	//those two lines
	fin>>t;
	for(int cas=0;cas<t;cas++)
	{
		fin>>ans1;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				fin>>arr1[i][j];
			}
		}
		fin>>ans2;
		for(int k=0;k<4;k++)
		{
			for(int l=0;l<4;l++)
			{
				fin>>arr2[k][l];
			}
		}
		
		for(int n=0;n<4;n++)
		{
			for(int m=0;m<4;m++)
			{
				if(arr1[ans1-1][n]==arr2[ans2-1][m])
				{
					answer++;
					temp=arr1[ans1-1][n];
				}
				if(answer>1)
				{
					break;
				}
			}
		}
		if(answer>1)
		{
		
			fout<<"Case #"<<cas+1<<": "<<"Bad magician!"<<endl;
		}
		else if(answer==1)
		{
			fout<<"Case #"<<cas+1<<": "<<temp<<endl;
			
		}
		else
		{
			fout<<"Case #"<<cas+1<<": "<<"Volunteer cheated!"<<endl;
		}
		answer=0;
					
		
			}
	return 0;
}

	

