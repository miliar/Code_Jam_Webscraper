#include <iostream>
#include <string>
using namespace std;
int main() {
	freopen("B-large.in","r",stdin);
	freopen("out.rtf","w",stdout);
	int t;
	cin>>t;
	for(int  i=0;i<t;i++)
	{
		string s;
		cin>>s;
		int a=s.size(),r=0;
		
		for(int j=0;j<a-1;j++)
		{
			if(s[j]!=s[j+1])
			{
				for(int k=j;k>=0;k--)
				s[k]=s[j+1];
				
				++r;
			}
		}
		if(s[0]=='-') ++r;
		
		cout<<"Case #"<<i+1<<": "<<r;
		if(i+1!=t)
		cout<<"\n";
	}
	return 0;
}

