#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;
bool cmp(const pair<int,char>a,const pair<int,char>b)
{
	return a.first>b.first;
	
}
int main() {
	// your code goes here
	
	int t,r,i;
	cin>>t;
	r=1;
	while(r<=t)
	{
		cout<<"Case #"<<r<<": ";
		int n,b,s;
		vector<pair<int,char>>a;
	pair<int,char>c;
		cin>>n;
		s=0;
		for(i=0;i<n;i++)
		{
			cin>>b;
			c=make_pair(b,65+i);
			a.push_back(c);
			s+=a[i].first;
			//a.second.push_back(65+i);
		}
		//cout<<s;
		//sort(a.begin(),a.end(),cmp);
		for(i=0;i<n;i++)
		{
			//cout<<a[i].first<<a[i].second<<"\n";
			
		}
		int l;
		if(n==2)
		{
				sort(a.begin(),a.end(),cmp);
					while(s>0)
		{
			sort(a.begin(),a.end(),cmp);
		    l=(s-2)/2;
		    //cout<<l;
		    if(a[0].first-1<=l&&a[1].first-1<=l)
		    {
		    	s-=2;
		    	//cout<<"hahaah";
		    	cout<<a[0].second<<a[1].second<<" ";
		    	a[0].first--;
		    	a[1].first--;
		    }
		    else if(a[0].first-2<=l&&a[1].first<=l)
		    {
		    	s-=2;
		    	//cout<<"hahaah";
		    	cout<<a[0].second<<a[0].second<<" ";
		    	a[0].first-=2;
		    	//a[1].first--;
		    }
		    else
		    {
		    	
		    	s--;
		    //	cout<<"ha";
		    	cout<<a[0].second<<" ";
		    	a[0].first--;
		    }
			//s--;
		}
				
		}
		if(n>2)
		while(s>0)
		{
			sort(a.begin(),a.end(),cmp);
		    l=(s-2)/2;
		    //cout<<l;
		    if(a[0].first-1<=l&&a[1].first-1<=l&&a[2].first<=l)
		    {
		    	s-=2;
		    	//cout<<"hahaah";
		    	cout<<a[0].second<<a[1].second<<" ";
		    	a[0].first--;
		    	a[1].first--;
		    }
		    else if(a[0].first-2<=l&&a[1].first<=l)
		    {
		    	s-=2;
		    	//cout<<"hahaah";
		    	cout<<a[0].second<<a[0].second<<" ";
		    	a[0].first-=2;
		    	//a[1].first--;
		    }
		    else
		    {
		    	
		    	s--;
		    //	cout<<"ha";
		    	cout<<a[0].second<<" ";
		    	a[0].first--;
		    }
			//s--;
		}
		
		cout<<"\n";
		r++;
		
		//cout<<t+1;
	}
	return 0;
}