#include<bits/stdc++.h>
using namespace std;


int main()
{
	freopen("E://A.in","r",stdin);
	freopen("E://ans.out","w",stdout);
	int t,test=0;
	scanf("%d",&t);
	while(test!=t)
	{
		int n,i,no;
		string c="A",t;
		scanf("%d",&n);
		priority_queue<pair<int,string> >  pq;
		for(i=0;i<n;i++)
		{
			scanf("%d",&no);
			t=c[0]+i;
			pq.push(make_pair(no,t));
		}
		vector<string> vec;
		pair<int,string> one,two;
		string temp;
		while(!pq.empty())
		{
			if(pq.size()==1)
			{
				one=pq.top();
				pq.pop();
				temp=one.second;
				vec.insert(vec.begin(),temp);
				break;
			}
			
			one=pq.top();
			pq.pop();
			two=pq.top();
			pq.pop();
			one.first=one.first-1;
			two.first=two.first-1;
			temp=one.second+two.second;
			vec.push_back(temp);
			if(one.first!=0)
			pq.push(one);
			if(two.first!=0)
			pq.push(two);
		}
		cout<<endl<<"Case #"<<test+1<<": ";
		for(i=0;i<vec.size();i++)
		{
			cout<<vec[i]<<" ";
		}
		vec.clear();
		test++;
	}
	
	
	
}
