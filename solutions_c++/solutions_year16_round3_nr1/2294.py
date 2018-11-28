#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define pii pair <int ,char>
int p[1100];


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
    int t;
	scanf("%d",&t);
	int num = t;
	while(t--)
	{
		printf("Case #%d: ",num-t);
		int n;
		scanf("%d",&n);
		priority_queue < pair <int ,char> > q;
		char ch='A';
		for(int i=0;i<n;i++)
		{
			scanf("%d",&p[i]);
			char ch1=ch+i;
			q.push({p[i],ch1});
		}
		bool flag =false;
		while(!q.empty())
		{
		   pii p1 =q.top();
		   if(p1.first==1&&q.size()==3)
		   {
		     q.pop();
		   	 cout<<p1.second<<" ";
		   	 continue;
		   }
			pii p2;
		   q.pop();
		   if(!q.empty())
		   {
		     p2 = q.top();
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
		printf("\n");
	}
	return 0;
}

