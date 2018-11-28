#include<bits/stdc++.h>
using namespace std;
#define fs first
#define sc second
#define INF 1000000000
#define p 1000000007
#define pb push_back
#define mp make_pair
typedef long long Int;
typedef pair<Int,Int> pii;
typedef vector<Int> vi;
typedef vector<pii> vii;

int Calculate(string s)
{
	Int ans=0;

	if(s[0]=='+')
	{
		Int count=0;
		bool flag=true;				// true -> + 
		for(int i=0;i<s.length();i++)
		{
			if(s[i]=='-'&&flag==true)
			{
				flag=false;
				count++;
			}
			else if(s[i]=='+'&&flag==false)
			{
				flag=true;
				count++;
			}
		}
		if(count%2==0)
		return count;
		
		if(count>0)
		{
			count++;
			return count;
		}
		else
		return 0;
	}
	if(s[0]=='-')
	{
		Int count=0;
		bool flag=true;				// true -> - 
		for(int i=0;i<s.length();i++)
		{
			if(s[i]=='+'&&flag==true)
			{
				flag=false;
				count++;
			}
			else if(s[i]=='-'&&flag==false)
			{
				flag=true;
				count++;
			}
		}
		if(count%2!=0)
		return count;
		
		count++;
		return count;
	}

}

int main()
{
	Int T;
    cin>>T;
	for(int i=1;i<=T;i++)
	{
		string s;
		cin>>s;
		cout<<"Case #"<<i<<": "<<Calculate(s)<<endl;
	}
	return 0;
}