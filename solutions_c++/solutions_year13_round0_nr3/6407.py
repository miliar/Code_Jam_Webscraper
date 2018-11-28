#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;

bool palindrome(unsigned int n)
{
	int m = n, n2=0;
	while(m > 0)
	{
		n2 = n2*10+m%10;
		m = m/10;
	}
	if(n == n2)
		return true;
	else
		return false;
}

bool whole(float f)
{
	int n = (int)f;
	return f-n == 0;
		
}

bool sqr(int n)
{
	return  whole(sqrt(n)) ;
}


bool fairNsqr(int n)
{
	if(sqr(n))
	{
		return palindrome(n) && palindrome(sqrt(n));
	}
}

int main()
{
	int t;
	
	//ifstream in("input.txt");
	ifstream in("C-small-attempt0.in");
	ofstream out("output.txt");
	
	in>>t;
	for(int x = 1; x<=t; x++)
	{
		int count = 0;
		int a,b;
		in>>a>>b;	
		for(int i = a; i<=b; i++)
		{
			if(fairNsqr(i))
				count++;
		}
		out<<"Case #"<<x<<": "<<count<<endl;
	}
	out.close();
	return 0;
}

