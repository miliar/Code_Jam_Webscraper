#include <iostream>
#include <cstdio>
#include <vector>
#include <math.h>
using namespace std;
/*bool check(long long int  x)
{
	vector<int> a;
	while(x>0)
	{
		a.push_back(x%10);
		x=x/10;
	}

	for(int i=0, j=a.size()-1; i<a.size()/2; i++, j--)
	{
		if(a.at(i)!=a.at(j))
		{
			return false;
		}
	}
	
	return true;
	}*/

bool check(long long int x)
{
	
	long long ans=0, y=x;
	while(x>0)
	{
	ans=ans*10+(x%10);
	x/=10;
}
return ans==y;
}

int main()
{
	long int T;
	scanf("%li", &T);
	long long int arr[]=
{1
 ,2
,3
 ,11
 ,22
 ,101
 ,111
 ,121
 ,202
 ,212
 ,1001
 ,1111
 ,2002
 ,10001
 ,10101
 ,10201
 ,11011
 ,11111
 ,11211
 ,20002
 ,20102
 ,100001
 ,101101
 ,110011
 ,111111
 ,200002
 ,1000001
 ,1001001
 ,1002001
 ,1010101
 ,1011101
 ,1012101
 ,1100011
 ,1101011
 ,1102011
 ,1110111
 ,1111111
 ,2000002
 ,2001002
 ,10000001
 ,10011001
 ,10100101
 ,10111101
 ,11000011
 ,11011011
 ,11100111
 ,11111111
 ,20000002};
	for(int k=1; k<=T; k++)
	{
		long long int p, q;
		scanf("%lli", &p);
		scanf("%lli", &q);
		int count=0;
		for(int i=0; i<48; i++)
		{
			if(arr[i]*arr[i]<=q && arr[i]*arr[i]>=p)
			count++;

		}
		printf("%s", "Case #");
	printf("%i", k);
	printf("%s", ": ");
	printf("%i\n", count);
	}

		
	
	
			
	return 0;
}
