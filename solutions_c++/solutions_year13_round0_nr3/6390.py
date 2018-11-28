#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;


int palin ( _int64 i )
{
	_int64 x=i, neww=0;
	while ( x>0 )
	{
		neww*=10;
		neww+=x%10;
		x/=10;
	}
	if ( neww==i ) return 1;
	else return 0;
}
		

int main()
{

	ofstream out ("Output.txt");
	int testcases;
	cin>>testcases;
	int q=1;
	while ( testcases-- )
	{
	_int64 A, B, num;
	cin>>A>>B;
	int count=0;
	int start, end;
	start=sqrt((double)A);
	if ( start*start!=A ) start++;
	end=sqrt((double)B);
	for ( num=start; num<=end; num++ )
	{
		if ( palin(num)==1 )
		{
			if ( palin(num*num)==1 ) count++;
		}
	}
	out<<"Case #"<<q<<": "<<count<<endl;
	q++;
	}
	return 0;
}