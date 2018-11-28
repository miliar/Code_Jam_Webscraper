#include<iostream>
#include<vector>
#include<set>
using namespace std;
int main()
{
	int t,a,b;
	cin>>t;
	for(int cs = 1; cs <=t ;cs++)
	{
		set<int>s;
		vector<int>count(17,0);
		cin>>a;
		int tmp;
		for (int i = 1; i <= 4; i++)
		{
			for (int j = 1; j <=4; j++)
			{
				cin>>tmp;
				if(a == i)
				{
					s.insert(tmp);
					count[tmp]++;
				}
			}
		}
		cin>>b;
		for (int i = 1; i <= 4; i++)
		{
			for (int j = 1; j <=4; j++)
			{
				cin>>tmp;
				if(b == i)
				{
					s.insert(tmp);
					count[tmp]++;
				}
			}
		}
		
		if(s.size() == 8)
			cout<<"Case #"<<cs<<": "<<"Volunteer cheated!"<<endl;
		else if(s.size() == 7)
		{
			for (int i = 1; i < 17; i++)
			{
				if(count[i]==2)
				{
					cout<<"Case #"<<cs<<": "<<i<<endl;
					break;
				}
			}
		}
		else if(s.size() < 7)
			cout<<"Case #"<<cs<<": "<<"Bad magician!"<<endl;
	}
	return 0;
}