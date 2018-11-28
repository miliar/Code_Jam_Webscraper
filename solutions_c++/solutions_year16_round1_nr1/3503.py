#include<bits/stdc++.h>
#define N 1000000007
#define maxs 300005
#define mins 1005
#define pf printf
#define sc scanf
#define ll long long
#define pb push_back
using namespace std;

int main()
{
	int t;
	sc("%d",&t);
	for(int l1=1;l1<=t;l1++)
	{
		string s;
		cin>>s;
		int n=s.length();
		cout<<"Case #"<<l1<<": ";
		char max1=s[0];
		int i;
		string st1="";
		stack<char> st;
		for(i=0;i<n;i++)
		{
			if(s[i]>=max1)
			{
				st.push(s[i]);
				max1=s[i];
			}
			else
			st1+=s[i];
		}
		while(!st.empty())
		{
			cout<<st.top();
			st.pop();
		}
		cout<<st1<<endl;
	}
	return 0;
}
