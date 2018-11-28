#include <bits/stdc++.h>
using namespace std;
int main()
{
	int T;
	cin>>T;
	for(int t = 1;t<=T;t++)
	{
		cout<<"Case #"<<t<<": ";
		int Ans1;
		cin>>Ans1;
		Ans1-=1;
		int v;
		set<int> S;
		for(int i = 0;i<4;i++)
		{
			for(int j = 0;j<4;j++)
			{
				cin>>v;
				if(i==Ans1)
				{
					S.insert(v);
				}
			}
		}
		int Ans2;
		cin>>Ans2;
		Ans2-=1;
		set<int> F;
		for(int i = 0;i<4;i++)
		{
			for(int j = 0;j<4;j++)
			{
				cin>>v;
				if(i==Ans2)
				{
					if(S.find(v)!=S.end()){
						F.insert(v);
					}
				}
			}
		}
		if(F.empty())
		{
			cout<<"Volunteer cheated!"<<endl;
		}
		else if(F.size()>1)
		{
			cout<<"Bad magician!"<<endl;
		}
		else
		{
			cout<<*F.begin()<<endl;
		}
	}
	return 0;
}
