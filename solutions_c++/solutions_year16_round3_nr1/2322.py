#include <bits/stdc++.h>
using namespace std;
void solve(priority_queue < pair <int , char> > pq)
{
	bool flag =false;
	while(!pq.empty())
		{
		   pair <int ,char> p1 =pq.top();
		   if(p1.first == 1 && pq.size()==3)
		   {
		     pq.pop();
		   	 cout<<p1.second<<" ";
		   	 continue;
		   }
		   pq.pop();
		    pair <int ,char> p2;
		   if(!pq.empty())
		   {
		     p2 =pq.top();
		    pq.pop();
		    flag =true;
		   }
		   cout<<p1.second<<p2.second<<" ";
		   if(flag)
		   {
		    p1.first-=1;
		    p2.first-=1;
		    if(p1.first>0)
		    pq.push(p1);
		    if(p2.first>0)
		    pq.push(p2);
		  }
		  else 
		  {
		  	p1.first-=2;
		  	if(p1.first>0)
		    pq.push(p1);
		  }
		}
}

int main()
{
	int t;
	cin>>t;
	for (int tc=1; tc<=t; tc++)
	{
		int n;
		priority_queue < pair <int ,char> > pq;
		cin>>n;
		int senats[n+5];
		char ch='A';
		for(int i=0;i<n;i++)
		{
			cin>>senats[i];
			pq.push({senats[i],char(ch+i)});
		}
		cout<<"Case #"<<tc<<": ";
		solve(pq);
		cout<<endl;	
	}
}