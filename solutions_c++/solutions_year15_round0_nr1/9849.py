#include<iostream>
using namespace std ;
 
 
 
int main() 
{
	int t ;  int size ; int sum ; 
	cin>>t ;  string array ; int ans ;
	while(t)
	{  sum=0 ;
		cin>>size ; ans =0 ;
		cin>>array ;
		sum=(array[0] -'0') ;
		for(int i =1 ;i<=size;i++)
		{
			if(i>sum&&(array[i]-'0')!=0)
			{  ans =ans+i-sum ;
				sum=i ; 
				
			}
			sum=sum+array[i]-'0' ;
		}
		cout<<ans<<endl ;
		
		t-- ;
	}
	
	
	
}
