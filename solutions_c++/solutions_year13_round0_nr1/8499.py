#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;
const char* XWon = "X won";
const char* OWon = "O won";
const char* Draw = "Draw";
const char* GameNC = "Game has not completed";
#define TTDBG

class TestCase
{
	static const int T_R = 4;
	static const int T_C = 4;
	char input[T_R][T_C];
public:
	char& Input(int x, int y)
	{
		return input[x][y];
	}
	int R()
	{
		return T_R;
	}
	int C()
	{
		return T_C;
	}
};

class InputSystem
{
	int mTestCases;
	TestCase mCurrTestCase;
	char m_str[5];
	int currTestCase;
	fstream* fileStream;
public:
	InputSystem():mTestCases(-1), currTestCase(0), fileStream(0)
	{
	}
	~InputSystem()
	{
		if(fileStream)
			delete fileStream;
		fileStream = 0;
	}
	TestCase* ReadFromFile(char* filename)
	{
		if(mTestCases == -1)
		{
			char x[4];
			fileStream = new fstream(filename);
			(*fileStream)>>mTestCases;
			(*fileStream).getline(x,5);
		}
		if(currTestCase < mTestCases)
		{
			for(int i = 0; i < mCurrTestCase.R(); i++)
			{
				(*fileStream).getline(m_str, 5);
				for(int j = 0; j < mCurrTestCase.C(); j++)
				{
					mCurrTestCase.Input(i, j) = m_str[j];
				}
			}
			(*fileStream).getline(m_str, 5);
			currTestCase++;
			return &mCurrTestCase;

		}
		return 0;
	}
	TestCase* Read()
	{
		if(mTestCases == -1)
		{
			cin>>mTestCases;
		}
		if(currTestCase < mTestCases)
		{
			for(int i = 0; i < mCurrTestCase.R(); i++)
			{
				cin.getline(m_str, 4);
				for(int j = 0; j < mCurrTestCase.C(); j++)
				{
					mCurrTestCase.Input(i, j) = m_str[j];
				}
			}
			cin.getline(m_str, 4);
			currTestCase++;
			return &mCurrTestCase;

		}
		return 0;
	}
};

class TicTakTotem
{
	InputSystem input;
	static const char X = 'X';
	static const char O = 'O';
	static const char T = 'T';
	static const char Emp = '.';
	enum 
	{
		xwon,
		owon,
		draw,
		gamenc
	};
public:
	void SolveAndPrint()
	{
		TestCase* c = input.Read();
		int i = 1;
		while(c)
		{
			const char* result = Result(c);
			cout<<"Case #"<<i<<" "<<result<<endl;
		}
	}
#ifdef TTDBG
	void SolveDbg(TestCase tc, char* inputFile, char* outputfile)
	{
		TestCase* c = input.ReadFromFile(inputFile);
		fstream ofile(outputfile);
		int nn = 1;
		while(c)
		{
			const char* rs = Result(c);
			ofile<<"Case #"<<nn<<": "<<rs<<endl;
			nn++;
			c = input.ReadFromFile(inputFile);
		}
	}
#endif
private:
	const char* Result(TestCase* tc)
	{
		int result = gamenc;
		int i = 0;
		int empty = 0;
		//Rows
		for(int r = 0; r < tc->R(); r++)
		{
			for(i = 1; i < tc->C(); i++)
			{
				if(((tc->Input(r, i-1) == tc->Input(r, i)) ||(tc->Input(r, i) == T) ||(tc->Input(r, i-1) == T))
					&&(tc->Input(r, i-1) != Emp))
					continue;
				if((tc->Input(r, i) == Emp))
				{
					empty++;
				}
				break;
			}
			if(i == tc->C())
			{
				if((tc->Input(r, 0) == X) || tc->Input(r, 3) == X)
					return XWon;
				else if((tc->Input(r, 0) == O) || tc->Input(r, 3) == O)
					return OWon;
			}
		}
		//cols
		for(int c = 0; c < tc->R(); c++)
		{
			for(i = 1; i < tc->C(); i++)
			{
				if(((tc->Input(i - 1, c) == tc->Input(i, c)) ||(tc->Input(i, c) == T)||(tc->Input(i -1, c) == T))
					&&(tc->Input(i - 1, c) != Emp))
					continue;
				if((tc->Input(i, c) == Emp))
				{
					empty++;
				}
				break;
			}
			if(i == tc->R())
			{
				if((tc->Input(0, c) == X) || tc->Input(3, c) == X)
					return XWon;
				else if((tc->Input(0, c) == O) || tc->Input(3, c) == O)
					return OWon;
			}
		}
		//Diagonals 1
		for(i = 1; i < tc->R(); i++)
		{
			if(((tc->Input(i - 1, i-1) == tc->Input(i, i)) ||(tc->Input(i, i) == T)||(tc->Input(i-1, i-1) == T))
				&&(tc->Input(i-1, i-1) != Emp))
					continue;
			if((tc->Input(i, i) == Emp))
			{
				empty++;
			}
			break;

		}
		if(i == tc->R())
		{
			if((tc->Input(0, 0) == X) || tc->Input(3, 3) == X)
				return XWon;
			else if((tc->Input(0, 0) == O) || tc->Input(3, 3) == O)
				return OWon;
		}
		int j = tc->R() - 1;
		for(i = 1; i < tc->R(); i++, j--)
		{
			if(((tc->Input(j, i-1) == tc->Input(j - 1, i)) ||(tc->Input(j - 1, i) == T)||(tc->Input(j, i-1) == T))
				&&(tc->Input(j, i-1) != Emp))
					continue;
			if((tc->Input(j, i) == Emp))
			{
				empty++;
			}
			break;
		}
		if(i == tc->R())
		{
			if((tc->Input(0, 3) == X) || tc->Input(3, 0) == X)
				return XWon;
			else if((tc->Input(0, 3) == O) || tc->Input(3, 0) == O)
				return OWon;
		}
		if(empty > 0)
			return GameNC;
		return Draw;
	}
};


int main()
{
#ifndef TTDBG
	TicTakTotem t;
	t.SolveAndPrint();
#else
	TicTakTotem tc;
	TestCase t;
	t.Input(0, 0) = '.';
	t.Input(0, 1) = 'X';
	t.Input(0, 2) = 'X';
	t.Input(0, 3) = 'O';
	t.Input(1, 0) = '.';
	t.Input(1, 1) = 'O';
	t.Input(1, 2) = 'O';
	t.Input(1, 3) = 'O';
	t.Input(2, 0) = 'O';
	t.Input(2, 1) = 'O';
	t.Input(2, 2) = 'O';
	t.Input(2, 3) = 'X';
	t.Input(3, 0) = 'O';
	t.Input(3, 1) = '.';
	t.Input(3, 2) = '.';
	t.Input(3, 3) = 'O';
	char* ifn = "input1.txt";
	char* ofn = "output1.txt";
	tc.SolveDbg(t, ifn, ofn);
#endif
	return 0;
}