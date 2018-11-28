#include"iostream"
#include"unordered_set"
#include"string"
using namespace std;
int SlovePanCake(string s, int start, int end, bool bToPos = true)
{
	int Size = end - start;

	char Target = bToPos ? '+' : '-';

	if (Size == 0){ return 0; }

	int PCount = 0;
	int NCount = 0;

	//Debug
	/*::cout << "[";
	for (int seek = start; seek < end; seek = seek + 1)
	{
		::cout << s[seek];
	}
	::cout << "]";*/


	for (int seek = start; seek < end; seek = seek + 1)
	{
		PCount = PCount + (s[seek] == Target ? 1 : 0);
		NCount = NCount + (s[seek] != Target ? 1 : 0);
	}

	if (PCount == Size){ /*::cout << " : 0\r\n";//*/ return 0; }
	if (NCount == Size){ /*::cout << " : 1\r\n";//*/ return 1; }

	int LastSame = end - 1;
	for (int seek = end; seek >= start; seek = seek - 1)
	{
		if (s[seek] != s[LastSame]){ break; }
		LastSame = seek;
	}

	/*if (s[LastSame] == Target)
	{
		::cout << " : 0\r\n";
	}
	else
	{
		::cout << " : 1\r\n";
	}*/

	return SlovePanCake(s, start, LastSame, s[LastSame] == '+') + (s[LastSame] == Target ? 0 : 1);
}
int main()
{
	int Times = 0;
	::cin >> Times;

	for (int seek = 0; seek < Times; seek = seek + 1)
	{
		char Buffer[512];
		::cin >> Buffer;

		string strStack = Buffer;

		::cout << "Case #" << seek + 1 << ": " << SlovePanCake(strStack, 0, strStack.size()) << endl;
	}

	//::system("pause");

	return 0;
}