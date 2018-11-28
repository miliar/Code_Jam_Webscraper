#include<algorithm>
#include<iostream>
#include<string>
#include<vector>
using namespace std;

int main()
{
	int T;
	cin>>T;
	for(auto i(0);i!=T;++i)
	{
		int S,y(0);
		string str;
		cin>>S>>str;
		int people(0);
		for(auto j(0);j!=str.size();++j)
		{
			if(people<j)
			{
				y+=j-people;
				people=j;
			}
			people+=str[j]-48;
		}
		cout<<"Case #"<<i+1<<": "<<y<<endl;
	}
}