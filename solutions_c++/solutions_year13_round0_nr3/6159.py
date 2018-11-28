

#include <stdio.h>
#include <iostream>

using namespace std;


FILE *fp;


char temp;


int main()
{
	int t;

	cin >> t;

	int i = 1;
	
	for(; i <= t; i++)
	{
		int A,B,j,k,l,m,n;
		
		int result = 0;
		
		cin >> A >> B;
		
		if(A <= 1)
		{
			if(B < 4)
			{
				result = 1;
			}
			else if(B < 9)
			{
				result = 2;
			}
			else if(B < 121)
			{
				result = 3;
			}
			else if(B < 484)
			{
				result = 4;
			}
			else
			{
				result = 5;
			}
		}
		
		else if(A <= 4)
		{
			if(B < 4)
			{
				result = 0;
			}			
			else if(B < 9)
			{
				result = 1;
			}
			else if(B < 121)
			{
				result = 2;
			}
			else if(B < 484)
			{
				result = 3;
			}
			else
			{
				result = 4;
			}
		}
		
		else if(A <= 9)
		{
			if(B < 9)
			{
				result = 0;
			}			
			else if(B < 121)
			{
				result = 1;
			}
			else if(B < 484)
			{
				result = 2;
			}
			else
			{
				result = 3;
			}
		}
		
		else if(A <= 121)
		{
			if(B < 121)
			{
				result = 0;
			}			
			else if(B < 484)
			{
				result = 1;
			}
			else
			{
				result = 2;
			}
		}
		else if(A <= 484)
		{
			if(B < 484)
			{
				result = 0;
			}		
			else
			{
				result = 1;
			}
		}
		else
		{
			result = 0;
		}
		
		
		cout << "Case #" << i << ": " << result << endl;
				//<< "A: " << A << "\n B: " << B << endl<< endl;
	
	}
	
	
	return 0;
}



