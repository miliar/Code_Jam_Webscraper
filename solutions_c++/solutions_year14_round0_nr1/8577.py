#include <iostream>
#include <iomanip>
#include <cstdio>
#include <set>
using namespace std;
int main()
{

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	int row1, row2;
	int deck1[100], deck2[200];
	set<int> s1,s2;
	for(int testCase = 1; testCase<=t;testCase++)
	{
		s1.clear();
		cin>>row1;
		for(int i=0;i<16;i++)
		{
			cin>>deck1[i];
		}
		cin>>row2;
		for(int i=0;i<16;i++)
		{
			cin>>deck2[i];
		}

		for(int i=(row1-1)*4;i<(row1-1)*4+4;i++)
		{
			s1.insert(deck1[i]);
		}

		int cnt = 0;
		int answer;

		for(int i=(row2-1)*4;i<(row2-1)*4+4;i++)
		{
			if(s1.find(deck2[i])!=s1.end())
			{
				cnt++;
				answer=deck2[i];
			}
		}

		cout<<"Case #"<<testCase<<": ";
		if(cnt==0)
		{
			cout<<"Volunteer cheated!"<<endl;

		}
		else if(cnt==1)
		{
			cout<<answer<<endl;
		}
		else
		{
			cout<<"Bad magician!"<<endl;
		}

	}
	return 0;
}