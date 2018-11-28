#include<cstdio>
#include<iostream>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	
	int t;
	cin>>t;
	
	int cnt = 1;
	while(t--)
	{
		string s;
		cin>>s;
		
		int idx = s.length();
		int i;
		for(i=s.length()-1;i>=0;i--)
		{
			if(s[i] == '+')
				idx--;
			else
				break;
		}
		//cout<<idx<<endl;
		string r;
		for(i=0;i<idx;i++)	
		{
			r.push_back(s[i]);
		}
		if(r.length() == 0)
		{
			cout<<"Case #"<<cnt<<": 0"<<endl;
			cnt++;
			continue;
			
		}
		if(r.length() == 1)
		{
			cout<<"Case #"<<cnt<<": 1"<<endl;
			cnt++;
			continue;
		}
		
		int fl = 0;
		for(i=1;i<r.length();i++)
		{
			if(r[i] != r[i-1])
				fl++;
		}
		
		cout<<"Case #"<<cnt<<": "<<fl+1<<endl;
		cnt++;
	}
	
	
	
	
}