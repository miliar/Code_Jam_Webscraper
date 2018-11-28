#include <bits/stdc++.h>
 
using namespace std;
 
int main()
{   std::ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int ti=0;ti<t;ti++)
	{	int n;
		string s;
		cin>>n>>s;
		int count=0;
		int add=0;
		for(int i=0;i<=n;i++)
		{	if(add+count>=i)count+=(s[i]-'0');
			else 
			{	add+=i-(add+count);
				count+=(s[i]-'0');
			}
		}
		cout<<"Case #"<<(ti+1)<<": "<<add<<endl;
	}
}
