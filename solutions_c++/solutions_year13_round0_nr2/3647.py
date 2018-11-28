#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int a[100][100],m,n;
int call()
{
	cin>>n>>m;
	bool f,g;
	for(int i=0;i<n;i++) for(int j=0;j<m;j++) 
		cin>>a[i][j]; 
	for(int i=0;i<n;i++) for(int j=0;j<m;j++)
	{ 
			f=1;g=1;
		    for(int i1=0;i1<n;i1++)
		    {
				if(a[i1][j]>a[i][j]) {f=0; cerr<<"f("<<i<<", "<<j<<")=>"<<f; break;}
			}
			for(int j1=0;j1<m;j1++)
			{
				if(a[i][j1]>a[i][j]) {g=0;cerr<<"g("<<i<<", "<<j<<")=>"<<g<<endl;break;}
			}
			if(f==0&&g==0) {cout<<"NO"; return 0;}
		}
	
	cout<<"YES";
	return 0;
}

int main()
{
	int TC;
	cin>>TC;
	for(int i=0;i<TC;i++)
	{
		cout<<"Case #"<<(i+1)<<": ";call(); cout<<endl;
	}
	return 0;
}
/*	vector<int>x(1);	
		x.resize(c+1);
		x[c]=a[i][j]; c++;
	}
	sort(x.begin(),x.end());
	for(int it=x.begin(); it<x.end()-1; it++)
	{
		if(x[it]==x(it+1))
		{
          x.erase(it);
          x.erase(it);
          it--;
		} 
	}
	for(int i=0;i<x.size();i++) cout<<x[i]<<" ";*/
