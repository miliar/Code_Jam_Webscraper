#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>
#include <algorithm>
using namespace std;

class DWSolver
{
private:
	vector <double> Naomi, Ken;
	int Result1, Result2;
	static bool Comp(double i, double j)
	{
		return i > j;
	}
public:
	void ReadInput(fstream &f)
	{
		int size;
		f >> size;
		Naomi.resize(size);
		Ken.resize(size);
		for (int i = 0; i < size; i++)
			f >> Naomi[i];
		for (int i = 0; i < size; i++)
			f >> Ken[i];
		sort(Naomi.begin(), Naomi.end(), Comp);
		sort(Ken.begin(), Ken.end(), Comp);
	}
	void Solve()
	{
		vector<double> Naomi1, Ken1, Naomi2, Ken2;
		Naomi1 = Naomi2 = Naomi;
		Ken1 = Ken2 = Ken;
		int count = 0;
		while(Naomi1.size())
		{
			if (Ken1[0] > Naomi1[0])
			{
				count++;
				Ken1.erase(Ken1.begin());
				Naomi1.erase(Naomi1.begin());
			}
			else
			{
				Naomi1.erase(Naomi1.begin());
			}
		}
		Result2 = Ken.size() - count;
		count = 0;
		while(Ken2.size())
		{
			if (Ken2[0] < Naomi2[0])
			{
				count++;
				Ken2.erase(Ken2.begin());
				Naomi2.erase(Naomi2.begin());
			}
			else
			{
				Ken2.erase(Ken2.begin());
			}
		}
		Result1 = count;
	}
	void WriteOuput(int nTestCase, fstream &f)
	{
		f << "Case #" << nTestCase << ": " << Result1 << " " << Result2 << endl;
	}
};
int main(int argc, char **argv)
{
	fstream input, output;
	input.open(argv[1], ios::in);
	output.open(argv[2], ios::out);
	int nTestCase;
	input >> nTestCase;
	DWSolver MP;
	for (int i = 0; i < nTestCase; i++)
	{
		MP.ReadInput(input);
		MP.Solve();
		MP.WriteOuput(i + 1, output);
	}
	input.close();
	output.close();
	return 0;
}