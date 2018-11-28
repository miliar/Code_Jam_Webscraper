#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<set>
#include<fstream>
#include<queue>
#include<fstream>
#include<map>

using namespace std;


int main()
{
	ifstream cin("B-small-attempt0.in");
	ofstream cout("B-small.out");
	//ifstream cin("B-large.in");
//	ofstream cout("B-large.out");


	int arr[150][150];
	int T;
	cin>>T;
	for(int k=0;k<T;k++)
	{
		string ans;
		int n,m;
		cin>>n>>m;
		
		int ones=0;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				cin>>arr[i][j];
				if(arr[i][j]==1)
					ones++;
			}
		}


		for(int i=0;i<n;i++)
		{
			bool in=true;
			for(int j=0;j<m;j++)
			{
				if(arr[i][j]!=1)
				{
					in=false;
					break;
				}
			}
			if(in)
			{
				for(int j=0;j<m;j++)
				{
					arr[i][j]=0;
				}
				ones-=m;
			}
		}

		for(int i=0;i<m;i++)
		{
			bool in=true;
			int o=0;
			for(int j=0;j<n;j++)
			{

				if(arr[j][i]!=1 && arr[j][i]!=0)
				{
					in=false;
					break;
				}
				if(arr[j][i]==1)
					o++;
			}
			if(in)
			{

				ones-=o;
			}
		}

		if(ones==0)
			ans="YES";
		else ans="NO";


		cout<<"Case #"<<k+1<<": "<<ans<<endl;
	}

	//system("pause");
	return 0;
}