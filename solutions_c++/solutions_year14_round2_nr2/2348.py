#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <conio.h>

std::ifstream In;
std::ofstream Out;

int main(int argc, char *argv[])
{
	In = std::ifstream("In.txt");
	Out = std::ofstream("Out.txt");

	unsigned int TestCases = 0;
	In >> TestCases;

	for (unsigned int x = 0; x < TestCases; x++)
	{
		unsigned int LimitA, LimitB, Goal;
		In >> LimitA >> LimitB >> Goal;

		unsigned int Matches = 0;
		for (unsigned int K = 0; K < Goal; K++)
		{
			for (unsigned int A = 0; A < LimitA; A++)
			{
				if ((A & K) == 0 && K != 0)
				{
					continue; // No common bits
				}
				for (unsigned int B = 0; B < LimitB; B++)
				{
					if ((B & K) == 0 && K != 0)
					{
						continue; // No common bits
					}
					if ((A & B) == K)
					{
						Matches++;
					}
				}
			}
		}
		Out << "Case #" << (x + 1) << ": " << Matches << std::endl;
	}

	In.close();
	Out.close();

	return 0;
}