#include<cmath>
#include<fstream>
using namespace std;

bool isPal(int);

ofstream out("out.txt");

int *ptr = new int[101];

int main()
{
	ifstream in("in.txt");
	int N, A, B, a, b, count;
	double cast = 1.0;

	in >> N;

	for(int i = 0; i < N; i++)
	{
		count = 0;
		
		in >> A >> B;
		
		a = (int)(sqrt(A * cast)+.000000000000000000000000000000000000000000001);
		if(A != a*a)
			a++;		//fricking float math

		b = (int)sqrt(B * cast);

		for(int j = a; j <= b; j++)
		{
			if(isPal(j))
				if(isPal(j*j)){
					count ++;
				}
		}
		out << "Case #" << i+1 << ": " << count << endl;
	}
//	out << "isPal? : " << isPal(12346321) << endl;
}

bool isPal(int n)
{
	int rem = n, nth;
	int pos = 0;

//	out << endl << endl;
	
	while(rem > 0)
	//populates *ptr w/ digits of the int
	{
		nth = rem % 10;
		rem = rem / 10;
		*(ptr+pos) = nth;
//		out << *(ptr+pos);
		pos ++;	
	}

//	out << endl << endl;

//	out << pos << endl;

	for(int i = 0; i < pos/2; i++)
	//checks 1st digit against last digit... etc.
	{
//		out << "1: " << *(ptr+i) << "  2: " << *(ptr+pos-i-1) << endl;
		if(*(ptr+i) != *(ptr+pos-i-1))
			return false;
	}
	return true;
}