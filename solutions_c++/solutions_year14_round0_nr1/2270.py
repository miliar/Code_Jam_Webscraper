/* name of code*/
#include<iostream>
#include<cstring>
#include<iomanip>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<fstream>
#include<set>
#include<bitset>

#define lol long long
#define ull unsigned long long int

#define cin fin
#define cout fout

using namespace std;


int main()
{
	//ios_base::sync_with_stdio(false);
	ifstream fin;
	fin.open("A-small-attempt0.in");
	ofstream fout;
	fout.open("1.txt");
	int test_case;
	cin>>test_case;
	int x=1;
	while(test_case--)
	{
		int a[4][4];
		int first_row,second_row;
		int first_hash[17]={0};
		int second_hash[17]={0};
		cin>>first_row;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>a[i][j];
			}
		}
		for(int j=0;j<4;j++)
		first_hash[a[first_row-1][j]]=1;
		cin>>second_row;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>a[i][j];
			}
		}
		int count=0;
		int temp=0;
		for(int j=0;j<4;j++)
		{
			if(first_hash[a[second_row-1][j]]==1) count++;
			if(temp>0) continue; 
			if(count==1) temp=a[second_row-1][j];
		}
		cout<<"Case #"<<x<<": ";
		if(count==1) cout<<temp<<"\n";
		else if(count>1) cout<<"Bad magician!\n";
		else cout<<"Volunteer cheated!\n";
		x++;
	}
	return 0;
}
