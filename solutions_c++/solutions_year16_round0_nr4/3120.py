#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream read;
	read.open("D-small-attempt0.in");

	ofstream write;
	write.open("output.txt");

	int T;
	read >> T;
	
	for(int i = 0; i < T; i++)
	{
		write << "Case #" << i+1 << ": ";
		int K,C,S;
		read >> K >> C >> S;
		for(int j = 0; j < K; j++)
		{
			write << j+1 << " ";
		}
		write << endl;
	}

	return 0;
}