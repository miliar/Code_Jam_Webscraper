#include<iostream>
#include<vector>
#include<algorithm>
#include<string>

using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i1=1;i1<=t;i1++)
	{
	    int d;
	    cin>>d;
	    vector<int>p;
	    int mx=0;
	    for(int i=1;i<=d;i++)
	    {
	    	int a;
	    	
	    cin>>a;
	    p.push_back(a);
	    mx=max(mx,a);
	    }
	    int ans=mx;
	    // sort(p.begin(),p.end());
	     
	      for(int i=1;i<=mx;i++)
	      {   
	      	int nw=0,mxx=0;
	      	for(int j=0;j<d;j++)
	      	{
	      		if(p[j]>i)
	      		{
	      			nw+=p[j]/i-1;
	      		    if(p[j]%i)
	      		    nw++;

	      			mxx=max(mxx,i);
	      		}
	      		else
	      		mxx=max(mxx,p[j]);
	      	
	      	}
	      	nw+=mxx;
	      	ans=min(nw,ans);
	      	
	      }
		cout<<"Case #"<<i1<<": "<<ans<<endl;

	}
	
	return 0;
}