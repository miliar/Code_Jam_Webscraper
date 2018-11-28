#include<cstdio>
#include<iostream>
#include<string>

using namespace std;

string output(string s)
{
	int i;
	
	string r;
	r.push_back(s[0]);
	
	for(i=1;i<s.length();i++)
	{
		if(s[i]>= r[0])
		{
			string t;
			t.push_back(s[i]);
			int j;
			for(j=0;j<i;j++)
				t.push_back(r[j]);
			r.clear();
			for(int j=0;j<t.length();j++)
				r.push_back(t[j]);
		}
		else
		{
			string t;
			
			int j;
			for(j=0;j<i;j++)
				t.push_back(r[j]);
			t.push_back(s[i]);
			r.clear();
			for(int j=0;j<t.length();j++)
				r.push_back(t[j]);
		}
		
		
	}
	return r;
	
	
}

int main()
{
	
	int t;
	cin>>t;
	
	int cnt = 1;
	while(t--)
	{
		string s;
		cin>>s;
		
		cout<<"Case #"<<cnt<<": "<<output(s)<<endl;
		cnt++;
	}
}