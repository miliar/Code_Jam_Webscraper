#include<iostream>
#include<fstream>

using namespace std;



int main()
{
	ofstream out ( "A.txt" );
	unsigned _int64 r, check, i, a, b, t;
	unsigned _int64 arr[99999];
	a=1; b=0; r=10000000000000; t=2000000000000000000;
	for ( i=0; ; i++ )
		{
			arr[i]=check=(a*a)+(2*a*r)-(b*b)-(2*b*r);

			if ( check> t ) break;
			t-=check;
			a+=2; b+=2;
		}
	int testcases;
	cin>>testcases;
	int cases=1;
	while ( testcases-- )
	{
		a=1; b=0;
		cin>>r>>t;
		int boo=0;
		for ( i=0; ; i++ )
		{
			if ( r+a >10000000000000 ) { boo=1; break; }
			check=(a*a)+(2*a*r)-(b*b)-(2*b*r);


			if ( check> t ) break;
			t-=check;
			a+=2; b+=2;
		}
		if ( boo==0 ) out<<"Case #"<<cases<<": "<<i<<endl;
		else
		{
		long count=i;
		for ( i=0; ; i++ )
		{
			check=arr[i];

			if ( check> t ) break;
			t-=check;
		}
		out<<"Case #"<<cases<<": "<<count+i<<endl;
		}
		cases++;
	}






	return 0;
}