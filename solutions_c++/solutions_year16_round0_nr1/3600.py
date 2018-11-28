#include <bits/stdc++.h>
using namespace std;
long long inf = 9000000000000000000;

void digit(long long n,int mark[])
{
	while(n)
	{
		int rem = n%10;
		//cout<<rem<<" ";
		mark[rem]  = 1;
		n/=10;
	}
}

int main()
{   int t,r=1;

	#ifndef ONLINE_JUDGE
	    freopen("input.txt","r",stdin);
	    // freopen("output.txt","w",stdout);
	  #endif

	cin>>t;
	

	while(t--)
	{    
		   int n,j=1,i, mark[10] = {0}; 
		   cin>>n; 

		long long ans = n;

		while(n)
		{  // cout<<ans<<" ";
			digit(ans,mark);

			int k = 1;

			for(i=0;i<=9;i++)
				if(mark[i]==0)
					k=0;

			// for(i=0;i<=9;i++)
			//   cout<<mark[i]<<" ";

			 // cout<<endl;	

			if(k==1)
			  break;

            j++;
			ans = n*j;
			
		}

		if(n)
			cout<<"Case #"<<r<<": "<<ans<<endl;

		else 
			cout<<"Case #"<<r<<": "<<"INSOMNIA\n";
		 r++;

	}




 	return 0;
}