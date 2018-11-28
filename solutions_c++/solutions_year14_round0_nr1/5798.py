#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

int square1[4][4];
int square2[4][4];
int sel1[4];
int sel2[4];

int main()
{
		int test;
		cin>>test;
		int ct=0;
		int row1,row2;
		while(ct<test)
		{
				ct++;
				cin>>row1;
				for(int i=0;i<4;i++)
						for(int j=0;j<4;j++)
								cin>>square1[i][j];
				for(int i=0;i<4;i++)
						sel1[i]=square1[row1-1][i];

				cin>>row2;
				for(int i=0;i<4;i++)
						for(int j=0;j<4;j++)
								cin>>square2[i][j];
				for(int i=0;i<4;i++)
						sel2[i]=square2[row2-1][i];

				int match=0;
				int ans;
				for(int i=0;i<4;i++)
				{
						for(int j=0;j<4;j++)
						{
								if(sel1[i]==sel2[j])
								{
										match++;
										ans=sel1[i];
								}

						}
				}

				cout<<"Case #"<<ct<<": ";
				if(match==1)cout<<ans<<endl;
				else if(match==0)
						cout<<"Volunteer cheated!\n";
				else cout<<"Bad magician!\n";

		}
		return 0;
}





