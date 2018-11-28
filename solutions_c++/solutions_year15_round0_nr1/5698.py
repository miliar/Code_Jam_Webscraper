#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int d;
		cin>>d;
		d++;
		int *k=new int[d];
		char *str=new char[d+1];
		cin>>str;
		int people=0;
		int added=0;
		for(int j=0;j<d;j++)
		{
			if(j>people)
			{
				added+=j-people;
				people=j;
			}
			people+=str[j]-48;
			//cout<<people<<endl;

		}
		cout<<"Case #"<<i<<": "<<added<<endl;
	}
}