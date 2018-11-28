#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
	int t=0;
	cin>>t;
	int p=1;
	while(p<=t)
	{
		int smax=0,s;
		int prev,neww;
		int count=0;
		int fr=0;
		getchar();
		cin>>smax;
		getchar();
		s=getchar()-'0';
		
		if(smax==0&&s==0)
			{cout<<"Case #"<<p<<": 0-"<<endl; break;}
		prev=s;count+=prev;
		for (int i = 1; i <= smax; ++i)
		{
			s=getchar()-'0';
			neww=s;
			if(count>=i)
			{
				prev=neww;
				count+=prev;
			}
			else {
				fr++;
				prev=neww;
				count++;
				count+=prev;
			}
		}
		cout<<"Case #"<<p<<": "<<fr<<endl;
		
		++p;
	}
	return 0;
}