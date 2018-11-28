#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<cstring>
#include<cmath>
#include<cstdio>
#include<stack>
#include<queue>
#include<deque>
#include<list>
#include<map>
#include<set>
#include<numeric>
#include<iterator>
using namespace std;
int main()
{
	int n;
	freopen("1.in","r",stdin);
	freopen("out2.txt","w",stdout);
	while(cin>>n)
	{
		for(int kk=0;kk<n;kk++)
		{
			string s;
			list<char> ans;
			cin>>s;
			for(int i=0;i<s.length();i++)
			{
				if(s[i]<ans.front())
				ans.push_back(s[i]);
				else
				ans.push_front(s[i]);
			}
			cout<<"Case #"<<kk+1<<": ";
			for(list<char>::iterator x=ans.begin();x!=ans.end();x++)
			cout<<*x;
			cout<<endl; 
		}
	}	
} 
