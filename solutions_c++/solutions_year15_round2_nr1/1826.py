#include<bits/stdc++.h>
using namespace std;
#define PII pair< long long, long long>
map<long long, long long> m;
priority_queue< PII, vector< PII >, greater< PII> > q;
long long rev(long long n)
{
	long long m=0;
	while(n)
	{
		m=m*10+(n%10);
		n/=10;
	}
	return m;
}
int main()
{
	long long int t,tt,i,j,n;
	PII x;
	cin>>tt;
	for(t=1;t<=tt;t++)
	{
		while(!q.empty())
			q.pop();
		m.clear();
		cin>>n;
		m[n]=1;
		q.push(make_pair(1,n));
		//cout<<"Pushing 1,"<<n<<"\n";
		while(1)
		{
			x = q.top();
		//	cout<<"Top : "<<x.first<<","<<x.second<<"\n";
			q.pop();
			if(x.second == 1)
			{
				cout<<"Case #"<<t<<": "<<x.first<<"\n";
				break;
			}
			if(x.second%10!=0)
			{
				i = rev(x.second);
				if(m[i]==0 || m[i]>1+m[x.second])
				{
					m[i]=1+m[x.second];
					q.push(make_pair(m[i],i));
		//			cout<<"Pushing "<<m[i]<<","<<i<<"\n";
				}
			}
			i = x.second-1;
			if(m[i]==0 || m[i]>1+m[x.second])
			{
				m[i]=1+m[x.second];
				q.push(make_pair(m[i],i));
		//		cout<<"Pushing "<<m[i]<<","<<i<<"\n";
			}
		}
		//cout<<"***\n";
	}
}