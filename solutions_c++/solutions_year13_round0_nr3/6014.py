#include <fstream>
#include <cmath>
#include <string>
using namespace std;

bool palindrom(int x)
{
	int temp = x;
	int reverse = 0;
	int rem;
	while (temp!=0)
	{
		rem = temp%10;
		reverse = reverse*10+rem;
		temp = temp/10;
	}
	if (reverse == x)
		return true;
	else
		return false;
}
int main()
{
	int T,A,B;
	int y;
	double sq;
	bool not_int;
	ifstream in1;
	in1.open("C-small-attempt0.in");
	ofstream out;
	out.open("C-small-attempt0.out");
	in1 >> T;
	int count;
	for (int i=0;i<T;i++)
	{
		count = 0;
		in1 >> A >> B;
		for (int k=A; k<B+1;k++)
		{
			sq = sqrt(k);
			y = (int)sq;
			if (sq > y)
				not_int = 1;
			else
				not_int = 0;
			if (not_int == 0 && palindrom(k) && palindrom(y))
			{
				count++;
			}
		}
		out << "Case #" << i+1 << ": " << count << endl;
		
	}
	in1.close();
	out.close();
}
