#include <iostream>  
using namespace std;

int check( int a[] , unsigned long long int i)
{
	while(i!=0)
	{
		a [ i%10 ] ++;
		i/=10;
		
	}
	int flag=1;
	for(int i=0; i<=9; i++)
	{
		if(a[i]==0)
			flag=-1;
	}
	
	if(flag==-1)
	return 0;
	else
	return 1;
}

  
int main() {
  unsigned long long int t, n, m,ans;
    cin >> t; 
    
	for (int i = 1; i <= t; ++i) 
	{
    	int a[13]={0};
		cin >> n ;  
    	if(n==0)  
    	{
    		cout << "Case #" << i << ": " <<"INSOMNIA"<< endl; continue;	
		}
		ans=n;
		while(!check(a,ans))
		{
			ans+=n;
		}
    	cout << "Case #" << i << ": " << ans << endl;

  }
}
