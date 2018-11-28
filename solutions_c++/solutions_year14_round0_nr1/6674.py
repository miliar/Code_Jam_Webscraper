#include <iostream>
#include <set>
using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int t=1; t<=T; t++)
	{
		int fst,sec;
		set<int> set1[5], set2[5];
		cin>>fst;

		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				int a;
				cin>>a;
				set1[i].insert(a);
			}
		}
		
		cin>>sec;

		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				int a;
				cin>>a;
				set2[i].insert(a);
			}
		}
		set<int> res; 
		for(set<int>::iterator it = set1[fst].begin(); it != set1[fst].end(); it++)
		{
			if(set2[sec].find(*it) != set2[sec].end())
			{
				res.insert(*it);
			}
		}

		cout<<"Case #"<<t<<": ";
		if(res.size() == 1)
		{
			cout<<(*res.begin())<<endl;
		}
		else if(res.size() == 0)
		{
			cout<<"Volunteer cheated!"<<endl;
		}
		else if(res.size() > 1)
		{
			cout<<"Bad magician!"<<endl;
		}
	}
}