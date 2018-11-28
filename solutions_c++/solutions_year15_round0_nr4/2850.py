#include <iostream>
#include <string>
#include <vector>
#include <fstream>

//#define DEBUGMODE
//#define DOUBLENEWLINE
#define PROMPT_INCORRECT_INPUT std::cout<<"Incorrect input!"<<std::endl

void PrintResult(int BOOL)
{
	static int Counter = 1;
	std::cout << "Case #" << Counter++ << ": ";
	if (BOOL)
	{
		std::cout << "GABRIEL" << std::endl;
	}
	else
	{
		std::cout << "RICHARD" << std::endl;
	}
}

int Min(int R, int C)
{
	if (R<C) return R;
	else return C;
}

int Max(int R, int C)
{
	if (R<C) return C;
	else return R;
}

// 1 represents GABRIEL
// 0 represents RICHARD
int Omino(int X, int R, int C)
{
	if (X == 1) return 1;
	if ( X > R && X > C ) return 0;
	if ( (R*C) % X != 0 ) return 0;
	if ( X >= 7 ) return 0;
	//if ( X >= R + C - 1) return 0;
	if ( X >= Min(R,C) + 2 && Max(R,C) > 2) return 0;
	return 1;
}

void Execute()
{
	int NumberOfInputs;
	std::cin >> NumberOfInputs;

	if (NumberOfInputs > 100 || NumberOfInputs < 1)
	{
		PROMPT_INCORRECT_INPUT;
		return;
	}

	int X,R,C;
	while (NumberOfInputs--)
	{
		std::cin >> X >> R >> C;
		PrintResult(Omino(X,R,C));
	}
}

int main(int argc, char* argv[])
{

	std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf

	if (argc < 3)
	{
		std::cout << argv[0] << " INPUT_FILE OUTPUT_FILE" << std::endl;
		return -1;
	}

	std::ifstream in(argv[1]);
    std::cin.rdbuf(in.rdbuf()); //redirect std::cin to text file

    std::ofstream out(argv[2]);
    std::cout.rdbuf(out.rdbuf()); //redirect std::cout to text file

    Execute();

    std::cin.rdbuf(cinbuf);   //reset to standard input again
    std::cout.rdbuf(coutbuf); //reset to standard output again
 
}
