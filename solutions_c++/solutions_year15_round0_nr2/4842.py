#include <iostream>
using namespace std ;
main() 
{

	int T = 0;
	cin>>T;
	for( int i = 0 ; i < T;i++)
	{
		int D;
		cin>>D;
		int arr[1001];
		int mx = 0;
		int mn = 0;
		for( int j = 0 ; j < D; j++)
		{
			cin>>arr[j];
			if( mx < arr[j]) 
				mx = arr[j];
		}
		mn = mx;
		int s = 0;
		for(int j = 1; j < mx+1; j++)
		{
			s = j;
			for( int k = 0 ; k < D;k++)
			{
				if( arr[k] > j)
				{
					if( arr[k]%j == 0)			
						s = s+(arr[k]/j-1);	
					else
						s = s+(arr[k]/j);	
				}
			}
			if( mn > s) mn=s;
		}
		cout<<"Case #"<<i+1<<": "<<mn<<endl;
	}
}

