#include <iostream>
#include <conio.h>
#include <cmath>
#include <fstream>
int  pal_check(int x)
{
	int rev = 0,rem, x1 = x;

	while(x)
	{
		rem = x%10;
		rev = rev*10 + rem;
		x = x/10;
	}
	if(x1 == rev)
		return 1;
	else
		return 0;
}

int main()
{
	int T, A, B, a, b, count, c = 0; 
	std::ifstream in;
	std::ofstream out;
	in.open("C-small-attempt0.in");
	out.open("C-small-attempt0.out");
	if(in.is_open() && out.is_open())
	{
		in>>T;
			while(T--)
			{
				c++;
				in>>A;
				in>>B;
				count = 0;
				a = sqrt(double(A));
				if(A != a*a)
					a+=1;
				b = sqrt(double(B));
				for(int i = a; i <= b; i++)
				{
					if(pal_check(i))
						if(pal_check(i*i))
							count++;
				}
				out<<"Case #"<<c<<": "<<count<<"\n";
			}
	}
	getch();

}


