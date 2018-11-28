#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t=0;
	cin>>t;
	int p=1;
	for(int i=1;i<=t;i++){
		int len=0,s,prev,curr,count=0,dost=0;
		getchar();
		cin>>len;
		getchar();
		s=getchar()-'0';
		
		if(len==0&&s==0)
			cout<<"Case #"<<i<<": 0-"<<endl;
		prev=s;count+=prev;
		for (int i = 1; i <= len; ++i)
		{
			s=getchar()-'0';
			curr=s;
			if(count>=i)
			{
				prev=curr;
				count+=prev;
			}
			else {
				dost++;
				prev=curr;
				count++;
				count+=prev;
			}
		}
		cout<<"Case #"<<i<<": "<<dost<<endl;
	}
	return 0;
}
