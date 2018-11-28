#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n,i,count;
	char s[200];
	cin>>n;
	for(int tc=1;tc<=n;tc++)
	{
		cin>>s;
		int l=strlen(s);
		s[l]='+';
		count=0;
		for(i=l-1;i>=0;i--)
		{
			if(s[i]!=s[i+1]) count++;
		}
		cout<<"Case #"<<tc<<": "<<count<<endl;
	}
}
