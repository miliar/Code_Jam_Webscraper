#include <iostream>  
#include<string.h>
using namespace std;

  
int main() {
  unsigned long long int t, n, j,ans;
    cin >> t; 
    char a[1000];
	for (int i = 1; i <= t; ++i) 
	{
		cin >> a;  
    	n = strlen(a);
    	ans=0;
    	j=0;
    	if(a[j]=='-')
    	{
		
			while(a[j]=='-'&&j<n)
			{
					j++;
			}
			
			ans++;
		}
		
		for(; j<n; j++)
		{
			
			
			if(a[j]=='-')
    		{
				while(a[j]=='-'&&j<n)
				{
					j++;
				}
				ans+=2;
			}
					
		}
		 
    	cout << "Case #" << i << ": " << ans << endl;

  }
  
  return 0;
  
}
