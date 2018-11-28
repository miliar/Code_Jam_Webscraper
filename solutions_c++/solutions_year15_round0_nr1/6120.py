#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	ifstream in;
	in.open("A-large.in");
	ofstream out;
	out.open("result1.out");
	int count;
	int max;
	char *test;
	in >> count;
	int shy = 0;
	int friends=0;
	for (int i = 0; i < count; i++)
	{
		shy = 0;
		friends = 0;
		in >> max;
		test = new char[max + 1];
		in >> test;
		for (int i = 0; i <=max; i++)
		{
			if (shy < i)
			{
				friends++;
				shy++;
			}
			if (test[i] != '0' && shy >= i)
			{
				shy = shy + (test[i] - 48);
			}
		}
		out << "Case #" << i + 1 << ": " << friends << "\n";
	}
	in.close();
	out.close();
	return 0;
}