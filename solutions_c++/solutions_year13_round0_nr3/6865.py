#include<iostream>
#include<stdlib.h>
#include<math.h>
using namespace std ;
int Arry[8] ;
bool pal(unsigned long long int n)
{
	int j = 1 ;
	unsigned long long int i ;
	i = n ;
	while(i)
	{	
		
		Arry[j] = (int)i%10 ;
		i = i/10 ;
		j++ ;		
	}
	j-- ;
//	for(i=0 ; i<=8 ;i++)
//		cout << Arry[i] << endl ;
	for(i=1 ; i<=j/2 ;i++)
		if(Arry[i]!=Arry[j-(i-1)])
			return false ;
	return true ;
	
}
bool val(int n)
{
	if(pal(n))
		if(pal(n*n))
			return true ;
	return false ;
}
int main()
{
	bool result ;
	double A,B ;
	int a,b ;
	int count ;
	int T ;
	int x,i ;
	cin >> T  ;
	i = 1 ;
	while(T--)
	{
		count = 0 ;
		cin >> A  ;
		cin >> B  ;
		if(A != B)
		{
			a = (int)sqrt(A) ;
			b = (int)sqrt(B) ;
			if (a*a != A)
				a = a + 1 ;
			for(x=b ;x>=a ;x--)
				if(val(x))
				{
					count++ ;
				}

			cout << "Case #"<< i << ": " << count << endl ;
		}else
		{
			a = (int)sqrt(A) ;
			if (a*a != A)
				cout << "Case #"<< i << ": " << 0 << endl ;
			else
			{
				if(val(a))
					cout << "Case #"<< i << ": " << 1 << endl ;
				else
					cout << "Case #"<< i << ": " << 0 << endl ;
			}
		}
		i++ ;
	}
	return 0 ;
}