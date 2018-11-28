#include<iostream>
#include<cstdio>
using namespace std;

#include<algorithm>
#include<vector>
#include<cmath>
#include<limits.h>

typedef long long ll;
typedef vector<int> vi;
typedef vi::iterator vit;

#define sz(c) (int)( (c).size() ) 

inline double calc(double c , double f, double x)
{
	double time = 0 ;
	double current_rate = 2;
	double time_to_next;
	
	if( x <= c ) 
		{
			time += x/current_rate;
			return time;
		}
		
	while( true )
	{
		
	time += c/current_rate;
	if(  (x-c)/current_rate <= x/(current_rate + f) )
		{
			time += (x-c)/current_rate;
			return time;
		} 	
		
	else
	{
		current_rate += f;
	}	
		
	}
}

int main()
{
	int t;
	double c,f,x;
	cin>>t;
	for( int z = 1 ; z <= t ; ++z)
	{
		cout<<"Case #"<<z<<": ";
		
		cin>>c>>f>>x;
		
		printf("%.8lf\n",calc(c,f,x));
		
	}
	
	return 0 ;
}
