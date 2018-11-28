#include<iostream>
#include<vector>

using namespace std;

int main()
{
	vector<int> c;
	int ans1,ans2,ar1[4][4],ar2[4][4],a[16];
	int T;
	cin>>T;
	
	for(int i=0;i<T;i++)
	{
		c.clear();
		cin>>ans1;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				cin>>ar1[j][k];
		
		cin>>ans2;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				cin>>ar2[j][k];
				
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(ar1[ans1-1][j]==ar2[ans2-1][k])
					c.push_back(ar2[ans2-1][k]);
					
			}
		}
		
		if(c.size()==0)
			cout<<"Case #"<<i+1<<": Volunteer cheated!\n";
		else if(c.size()==1)
			cout<<"Case #"<<i+1<<": "<<c[0]<<endl;
		else if(c.size()>1)
			cout<<"Case #"<<i+1<<": Bad magician!\n";

	}
	
}
