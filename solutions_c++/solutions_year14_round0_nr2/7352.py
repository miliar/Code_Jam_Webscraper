#include<iostream>
#include<string>
#include<cmath>
#include<vector>
#include<cstdio>

using namespace std ;

double c , f , x ;

double cook(double sum) ;

int main()
{
	int t , counter = 0 ;
	cin>>t ;
	while(t--)
	{
		cin>>c>>f>>x ;
		//sum = 2.00 ;
	/*	temp1 = x/sum ;
		temp2 = (c/sum) + (x/(sum+f)) ;
		while(temp1 >= temp2)
		{
			temp1 = x/sum ;
			temp2 = (c/sum) + (x/(sum+f)) ;
			answer += (c/sum) ;
			//cout<<c/sum<<endl ;
			sum += f ;
		}
		answer += (x/(sum)) ;
	*/	++counter ;
		cout<<"Case #"<<counter<<": " ;
		printf("%.7lf\n",cook(2.00)) ;
	}
	return 0 ;
}
		
double cook(double sum)
{
	double answer = 0 ;
	double temp1 , temp2 ;
	temp1 = x/sum ;
	temp2 = c/sum + x/(sum+f) ;
	if(temp1 >= temp2)
	{
		answer += c/sum + cook(sum + f) ;
	}
	else
	{
		return x/sum ;
	}
	return answer ;
}
