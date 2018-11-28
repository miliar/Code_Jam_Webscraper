// CDijkstra.cpp : Defines the entry point for the console application.
//

#include <tchar.h>
#include<iostream>
#include<fstream>
#include<vector>
#include <cassert>
#include<string>
#include <sstream>
#include<algorithm>

int M[3][3] = { { '1', 'k', 'j' }, { 'k', '1', 'i' }, { 'j', 'i', '1' } };
int sign[3][3] = { { -1, 1, -1 }, { -1, -1, 1 }, { 1, -1, -1 } };
char quat[4] = { '1', 'i', 'j', 'k' };

std::vector<int> ConvertSpacedInts(std::string& line)
{
	std::vector<int> integers;
	std::istringstream iss(line);
	int n;
	while (iss >> n)
	{
		integers.push_back(n);
	}
	return integers;
}


void mult(char a, char b, int Sa, int Sb, char& out, int& Sout)
{
	if (a == '1')
	{
		out = b;
		Sout = Sa*Sb;
		return;
	}
	if (b == '1')
	{
		out = a;
		Sout = Sa*Sb;
		return;
	}

	out = M[a - 'i'][b - 'i'];
	Sout = Sa*Sb* sign[a - 'i'][b - 'i'];;

}

void invert(char C, int S, char& CO, int& SO)
{
	if (C == '1')
	{
		CO = C;
		SO = S;
	}
	else
	{
		CO = C;
		SO = -S;
	}
}

unsigned int index(char a, int M)
{
	if (a == '1')
	{
		return (M == 1) ? 4 : 0;
	}

	return 1+ (a - 'i') + (M == 1) ? 4: 0;
}

void fromIndex(unsigned int i, char& a, int& sign)
{
	if (i <= 3)
	{
		a = quat[i];
		sign = -1;
	}
	else
	{
		a = quat[i-4];
		sign = 1;
	}
}



int search(int start, int end, char C, const std::vector<char>& Parray)
{
	char tot = '1';
	char totsign = 1;
	for (int n = start; n < end; n++)
	{

	}
	return 0;

}



std::string solve(std::vector<char>& LV, int L, int X)
{
	assert(LV.size() == L);

	int XMod4 = X % 4;

	std::vector<bool> LPs(8, false);

	std::vector<char> PLC(L);
	std::vector<int> PLS(L);

	char tot = '1';
	int totS = 1;

	for (int i = 0; i < L; i++)
	{
		mult(tot, LV[i], totS, 1, tot, totS);
		PLC[i] = tot;
		PLS[i] = totS;
		LPs[index(tot, totS)] = true;
		//std::cout << " result " << totS << " " << tot<<std::endl;
	}

	char PLCT = PLC[L - 1];
	int PLST = PLS[L - 1];

	char PT = '1';
	int PS = 1;

	for (int i = 0; i < XMod4; i++)
	{
		mult(PT, PLCT, PS, PLST, PT, PS);
	}

	if (PT != '1' || PS != -1)
	{
		return "NO";
	}

	char XFFacC = '1';
	int XFFacS = 1;

	char XBFacC = '1';
	int XBFacS = 1;

	char XBFacIC = '1';
	int XBFacIS = 1;

	char ISC = '1';
	int ISS = 1;

	char JSC = '1';
	int JSS = 1;

	char JSIC = '1';
	int JSIS = 1;

	for (unsigned int xF = 0; (xF < 4); xF++)
	{
		char XBFacC = '1';
		int XBFacS = 1;
		for (unsigned int xB = 0; (xB <4); xB++)
		{

			invert(XFFacC, XFFacS, ISC, ISS);
			mult(ISC, 'i', ISS, 1, ISC, ISS);
			if (xF + 1 > X) continue;
			for (int l = 0; l < L; l++)
			{

				if (PLC[l] == ISC&&PLS[l] == ISS)
				{
					char JSRC = '1';
					int JSRS = 1;

					for (int lR = l + 1; lR < L; lR++)
					{
						mult(JSRC, LV[lR], JSRS, 1, JSRC, JSRS);
						if ((JSRC == 'j') && (JSRS == 1))
						{
							return "YES";
						}

					}

					if (xF + 1 + xB + 1>X) continue;
					JSC = JSRC;
					JSS = JSRS;


					invert(JSC, JSS, JSIC, JSIS);

					mult(JSIC, 'j', JSIS, 1, JSIC, JSIS);

					invert(XBFacC, XBFacS, XBFacIC, XBFacIS);

					mult(XBFacIC, JSIC, XBFacIS, JSIS, JSC, JSS);

					for (int l1 = 0; l1 < L; l1++)
					{
						if (PLC[l1] == JSC&&PLS[l1] == JSS)
						{
							return "YES";
						}

					}

				}
			}



			mult(XBFacC, PLCT, XBFacS, PLST, XBFacC, XBFacS);
		}
		mult(XFFacC, PLCT, XFFacS, PLST, XFFacC, XFFacS);
	}

	return "NO";
}

void parsecase(std::ifstream& inputfile, int& L, int& X, std::string& ijks)
{
	std::string line;
	std::getline(inputfile, line);
	std::vector<int> LX = ConvertSpacedInts(line);
	L = LX[0];
	X = LX[1];
	assert(LX.size() == 2);
	std::getline(inputfile, ijks);
	assert(ijks.size() == L);
}


int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream inputfile("C-small-attempt2.in");
	//std::ifstream inputfile("test.txt");
	std::string line;
	std::getline(inputfile, line);
	int nNumbCases = ConvertSpacedInts(line)[0];
	int L;
	int X;
	std::string ijks;
	std::ofstream output_test("C-small-output.txt");
	//std::ofstream output_test("test-output.txt");
	for (int CI = 0; CI < nNumbCases; CI++)
	{
		parsecase(inputfile, L, X, ijks);
		std::vector<char> ijksVec(ijks.begin(), ijks.end());
		std::string output = solve(ijksVec, L, X);
		output_test << "Case #" << (CI + 1) << ": " << output << std::endl;
	}


	return 0;
}

