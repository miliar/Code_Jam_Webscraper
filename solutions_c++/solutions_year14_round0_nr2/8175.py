#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
	int ttt;
	cin>>ttt;
	long double C, F, X;
	for( int tt = 1; tt <= ttt; tt++ )
	{
	  cout<<"Case #"<<tt<<": ";
	  cin>>C>>F>>X;
	  long double rate = 2; 
	  long double ans = X/rate,temp, prev_sum = 0;
	  while( 1 ) 
	  {
		prev_sum = prev_sum + C/rate;
		rate = rate + F;
	    temp = prev_sum + X/rate;
		if( temp < ans ) 
			ans = temp;
		else
			break;
	  }
	  printf("%.7f", ans );
	  cout<<endl;
	}
}