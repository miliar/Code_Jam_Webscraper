#include <iostream>
#include <cstdio>
#include <vector>
#include <math.h>
using namespace std;
bool check(long int  x)
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
	}
	
bool issquare(long int x)
{
	return (sqrt(x)==floor(sqrt(x)));
}

int main()
{
	long int T;
	scanf("%li", &T);
	for(int k=1; k<=T; k++)
	{
		long int p, q;
		scanf("%li", &p);
		scanf("%li", &q);
		int count=0;
		for(long int i=p; i<=q; i++)
		{

			if(check(i) && issquare(i) && check(sqrt(i)))
			count++;

		}
		printf("%s", "Case #");
	printf("%i", k);
	printf("%s", ": ");
	printf("%i\n", count);
	}

		
	
	
			
	return 0;
}
