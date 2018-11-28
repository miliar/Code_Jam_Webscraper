#include<fstream>

using namespace std;
int main()
{
	ifstream in("A-large.in");
	ofstream out("output.txt");
	long long n;
	long long k = 0;
	long long t;
	in >> t;

	for (int j = 0; j < t; j++)
	{
		in >> n;
		long long z = n;
		if (n != 0)
		{
			bool*a = new bool[n];
			for (int i = 0; i < 10; i++)
			{
				a[i] = false;
			}
			long long i = 0;
			while (!a[0] || !a[1] ||!a[2] || !a[3] || !a[4] ||!a[5] || !a[6] ||!a[7] || !a[8] || !a[9])
			{
				long long b = n;
				while (b != 0)
				{
					a[b % 10] = true;
					b = b / 10;
				}
				i++;
				k = n;
				n = z*i;

			}
			out << "Case #" << j + 1 << ':' <<' '<< k<<endl;
		}
		else
		{
			out << "Case #" << j + 1 <<':'<<" INSOMNIA"<<endl;
		}
	}
	in.close();
	out.close();
	return 0;
}