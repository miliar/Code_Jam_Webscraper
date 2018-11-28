#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;
int main()
{
	ifstream fin("1.txt");
	ofstream fout("2.txt");
	int i,o,j,n,now,ans1,ans2,max;
	int t;
	fin >> t;
	int num[2000];
	for (o=0;o<t;o++)
	{
		fin >> n;
		for (i=0;i<n;i++)
		{
			fin >> num[i];
		}
		max=0;ans1=0;ans2=0;
		for (i=1;i<n;i++)
		{
			if (num[i-1]-num[i]>max) max=num[i-1]-num[i];
			if (num[i-1]-num[i]>0) ans1+=num[i-1]-num[i];
		}
		for (i=0;i<n-1;i++)
		{
			if (num[i]<max)
			{
				ans2+=num[i];
			}
			else
			{
				ans2+=max;
			}
		}
		fout << "Case #"<<o+1<<": " <<ans1<<" "<<ans2 <<  endl;
		cout << "Case #"<<o+1<<": " <<ans1<<" "<<ans2 <<  endl;
	}
	return 0 ;
}