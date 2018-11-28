// Bismillahir Rahmanir Rahim

#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <utility>
#include <algorithm>
using namespace std;


vector<int>v;
typedef pair<int,int> pi;

pi calc(int cur,int in)
{
	int a,b,c,d,e,x,y,z;
	
	x=0;
	//cout<<"Now at "<<cur<<" "<<in<<endl;
	while(1)
	{
		if(cur>v[in]) break;
		cur=cur+cur-1;
		x++;
	}
	//cout<<x<<" needed "<<endl;
	y=0;
	for(a=in;a<v.size();a++)
	{
		if(cur<v[a]) break;
		y++;
		cur=cur+v[a];
	}
	pi k;
	k.first=x; k.second=y;
	return k;
}

int main()
{
	//freopen("0.in","r",stdin);
	//freopen("00.out","w",stdout);
	
	int a,b,c,d,e,x,y,z,t,cur;
	
	cin>>t;
	
	for(int i=1;i<=t;i++)
	{
		int n;
		
		cin>>cur;
		e=cur;
		cin>>n;
		v.clear();
		for(a=0;a<n;a++)
		{
			cin>>x;
			v.push_back(x);
		}
		sort(v.begin(),v.end());
		
		if(cur==1)
		{
			printf("Case #%d: %d\n",i,v.size());
			continue;
		}
		int ans;
		ans=100;
		z=0;
		pi p;
		//for(a=0;a<v.size();a++) cout<<v[a]<<" "; cout<<endl;
		
		
		for(a=0;a<n;a++)
		{
			if(cur>v[a])
			{
				//cout<<"Auto absorb "<<a<<" "<<v[a]<<" "<<cur+v[a]<<endl;
				cur=cur+v[a];
			}
			else
			{
				p=calc(cur,a);
				x=p.first;
				y=p.second;
				ans=min(ans,z+(n-a));
				
				//cout<<"Absorbing at"<<a<<" "<<v[a]<<" "<<cur<<"->";
				z=z+x;
				for(b=0;b<x;b++) cur=cur+cur-1;
				cur=cur+v[a];
				//cout<<cur<<endl;
			}
		}
		ans=min(ans,z);
		printf("Case #%d: %d\n",i,ans);
		/*cout<<e<<"->";
		for(a=0;a<v.size();a++) cout<<v[a]<<" "; cout<<endl;*/
	}
	
	return 0;
}
