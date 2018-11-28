#include<iostream>
#include<math.h>
#include<conio.h>
using namespace std;

int Reverse(int x)
{
	int ReturnValue=0;
	int  Digit;

	do{	
	Digit=x%10; 
	ReturnValue=ReturnValue*10+Digit;
	x/=10;
	} while(x>0);

	return ReturnValue;
}
bool IsPalindromes(int x)
{
	return (x==Reverse(x));
}
bool CheakSqrt(int x)
{
	int root = (int)(floor(sqrt(x)));
	return ( root*root )== x ;
}
void main()
{
	freopen ("Input.txt","r",stdin);
	freopen ("Output.txt","w",stdout);
	
	int T;
	int A,B;

	cin>>T;
	if(1 <= T <= 100)
	{
	for (int x = 0; x < T; x++)
	{
		int Count=0;
		
		cin>>A>>B;
		if(1 <= A <= B <= 1000)
		{
		for (int i = A; i <= B ; i++)
		{
			if( CheakSqrt(i) && IsPalindromes( sqrt(i) ) && IsPalindromes(i)  )
			{ 
				Count++; 
			}
		}
		}
		
		cout<<"Case #"<<x+1<<": "<<Count<<endl;
	}
	}
	
	getch();
}