#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);

	string priyanka;
	getline(cin,priyanka);

	for(int i=1;i<=t;i++)
	{
		string s;
		getline(cin, s);

		int count = 0;
		for(int i=0;i<(s.length()-1);i++)
		{
			if(s[i] != s[i+1])
				count++;
		}
		count++;

		if(s[s.length()-1] == '+')
		{
			cout<<"Case #"<<i<<": "<<count-1<<endl;
		}
		else
		{
			cout<<"Case #"<<i<<": "<<count<<endl;
		}
	}
}