#include<bits/stdc++.h>
using namespace std;
#define f_in(st) freopen(st,"r",stdin);
#define f_out(st) freopen(st,"w",stdout);
int main()
{
	f_in("large1.in");
    f_out("large1out.in");
    int t,n,i,m=0;
    cin>>t;
    while(t--)
    {
    	m++;
    	cin>>n;
    	int a[n+1],sum=0,count=0;
    	for(i=1;i<=n;i++)
    	{
    		cin>>a[i];
    		sum=sum+a[i];
    	}
    	cout<<"Case #"<<m<<": ";
    	if(sum%2!=0)
    	{
    		int max=0,k=0;
    		for(i=1;i<=n;i++)
    		{
    			if(a[i]>max)
    			{
    				max=a[i];
    				k=i;
				}
			}
			char ch =k+64;
			a[k]--;
			count++;
			cout<<ch<<" ";
		}
		while(count<sum)
		{
			int max=0,max1=0,k=0,l=0;
			for(i=1;i<=n;i++)
			{
				if(a[i]>max)
				{
					max1=max;
					max=a[i];
					l=k;
					k=i;
				}
				else if(a[i]>max1)
				{
					max1=a[i];
					l=i;
				}
			}
			count=count+2;
			char c=k+64,c1=l+64;
			cout<<c<<c1<<" ";
			a[k]--;
			a[l]--;
		}
		cout<<endl;
	}
    return 0;
}
