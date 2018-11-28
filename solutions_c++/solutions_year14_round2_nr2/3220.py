#include<iostream.h>
#include<conio.h>
#include<string.h>
#include<fstream.h>
#include<math.h>
void tobin(int string[], int);
int todec(int string[]);
int h;
void main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");
	int cases;
	in>>cases;
	for (int i = 0; i<cases; ++i)
	{
		int count=0;
		int a, b, q,h1,h2;
		int b1[10], b2[10], b3[10];
		int number;
		in>>a;
		in>>b;
		in>>q;
		for (int y = 0; y<a; ++y)
		{
			for (int z = 0; z<b; ++z)
			{
				tobin(b1, y);
				h1 = h;
				tobin(b2, z);
				h2 = h;
				if (h2 <= h1)
				{
					h = h2;
				}
				else
					h = h1;
				for (int i = 0; i<10; ++i)
				{
					b3[i] = 0;
				}
				for (i = 9; i>=h; --i)
				{
					b3[i] = (b2[i] && b1[i]);
				}
				number = todec(b3);
				if (number<q) ++count;

			}
		}
		out<<"Case #"<<i+1<<": "<<count<<"\n";
	}
	in.close();
	out.close();
	cout << "Success";
}

void tobin(int string[], int inte)
{
	int k = 10;
	h = 9;
	for (int i = 0; i<10; ++i)
	{
		string[i] = 0;
	}
	while (inte>0)
	{
		string[k - 1] = inte % 2;
		inte = inte / 2;
		--k;
		h = k;
	}
}
int todec(int string[])
{
	double s = 0;
	for (int i = 0; i<10; ++i)
	{
		s += string[9- i] * pow(2,i);
		
	}
	return s;
}

