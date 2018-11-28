#include <bits/stdc++.h>
using namespace std;
int main()
{ ios_base::sync_with_stdio(0);
	int t;
	long long n,i,m,k;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		int count=0,a[10]={0};
		cin>>n;
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",j); continue;
		}
		for(i=1;i<100000000;i++)
		{ int p=0;
			m=i*n;
			while(m!=0)
  			{
  				count = m%10;            
      			a[count]=1;
      			m/=10;
  			}
  			for(k=0;k<10;k++)
  			{
  				if(a[k]==1)
					p++;
			  }
			  if(p==10)
  		    	{ printf("Case #%d: %lli\n",j,i*n); break; }
  		}
	}
}
