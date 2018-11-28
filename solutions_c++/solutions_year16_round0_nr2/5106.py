#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>
#include <cstring>
#include <map>
#include <bitset>

using namespace std;

int flip(int n,int bits)
{
	return (~n & ( (int)pow(2,bits) - 1 ));
}

int makeAll(int n,int bits,int to=1)
{
	if(n==0)
		return (to);
	if(n==1)
	{
		if(bits==1)
		{
			if(to==1)
			{
				return 0;
			}
			else
			{
				return 1;
			}
		}
		else
		{
			if(to==1)
			{
				return 1;
			}
			else
			{
				return 2;
			}
		}
	}
	if(to==1)
	{
		if(n&1==1)
		{
			return makeAll(n>>1,bits-1);
		}
		else
		{
			return makeAll(n>>1,bits-1,0)+1;
		}
	}
	else
	{
		if(n&1==1)
		{
			return makeAll(n>>1,bits-1)+1;
		}
		else
		{
			return makeAll(n>>1,bits-1,0);
		}
	}
}

void getNumsBin(int &n,int &bits)
{
	char a[11];
	cin>>a;
	bits=strlen(a);
	n=0;
	for(int i=0 ; i<bits ; i++ )
		if(a[i]=='+')
			n = (n<<1) + 1;
		else
			n = n<<1;
}

int main()
{
	int count;
	cin>>count;
	int i=1;
	while(i<=count)
	{
		int n;
		int bits;
		getNumsBin(n,bits);
		cout<<"Case #"<<i++<<": "<<makeAll(n,bits)<<"\n";
	}

}