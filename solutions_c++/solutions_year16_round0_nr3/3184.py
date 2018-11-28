#include"iostream"
#include"vector"
#include"unordered_set"
#include"string"
#include"cmath"
using namespace std;
unsigned long long GetVal(const vector<bool> &DigSet, const int Base)
{
	const int Size = DigSet.size();

	unsigned long long Val = 0;
	unsigned long long Pow = 1;
	for (int seek = Size - 1; seek >= 0; seek = seek - 1)
	{
		Val = Val + (DigSet[seek] ? Pow : 0);
		Pow = Pow * Base;
	}

	return Val;
}
unsigned long long IsPrime(unsigned long long Val)
{
	unsigned long long End = ::sqrt(Val);

	for (unsigned long long seek = 2; seek <= End; seek = seek + 1)
	{
		if ((Val % seek) == 0)
		{
			return seek;
		}
	}

	return 0;
}
void GenerateDigits(vector<bool> DigSet, int CurrentLength, const int Number, int &CurrentNumber, bool bWriteOne)
{
	if (CurrentNumber == Number){ return; }

	if ((CurrentLength + 1) < DigSet.size())
	{
		DigSet[CurrentLength] = bWriteOne;
		GenerateDigits(DigSet, CurrentLength + 1, Number, CurrentNumber, false);

		DigSet[CurrentLength] = bWriteOne;
		GenerateDigits(DigSet, CurrentLength + 1, Number, CurrentNumber, true);

		return;
	}

	if (!bWriteOne){ return; }

	DigSet.back() = true;

	unsigned long long DivArray[9];

	for (int seek = 2; seek <= 10; seek = seek + 1)
	{
		unsigned long long Val = GetVal(DigSet, seek);

		DivArray[seek - 2] = IsPrime(Val);
		if (DivArray[seek - 2] == 0)
		{
			return;
		}
	}

	for (const auto &d : DigSet)
	{
		::cout << (d ? 1 : 0);
	}

	for (int seek = 0; seek < 9; seek = seek + 1)
	{
		::cout << " " << DivArray[seek];
	}

	::cout << endl;

	CurrentNumber = CurrentNumber + 1;
}
int main()
{
	int Times = 0;
	::cin >> Times;

	for (int seek = 0; seek < Times; seek = seek + 1)
	{
		int Length;
		int Number;
		::cin >> Length >> Number;

		::cout << "Case #" << seek + 1 << ":"<<endl;
		
		int CurrentNumber = 0;
		vector<bool> DigSet(Length, true);

		GenerateDigits(DigSet, 0, Number, CurrentNumber, true);
	}

	//::system("pause");

	return 0;
}