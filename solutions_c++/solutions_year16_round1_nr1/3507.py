#include<bits/stdc++.h>
using namespace std;


int main()
{
	freopen("D://A.in","r",stdin);
	freopen("D://ans.out","w",stdout);
	int t,test=0;
	scanf("%d",&t);
	while(test!=t)
	{
		string s,temp="";
		cin>>s;
		int i;
		/*queue<string> str;
		
		temp=temp+s[0];
		str.push(temp);
		for(i=1;i<s.length();i++)
		{
			temp=
		}
		*/
		temp=temp+s[0];
		for(i=1;i<s.length();i++)
		{
			if(temp[0]>s[i])
			{
				temp=temp+s[i];
			}
			else
				temp=s[i]+temp;
		}
		cout<<endl<<"Case #"<<test+1<<": "<<temp;
		test++;
	}
}
