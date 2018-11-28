#include<iostream>
#include<fstream>
#include <set>

using namespace std;


void isertInHash(long long n, set<long long> &hash)
{
    while (n != 0 ) 
	{
          hash.insert (n % 10 );
          n = n / 10 ;
    }
}

int main ()
{
	ifstream ifile("A-large.in");
	ofstream ofile;
	ofile.open("A-large.out");
	long long t, cases = 0, n;
	ifile>>t;
	while(t--)
	{
		ifile>>n;
		set<long long> hash;
        if (n == 0 ) 
		{
            //cout<<"Case #"<< ++cases<< ": Insomnia\n";
            ofile<<"Case #"<<++cases<<": Insomnia"<<endl;
        } 
		else 
		{
            long long k = 1 ;
            while (hash.size() != 10 ) 
			{
				isertInHash(n * k, hash);
                k ++ ;
            }
            //cout<<"Case #"<< ++cases<<": "<< n * (k - 1 )<<endl;
            ofile<<"Case #"<<++cases<<": "<<n * (k - 1 )<<endl;
        }
    }
}

