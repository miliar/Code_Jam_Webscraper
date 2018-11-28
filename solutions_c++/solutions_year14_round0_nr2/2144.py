#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

class CookiesFarm
{
private:
	float C, F, X;
	double Result;
public:
	void ReadInput(fstream &f)
	{
		f >> C >> F >> X;
	}
	void Solve()
	{
		double tNextFarm, tNextFarm_Goal, tGoal, tPreFarm;
		double newC = 2;
		tPreFarm = 0;
		while(1)
		{
			tGoal = tPreFarm + X / newC;
			tNextFarm = tPreFarm + C / newC;
			newC = newC + F;
			tNextFarm_Goal = tNextFarm + X / newC;
			if (tGoal < tNextFarm_Goal)
			{
				Result = tGoal;
				break;
			}
			else
			{
				tPreFarm = tNextFarm;
				continue;
			}
		}
	}
	void WriteOuput(int nTestCase, fstream &f)
	{
		f << "Case #" << nTestCase << ": " << fixed << setprecision(7) << Result << endl;
	}
};

int main(int argc, char **argv)
{
	fstream input, output;
	input.open(argv[1], ios::in);
	output.open(argv[2], ios::out);
	int nTestCase;
	input >> nTestCase;
	CookiesFarm CF;
	for (int i = 0; i < nTestCase; i++)
	{
		CF.ReadInput(input);
		CF.Solve();
		CF.WriteOuput(i + 1, output);
	}
	input.close();
	output.close();
	return 0;
}