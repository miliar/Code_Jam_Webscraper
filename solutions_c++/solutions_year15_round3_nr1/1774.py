#include<iostream>		//ry
#include<cstdio>
#include<cmath>

using namespace std;

int xy(int r,int c,int w)
{
	if(w==c)
		return c;
	else
	{
		return (ceil((c*1.0)/w) -1 + w);
	}
}

int main()
{
	int t,cas=0;
	cin>>t;
	
	while(t--)
	{
		int ans=0,N,r,c,w;
		
		cin>>r>>c>>w;
		ans = xy(r,c,w);
		
		cout<<"Case #"<<++cas<<":"<<" "<<ans<<endl ;
			
		
	}
	return 0;
}
