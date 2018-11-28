#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int t, n, i, j, k,p, pp=1;
	string s="1234567890", ss;
	cin>>t;
	while(t>0)
	{cin>>n;
	if(n<=0)
			{
				cout<<"Case #"<<pp<<": "<<"INSOMNIA"<<"\n";
				
			}
			else
			{
		for(i=0;i<100 ; i++)
		{
			p = (i+1)*n;
			ss = to_string(p);
			
			for(k=0; k<ss.length(); k++)
			{
				for(j=0; j<=9; j++)
				{
					if(s[j]==ss[k])
					{
						s[j]='*';
						//cout<<s<<"\n";
						break;
					}
				}
			//	cout<<s<<"\n";
				if(s=="**********")
					break;
			}
			if(s=="**********")
				break;

		}
	//cout<<s;
		cout<<"Case #"<<pp<<": "<<p<<"\n";}
		++pp;
		t=t-1;
		s="1234567890";
	}
	return 0;
}