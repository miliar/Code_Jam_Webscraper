#include<iostream>
#include<fstream>

using namespace std;

long long NoOfInvites ( long long n , char* list )
{
	long long invites = 0 , sum =0;
	for ( long long i=0 ; i<n+1 ; ++i )
	{
		if ( list[i]=='0' )
			continue;
		else if (i<=sum)
			sum+=(list[i]-48);
		else if (i>sum)
		{
			invites+= (i-sum);
			sum+= ((i-sum)+(list[i]-48));
		}
	}
	return invites;
}

int main()
{
	ifstream ip;
	 ip.open ("A-large.in");
	ofstream op;
	op.open ("shySolution.txt");

	long long cases;
	ip>>cases;

	long long* tests = new long long[cases];
	char** shyList = new char* [cases];

	for ( long long i=0 ; i<cases ; ++i )
	{
		ip>> tests[i];
		shyList[i] = new char[tests[i]+1];
		ip>> shyList[i];
	}
	for ( long long i=0 ; i<cases ; ++i )
	{
		op<<"Case #"<<i+1<<": ";
		long long solution = NoOfInvites(tests[i],shyList[i]);
		op<<solution<<endl;
	}
	return 0;
}
