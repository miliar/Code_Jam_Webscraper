#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <math.h>
using namespace std;
typedef long long LL;

int coincounter = 0, bin=0, nonPrime = 1;
LL nontrivallist[9];


int dictobin(int n)
{
    if(n/2!=0) dictobin(n/2);
    bin = bin*10 + n%2;
}

int primecker(long long num , int bs)   // Returns '0' if its prime, and a '1' if its not prime.

{
   int isprime = 0;
	for(LL i = 2; i <= sqrt(num); i ++)
	{

		if((num% i) == 0)
		{
		    nontrivallist[bs-2] = i;
			isprime = 1;
			break;
		}
	}

	return isprime;
}

void conveter(int i, LL nm)
{
     long long  dec = 0, rem, num, base = 1;
     num = nm;
    while (num > 0)
    {
        rem = num % 10;
        dec = dec + rem * base;
        base = base * i;
        num = num / 10;
    }

 nonPrime =primecker(dec,i);

}

void jamcoincker(LL nm)
{
    for(int i=2; i<11;i++)
    {
        conveter( i, nm );
        if(nonPrime == 0) break;
    }
   if(nonPrime == 1)
   {
       coincounter++;
       cout<<nm;
       for(int j = 0; j<9;j++)
       {
           cout<<" "<<nontrivallist[j];
       }
       cout<<"\n";
   }

     nonPrime = 1;

}


main() {

  FILE *fin = freopen("C-small-attempt4.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("C-small-attempt4.out", "w", stdout);
	int T,N ,J;
	LL number;
	  //cout<<number;
	cin >> T;

	for(int t = 1; t <= T; t++){

		cin>>N;
		cin>>J;
		cout << "Case #" << t << ":\n";
        for(int i=0; coincounter<J; i++)
        {
            dictobin(i);
            number = 1000000000000000 + bin*10 +1 ;
            //cout<<number<<"\n";
            bin = 0;
            jamcoincker(number);
           // cout<<number<<"\n";
           // cout<<number;
          //  break;
        }

		//cout << "Case #" << t << ": ";
//		cout << add << endl;
	}
	exit(0);
}
