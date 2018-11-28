#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define pii pair <int ,char>
int p[1001];
int main()
{
	int t,p1=1;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	while(t--)
	{
		int n;
		priority_queue < pair <int ,char> > q;
		cin>>n;
		char ch='A';
		for(int i=0;i<n;i++)
		{
			cin>>p[i];
			char ch1=ch+i;
			q.push(make_pair(p[i],ch1));
		}
		bool flag =false;
		cout<<"Case #"<<p1<<": ";
		while(!q.empty())
		{
		   pii p1 =q.top();
		   if(p1.first==1&&q.size()==3)
		   {
		     q.pop();
		   	 cout<<p1.second<<" ";
		   	 continue;
		   }
		   q.pop();
		    pii p2;
		   if(!q.empty())
		   {
		     p2 =q.top();
		    q.pop();
		    flag =true;
		   }
		   cout<<p1.second<<p2.second<<" ";
		   if(flag)
		   {
		    p1.first-=1;
		    p2.first-=1;
		    if(p1.first>0)
		    q.push(p1);
		    if(p2.first>0)
		    q.push(p2);
		  }
		  else 
		  {
		  	p1.first-=2;
		  	if(p1.first>0)
		    q.push(p1);
		  }
		}
		p1++;
		cout<<"\n";
	}
	return 0;
}