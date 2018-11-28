#include <fstream>
#include <string>

using namespace std;

int main ()
{
	ifstream fin ("B.in");
	ofstream fout ("B.out");
	int CaseCount;
	fin >> CaseCount;
	for (int CaseNum = 1; CaseNum <= CaseCount; CaseNum++)
	{
		string Cake;
		int DifferCount = 0;
		fin >> Cake;
		for (int i = 0; i < Cake.size () - 1; i++)
			if (Cake[i] != Cake[i + 1]) DifferCount++;
		fout << "Case #" << CaseNum << ": ";
		if (Cake[Cake.size() - 1] == '+') 
			fout << DifferCount << endl;
		else
			fout << DifferCount + 1 << endl;
	}
}

