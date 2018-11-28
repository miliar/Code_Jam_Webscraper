#include<iostream>
#include<stdio.h> 
#include<stdlib.h>
#include<fstream>
#include<set>
using namespace std;
ifstream fin("A-small-attempt1.in");
ofstream fout("A-small-attempt1.out");
int main()
{
	int n,t[4],card[4][4],r,count,ans;
	int choose[4];
	//set<int> guess;
	fin>>n;
	for(int k=0;k<n;k++) {
	//	guess.clear();
		fin>>r;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				fin>>card[i][j];
				if(i==r-1) 
				{
					t[j] = card[i][j];
				//	cout<<card[i][j]<<endl;
				}
			//	cout<<card[i][j]<<" ";
			}
	//		cout<<endl;
		}
		count = 0;
		fin>>r;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				fin>>card[i][j];
				if(i==r-1)
				{
					for(int k=0;k<4;k++)
					{
						if(card[i][j] == t[k])
						{
					//		cout<<t[k]<<" ";
							count++;
							ans = card[i][j];
							break;
						}
					}
				}
			}
		}
	//	cout<<endl;
		if(count==0) fout<<"Case #"<<k+1<<": "<<"Volunteer cheated!"<<endl;
		if(count==1) fout<<"Case #"<<k+1<<": "<<ans<<endl;
		if(count>1) fout<<"Case #"<<k+1<<": "<<"Bad magician!"<<endl;
	}
}
