#include <iostream>
#include <vector>
using namespace std;
vector <int> first;
vector <int> second;
int main() 
{
	int t,row,x;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		cin>>row;
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				cin>>x;
				if(i==row)
				first.push_back(x);
			}	
		}
		
		cin>>row;
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				cin>>x;
				if(i==row)
				second.push_back(x);
			}	
		}
		int cnt=0,index=0;
		
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				//cout<<"first="<<first[i]<<" second="<<second[j]<<endl;
				if(first[i]==second[j])
				{
					cnt++;
					index=i;
				}	
			}
		}
		//cout<<"cnt="<<cnt<<" index="<<index<<endl;
		if(cnt==1)
		cout<<"Case #"<<k<<": "<<first[index]<<endl;
		else if(cnt>1)
		cout<<"Case #"<<k<<": Bad magician!"<<endl;
		else if(cnt==0)
		cout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
		
		first.clear();
		second.clear();
	}
	return 0;
}