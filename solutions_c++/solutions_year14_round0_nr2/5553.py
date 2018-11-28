#include "bits/stdc++.h"

#define eps 1e-7

using namespace std;

struct node
{
	double c,p,t;
	
	node(double _c=0,double _p=0,double _t=0)
	{
		c=_c;
		p=_p;
		t=_t;
	}
	
	friend bool operator < (const node &a,const node &b)
	{
		return a.t > b.t;
	}
	
}	tmp;

int T;

priority_queue < node > pq;

void read()
{
	scanf(" %d",&T);
	
	for(int i=1;i<=T;i++)
	{
		double C,F,X,Min=(double)INT_MAX;
		
		scanf(" %lf %lf %lf",&C,&F,&X);
		
		printf("Case #%d: ",i);
		
		while(!pq.empty())
			pq.pop();
		
		pq.push(node((double)0,(double)2,(double)0));
		
		while(!pq.empty())
		{
			tmp=pq.top();
			pq.pop();
			
			if(tmp.t > Min)
			{
				printf("%.7lf\n",Min);
				break;
			}
			
			double ans=tmp.t+(X-tmp.c)/tmp.p;
			
			if(ans < Min)
				Min=ans;
			
			if(tmp.c>=C)
				pq.push(node(tmp.c-C,tmp.p+F,tmp.t+(double)1));
			
			else if(tmp.c<C)
				pq.push(node(0,tmp.p+F,tmp.t+((C-tmp.c)/tmp.p)));
		}
	}
}

int main()
{
	read();
	
	return 0;
}
