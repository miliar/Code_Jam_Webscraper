#include <bits/stdc++.h>

 
using namespace std;
 
int n;
int counter[2600];
 
main() 
{
	int t;
	cin>>t;
	for(int cases=1;cases<=t;cases++)
	{
		
        memset(counter,0,sizeof(counter));
		cin>>n;
 
		for(int i=1;i<=2*n-1;i++)
			for(int j=1;j<=n;j++) 
			{
				int error;
				cin>>error;
				counter[error]++;
			}
            printf("Case #%d: ",cases);
			for(int i=1;i<=2600;i++) 
				if(counter[i]%2==1)
				  cout<<i<<" ";
 
			cout<<endl;
	}
		return 0;
}