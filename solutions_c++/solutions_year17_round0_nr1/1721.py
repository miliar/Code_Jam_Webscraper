#include <bits/stdc++.h>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
	int tc;
	scanf("%d",&tc);
	for(int tmp=1;tmp<=tc;tmp++)
	{
		string s;
		int k;
		cin>>s>>k;
		int cnt=0;
		for(int temp=0;temp<=s.size()-k;temp++)
		{
			if(s[temp]=='-')
			{
				cnt++;
				for(int temp2=temp;temp2<temp+k;temp2++)
				{
					if(s[temp2]=='-')	s[temp2]='+';
					else	s[temp2]='-';
				}
			}
		}
		printf("Case #%d: ",tmp);
		bool check=true;
		for(int temp=0;temp<s.size();temp++)
		{
			if(s[temp]=='-')
			{
				cout<<"IMPOSSIBLE\n";
				check=false;
				break;
			}
		}
		if(check)	cout<<cnt<<"\n";
	}
}
