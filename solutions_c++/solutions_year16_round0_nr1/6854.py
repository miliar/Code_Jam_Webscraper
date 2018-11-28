#include <fstream>
#include <iostream>

using namespace std;

int main()
{
	long n;
	ifstream inp;
	inp.open("input.txt");
	ofstream out;
	out.open("output.txt");
	int testcase;
	inp>>testcase;
	
	int j = 0;
	while (j<testcase)
	{
		j++;
		inp>>n;
		
		out<<"Case #"<<j<<": ";
		if (n==0)
			out<<"INSOMNIA";
		long i = 1;
		int k;
		long last = 0;
		int bin[10] = {0};
		while (1)
		{
			
			last = n * i;
			if (last == 0)
				break;
			long m = last;
			int a;
			while (m>0)
			{
				a = m % 10;
				bin[a] = 1;
				m = m / 10;
			}
			int sum = 1;

			for (k=0;k<10;k++)
				if (bin[k] == 0)
					sum = 0;
			if (sum == 1)
			{
				out<<last;
				break;
			}
				
			i++;
		}
		
		
		
		out<<endl;
	}
	
	inp.close();
	return 0;
}
