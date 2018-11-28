#include <iostream>
#include <deque> 
#include<string.h>
using namespace std;
int digit[30];
int alpha[30] , c;

  
int main() 
{
  unsigned long long int t, n, m,copy;
    cin >> t; 
    char a[2103];
   
	for (int i = 1; i <= t; ++i) 
	{
	
		for(int j=0; j<30; j++)
		{
			alpha[j]=digit[j]=0;	
		}	
	
	
    	cin>>a;
    	int len = strlen(a);
    
    	
		for(int j=0; j<len; j++)
		{
			c = a[j] - 'A' ;
			alpha[ c ] ++;				
		}
		
		//0
		if( alpha[ 'Z' - 'A' ] > 0)
		{
			digit[0] = alpha[ 'Z' - 'A'];
			alpha[ 'Z' - 'A' ] -= digit[0] ;
			alpha[ 'E' - 'A' ] -= digit[0] ;
			alpha[ 'R' - 'A' ] -= digit[0] ;
			alpha[ 'O' - 'A' ] -= digit[0] ;
		}
		
		
		//2
		
		if( alpha[ 'W' - 'A' ] > 0)
		{
			digit[2] = alpha[ 'W' - 'A'];
			alpha[ 'W' - 'A' ] -= digit[2] ;
			alpha[ 'T' - 'A' ] -= digit[2] ;
			alpha[ 'O' - 'A' ] -= digit[2] ;
		}
	
	
			//8
		
			
			if( alpha[ 'G' - 'A' ] > 0)
		{
			copy = digit[8] = alpha[ 'G' - 'A'];
			alpha[ 'E' - 'A' ] -= copy ;
			alpha[ 'I' - 'A' ] -= copy ;
			alpha[ 'G' - 'A' ] -= copy ;
			alpha[ 'H' - 'A' ] -= copy ;
			alpha[ 'T' - 'A' ] -= copy ;
			
		}
		
		
		//3
		
		if( alpha[ 'H' - 'A' ] > 0)
		{
			digit[3] = alpha[ 'H' - 'A'];
			alpha[ 'T' - 'A' ] -= digit[3] ;
			alpha[ 'H' - 'A' ] -= digit[3] ;
			alpha[ 'R' - 'A' ] -= digit[3] ;
			alpha[ 'E' - 'A' ] -= digit[3] ;
			alpha[ 'E' - 'A' ] -= digit[3] ;
		}
		
		//4
			if( alpha[ 'U' - 'A' ] > 0)
		{
			digit[4] = alpha[ 'U' - 'A'];
			alpha[ 'F' - 'A' ] -= digit[4] ;
			alpha[ 'O' - 'A' ] -= digit[4] ;
			alpha[ 'U' - 'A' ] -= digit[4] ;
			alpha[ 'R' - 'A' ] -= digit[4] ;
		
		}	
		
		
		//6
		
			if( alpha[ 'X' - 'A' ] > 0)
		{
			copy = digit[6] = alpha[ 'X' - 'A'];
			alpha[ 'S' - 'A' ] -= copy ;
			alpha[ 'I' - 'A' ] -= copy ;
			alpha[ 'X' - 'A' ] -= copy ;
			
		}	
		
		
	
		
		//1
		
			if( alpha[ 'O' - 'A' ] > 0)
		{
			copy = digit[1] = alpha[ 'O' - 'A'];
			alpha[ 'O' - 'A' ] -= copy ;
			alpha[ 'N' - 'A' ] -= copy ;
			alpha[ 'E' - 'A' ] -= copy ;
			
		}
		
		//5
		
			if( alpha[ 'F' - 'A' ] > 0)
		{
			copy = digit[5] = alpha[ 'F' - 'A'];
			alpha[ 'F' - 'A' ] -= copy ;
			alpha[ 'I' - 'A' ] -= copy ;
			alpha[ 'V' - 'A' ] -= copy ;
			alpha[ 'E' - 'A' ] -= copy ;
		}
		
		//7
		
			if( alpha[ 'V' - 'A' ] > 0)
		{
			copy = digit[7] = alpha[ 'V' - 'A'];
			alpha[ 'S' - 'A' ] -= copy ;
			alpha[ 'E' - 'A' ] -= copy ;
			alpha[ 'V' - 'A' ] -= copy ;
			alpha[ 'N' - 'A' ] -= copy ;
			alpha[ 'E' - 'A' ] -= copy ;
		}
		
		//9
		
		
		
			if( alpha[ 'I' - 'A' ] > 0)
		{
			copy = digit[9] = alpha[ 'I' - 'A'];
			alpha[ 'N' - 'A' ] -= copy ;
			alpha[ 'I' - 'A' ] -= copy ;
			alpha[ 'N' - 'A' ] -= copy ;
			alpha[ 'E' - 'A' ] -= copy ;
		}
		
		
		
			
    	cout << "Case #" << i << ": " ;
		for(int k=0; k<10; k++)
		{
			while(digit[k]>0)
			{
				cout<<k;
				digit[k]--;
			}
		}
		
		
		cout<<"\n";
    }
}
