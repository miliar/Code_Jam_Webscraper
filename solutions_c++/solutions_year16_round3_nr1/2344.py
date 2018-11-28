#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll arr[100001];
int main()
{
	ll t,i;
	FILE * pFile;
	pFile = fopen ("output.txt","w");
	cin>>t;
	ll ccc=0;
	while(t--)
	{
		ccc+=1;
		fprintf (pFile, "Case #%lld: ",ccc);
		ll n;
		cin>>n;
		ll sum=0;
		priority_queue<pair<ll,ll> > p;
		priority_queue<ll>q;
		for(i=0;i<n;i++)
		{
			cin>>arr[i];
			sum+=arr[i];
			p.push(make_pair(arr[i],i));
			q.push(arr[i]);
		}
		
		while(!p.empty())
		{
			pair<ll,ll> d=p.top();
			p.pop();
			q.pop();
			ll a=d.first;
			ll b=d.second;
			if(a<=0)
			break;
			if(p.size()==0)
			{
				//cout<<"hhh";
				for(ll i=0;i<a;i++)
				{
					fprintf (pFile, "%c",char(b+'A'));
				}
				fprintf (pFile, " ");
				break;
				
			}
			else
			{
				pair<ll,ll> dd=p.top();
				ll aa=dd.first;
				ll bb=dd.second;
				if(aa==a && q.size()==2 && aa==1)
				{
					fprintf (pFile, "%c",char(b+'A'));
					//p.pop();
					//cout<<char(b+'A');
					//cout<<char(bb+'A');
					//cout<<" ";
					fprintf (pFile, " ");
					a-=1;
					//aa-=1;
					//p.push(make_pair(a,b));
					p.push(make_pair(a,b));
					if(a>0) 
					q.push(a);
				}
				else if(aa==a)
				{
					p.pop();
					q.pop();
					fprintf (pFile, "%c",char(b+'A'));
					//cout<<char(b+'A');
					fprintf (pFile, "%c",char(bb+'A'));
					//cout<<char(bb+'A');
					//cout<<" ";
					fprintf (pFile, " ");
					a-=1;
					aa-=1;
					p.push(make_pair(a,b));
					p.push(make_pair(aa,bb));
					if(a>0)
					q.push(a);
					if(aa>0)
					q.push(aa);
				}
				else
				{
					if(abs(aa-a)>=2)
					{
						fprintf (pFile, "%c",char(b+'A'));
						fprintf (pFile, "%c",char(b+'A'));
						//cout<<char(b+'A');
						//cout<<char(b+'A');
						//cout<<" ";
						fprintf (pFile, " ");
						a-=2;
						p.push(make_pair(a,b));
						if(a>0)
						q.push(a);
					}
					else
					{
						fprintf (pFile, "%c",char(b+'A'));
						fprintf (pFile, " ");
						//cout<<char(b+'A');
						//cout<<char(b+'A');
						//cout<<" ";
						a-=1;
						p.push(make_pair(a,b));
						if(a>0)
						q.push(a);
					}
				}
			}
		}
		
		fprintf (pFile, "\n");
	}
}
