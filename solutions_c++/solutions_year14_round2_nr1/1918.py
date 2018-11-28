#include<bits/stdc++.h>
using namespace std;


		

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	//freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,n,k,i,j,ans,flag,ind;
	int a[100],b[100];
	vector< char> v1,v2;
	vector< pair<char,int> > p1,p2;
	char c;
	string s1,s2;
	cin>>t;k=0;
	while(t--)
	{
		cin>>n;k++;
		cin>>s1>>s2;
		ans=0;flag=0;
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		p1.clear();p2.clear();
		p1.push_back(make_pair(s1[0],1));p2.push_back(make_pair(s2[0],1));ind=0;
		for(i=1;i<s1.size();i++)
		{
			if(s1[i]==s1[i-1]){p1[ind].second++;}
			else {ind++;p1.push_back(make_pair(s1[i],1));}
		
		}
		ind=0;
		for(i=1;i<s2.size();i++)
		{
			if(s2[i]==s2[i-1]){p2[ind].second++;}
			else {ind++;p2.push_back(make_pair(s2[i],1));}
		}
		//for(i=0;i<p1.size();i++){cout<<p1[i].first<<" "<<p1[i].second<<"\n";}
		//for(i=0;i<p2.size();i++){cout<<p2[i].first<<" "<<p2[i].second<<"\n";}
		v1.clear();
		v2.clear();
		v1.push_back(s1[0]);v2.push_back(s2[0]);
		for(i=1;i<s1.size();i++)
		{
			if(s1[i]!=s1[i-1]){v1.push_back(s1[i]);}
		}
		for(i=1;i<s2.size();i++)
		{
			if(s2[i]!=s2[i-1]){v2.push_back(s2[i]);}
		}
		if(v1.size()!=v2.size())
		{
			flag=1;
		}
		else
		{
		for(i=0;i<v1.size();i++)
		{
			if(v1[i]!=v2[i]){flag=1;break;}
		}
		}
		if(flag==0)
		{
			for(i=0;i<min(p1.size(),p2.size());i++)
			{
				ans+=abs(p1[i].second-p2[i].second);
				if(p1[i].first!=p2[i].first){flag=1;break;}
			}
		}
			
		if(flag==1)
		{
			printf("Case #%d: Fegla Won\n",k);
		}
		else
		{
					
			printf("Case #%d: %d\n",k,ans);	
		}
	}
	return 0;
		
}
					
					
					
					
					
					
					
