#include <iostream>
#include <string>
#include<math.h>
#include<iomanip>
#include<vector>
#include<set>
#include<algorithm>
using namespace std;
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	int r1,r2;
	int temp;
	vector<int>v1,v2,v3;
	cin>>t;

	for(int i=0;i<t;i++)
	{
		cin>>r1;
		r1--;
		for(int j=0;j<16;j++)
		{
			cin>>temp;
			if(j>=(r1*4) && j< ((r1+1)*4))
				v1.push_back(temp);
		}

		cin>>r2;
		r2--;
		for(int j=0;j<16;j++)
		{
			cin>>temp;
			if(j>=(r2*4) && j< ((r2+1)*4))
				v2.push_back(temp);
		}
		
		for(int j=0;j<v1.size();j++)
		{
			if(std::find(v2.begin(), v2.end(), v1[j]) != v2.end())
			{
				v3.push_back(v1[j]);
			}
		}
		
		cout<<"Case #"<<i+1<<": ";
		if(v3.size()==1)
			cout<<v3[0];
		else if(v3.size()>1)
			cout<<"Bad magician!";
		else
			cout<<"Volunteer cheated!";

		cout<<endl;
		v1.clear();
		v2.clear();
		v3.clear();
	}
	return 0;
}
