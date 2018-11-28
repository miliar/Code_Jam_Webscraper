#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;
int main()
{
	string s1 = "7";
	string s2 = "Bad magician!";
	string s3 = "Volunteer cheated!";
	int p1[4][4];
	int p2[4][4];
	int t;
	int a,b;
	cin>>t;
	for(int x=1;x<=t;x++)
	{
		cin>>a;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>p1[i][j];
		cin>>b;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>p2[i][j];
		sort(p1[a-1],p1[a-1]+4);
		sort(p2[b-1],p2[b-1]+4);
		int i=0,j=0;
		vector<int> v;
		while(i<4 && j<4)
		{
			//cout<<"a="<<a<<",b="<<b<<endl;
			if(p1[a-1][i] < p2[b-1][j])
			{
				i++;
				continue;
			}
			if(p1[a-1][i] > p2[b-1][j])
			{
				j++;
				continue;
			}
			if(p1[a-1][i] == p2[b-1][j])
			{
				//cout<<"i="<<i<<",j="<<j<<endl;
				v.push_back(p1[a-1][i]);
				i++, j++;
			}
		}
		printf("Case #%d: ",x);
		if(v.size() == 0)
			cout<<s3<<endl;
		if(v.size() == 1)
			cout<<v[0]<<endl;
		if(v.size() > 1)
			cout<<s2<<endl;
	}
}