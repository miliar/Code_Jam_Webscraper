#include<bits/stdc++.h>
using namespace std;
typedef long long int LL;

LL a[1000009];

int main()
{

	 ios_base:: sync_with_stdio(false); cin.tie(0);
	  
	   freopen("input.in","r",stdin);
         freopen("output.in","w",stdout);
        
        for(LL i=1;i<=1000009;i++)
        {
        	vector<bool>seen(10,false);
        	LL c=0; LL j=1;
        	while(c!=10)
        	{
        		LL k=i*j;
        		while(k)
        		{
        			if(!seen[k%10])
        			{
        				seen[k%10]=true;c++;
        			}
        			k/=10;
        		}
        		j++;
        	}
        	a[i]=i*(j-1);
        }
        int t;cin>>t;for(int i=1;i<=t;i++)
        {
        	 int n;
        	cin>>n;
        	if(a[n]==0)
        		cout<<"Case #"<<i<<":"<<" INSOMNIA"<<endl;
        	else
        		cout<<"Case #"<<i<<": "<<a[n]<<endl;
        }

	 return 0;
}

