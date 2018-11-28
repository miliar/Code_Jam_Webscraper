#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

//#define OUT cout
#define OUT output

bool hasAllDigits(bool ns[]);
void updatestatus(bool ns[], long long n);

int main()
{
	ifstream input("file.in");
	ofstream output("file.out");

	int tc;

	input>>tc;

	for(int c=1; c<=tc; ++c)
	{
		long long n;
		int i=1;
		bool ns[]={0,0,0,0,0,0,0,0,0,0};

		input>>n;

		OUT << "Case #" << c << ": ";
		
		if(n==0) 
			OUT << "INSOMNIA";
		else
		{
			long long tmp=n;
			while(1)
			{
				updatestatus(ns, n);

				if(hasAllDigits(ns) || n<=0)
				break;

				n = tmp * ++i;
			}
			if(n>0)
				OUT << n;
			else
				OUT << "INSOMNIA";
		}


		if(c<tc) OUT << endl;
	}
	
//	getchar();
	return 0;
}
void updatestatus(bool ns[], long long n)
{
	while(n%10 == 0)
	{
		ns[0] = true;
		n /= 10;
	}
	while(n>9)
	{
		ns[n%10] = true;
		n /= 10;
	}
	ns[n] = true;
}
bool hasAllDigits(bool ns[])
{
	for(int i=0; i<10; ++i)
		if(!ns[i]) return false;
	return true;
}