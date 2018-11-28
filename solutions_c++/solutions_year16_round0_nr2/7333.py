#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,i,j,count,cas=1,x;
	string s;
	cin>>t;
	while(t--)
	{
		cin>>s;
		x=s[0];
		i=s.size();
		count=0;
		for(j=1;j<i;j++)
		{
			if(s[j]==x);
			else
			{
				x=s[j];
				count++;
			}
		}
		if(s[i-1]=='-')	count+=1;
		cout<<"Case #"<<cas<<": "<<count<<endl;
		cas++;
	}
	return 0;
}
