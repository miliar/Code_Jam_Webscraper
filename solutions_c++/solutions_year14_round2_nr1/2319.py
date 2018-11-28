#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <iomanip>
#include <vector>
#include <map>


#define p_b push_back
#define m_p make_pair


using namespace std;

string s[100];
int tt,t,i,j,num[200],sum,ans,mx,n,cnt[200],x,m1,m2,mn;
char c;
bool t1;


int f(int v)
{
	int sum=0,i;
	for (i=0; i<n; i++)
		sum+=fabs(num[i]-v);
	return sum;
}

int ter(int l,int r)
{
	while (r-l>0)
	{
		m1=l+(double)(r-l)/3+0.5;
		m2=r-(double)(r-l)/3+0.5;
		if (f(m1)>f(m2))
			l=m2;
		else
			r=m1;
	}
	int i,sum=0;
	for (i=0; i<n; i++)
		sum+=fabs(num[i]-r);
	return sum;
}

int main()
{
	ios_base::sync_with_stdio(false);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	for (tt=1; tt<=t; tt++)
	{
		cin>>n;
		for (i=0; i<n; i++)
		{
			cin>>s[i];
			cnt[i]=0;
		}
	   	t1=true;
	   	ans=0;
	   	while (cnt[0]<(int)s[0].length())
	   	{
	   		sum=0;
	   		mx=0;
	   		mn=1000;
	   		c=s[0][cnt[0]];
	   		for (i=0; i<n; i++)
	   		{
	   			j=cnt[i];
	   			while (j<(int)s[i].length() && s[i][j]==c) j++;
	   			if (j==cnt[i])
	   			{
	   				cout<<"Case #"<<tt<<": "<<"Fegla Won"<<endl;
	   				t1=false;
	   				break;
	   			}
	   			num[i]=j-cnt[i];
	   			sum+=num[i];
	   			if (mx<num[i]) mx=num[i];
	   			if (mn>num[i]) mn=num[i];
	   			cnt[i]=j;
	   		}
	   		if (!t1) break;
	   		x=ter(mn,mx);
	   		ans+=x;
	   	}
	   	if (!t1) continue;

	   	for (i=0; i<n; i++)
	   		if (cnt[i]!=s[i].length())
	   		{
	   			t1=false;
	   			cout<<"Case #"<<tt<<": "<<"Fegla Won"<<endl;
	   			break;
	   		}
	   	if (!t1) continue;
	   	cout<<"Case #"<<tt<<": "<<ans<<endl;
	}


	return 0;
}


