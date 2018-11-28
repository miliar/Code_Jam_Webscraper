#include <iostream>
using namespace std;
#include<cmath>
#include<algorithm>
int main()
{
	int t;
	cin>>t;
	int l=1;
	while(t--)
	{
		int m;
		cin>>m;
		int a[1000000]={0};
		for(int i=0;i<m;i++)
		cin>>a[i];
		sort(a,a+m);
		reverse(a,a+m);
		int k=m;
	    int ans=10000000,g,h,max=a[0];
	    for(int i=1;i<=max;i++)
	    {
	    	g=0;h=i;
	    	for(int j=0;j<m;j++)
	    	{
	    		if(a[j]>i)
	    		{
		    		g+=(a[j]/i);
		    		if(a[j]%i==0)
		    		g--;
	    		}
	    	}
	    	g+=h;
	    	if(g<ans)ans=g;
	    }
	    cout<<"Case #"<<l<<": ";l++;
	    cout<<ans<<endl;
	}
}
