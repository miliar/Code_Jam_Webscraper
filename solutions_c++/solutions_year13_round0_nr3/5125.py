// C1.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

class TC1
{
private:
	int TestNum;
	int TestCur;
	long long A, B;
	int Ans;
	static const long long MAXN = 100000000000000ll;
	ifstream cin;
	ofstream cout;
	vector<long long> Rvec;
	char CNum[30];
	int Aidx;

	void GetTestsNum()
	{
		cin >> TestNum;
	}

	bool fair(long long num)
	{
		Aidx = -1;
		while(num > 0)
		{
			CNum[++Aidx] = (num % 10 + '0');
			num /= 10;
		}
		for(int i = 0, j = Aidx; i < j; ++i, --j)
			if(CNum[i] != CNum[j])
				return false;
		return true;
	}

	void Init()
	{
		for (long long i = 1; i * i <= MAXN; ++i)
			if (fair(i) && fair(i * i))
			{
				std::cout << i << " " << i * i << endl;
				Rvec.push_back(i * i);
			}
		sort(Rvec.begin(), Rvec.end());
	}

	void Input()
	{
	    cin >> A >> B;
	}

	void Run()
	{
		Ans = 0;
		for(vector<long long>::iterator it = Rvec.begin(); it != Rvec.end(); ++it)
			if(A <= (*it) && (*it) <= B)
				++Ans;
	}

	void Output()
	{
		cout << "Case #" << TestCur << ": " << Ans << endl;
	}

public:
	TC1()
	{
		cin = ifstream("C-large-1.in");
		cout = ofstream("C-large-1.txt");
	}
	void Solve()
	{
		GetTestsNum();
		Init();
		for(TestCur = 1; TestCur <= TestNum; ++TestCur)
		{
			Input();
			Run();
			Output();
		}
		
	}
};


int _tmain(int argc, _TCHAR* argv[])
{
	TC1 problem;
	problem.Solve();
	system( "PAUSE" ); 
	return 0;
}

