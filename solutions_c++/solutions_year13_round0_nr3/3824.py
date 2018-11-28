#include <stdio.h>
#include <string.h>
#include <cmath>

using namespace std;

int ipow(int a, int b);
int digit(int a, int b);
bool is_fair_and_square(int a, bool b, int c, int d);
int length(int x);


int main(int argc, char** argv){

		int N;
		scanf(" %d",&N);

		for(int i=1;i<=N;i++)
		{
			printf("Case #%d: ",i);
			int a, b;
			scanf(" %d %d", &a, &b);
			int c, d;

			c=static_cast<int>(sqrt(static_cast<double>(a)))-1;
			d=static_cast<int>(sqrt(static_cast<double>(b)))+1;

			// Generate palindromes between c and d

			// First find lengths of c and d
			int lenc=0, lend=0;
			
			lenc=length(c);
			lend=length(d);

			int lower, upper;
			int count=0;

			lower=ipow(10, (lenc-1)/2);
			upper=ipow(10, (lend+1)/2);


			for(int x=lower;x<=upper;x++)
			{
				if(is_fair_and_square(x, true, a, b)) count++;
				if(is_fair_and_square(x, false, a, b)) count++;
			}

			printf("%d\n",count);

		}
		
		return 0;
}


bool is_fair_and_square(int x, bool odd_length, int a, int b)
{
// Generates a palindrome from x (of odd or even length depending on odd_length) and returns 
//true if its square is also a palindrome between a and b.

	int lenx;
	lenx=length(x);
	int p;


	if(odd_length)
	{
		p = x*(ipow(10, lenx-1));
	} else {
		p = x*(ipow(10, lenx));
	}

	if(odd_length)
	{
		x-=x%10;
		x=x/10;
		lenx-=1;
	}
	
	// Now reverse x and add it to p
	if(lenx>0)
	{
	for(int k=1;k<=lenx;k++)
	{
		p+=(digit(x,k)*ipow(10,lenx -k));
	}
	}

	// Now check for palindromes

	p=p*p;

	if(p<a || p>b) return false;

	int lenp = length(p);
	bool result=true;
	for(int r = 1;r<=lenp;r++)
	{
		if(digit(p,r)!=digit(p,(lenp+1)-r)) result=false;
	}

	return result;
}


int ipow(int a, int b)
{
	return static_cast<int>(pow(static_cast<double>(a), static_cast<double>(b)));
}

int digit(int x, int k)
{
	return (x%ipow(10,k))/ipow(10,k-1)%10;
}

int length(int x)
{
	int l=0;
	int j=1;
			
	while(j<=x)
	{
		j*=10;
		l++;
	}
	return l;
}