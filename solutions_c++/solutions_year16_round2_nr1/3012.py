#include <fstream>
#include <string>
#include <iostream>
using namespace std;
int main()
{
	ifstream infile("A-large.in");
	ofstream outfile("output.in");
	int T;
	int letters[15] = { 0,0,0,0,0,0,0,0,0,0,0,0,0,0 };
	int numbers[10] = { 0,0,0,0,0,0,0,0,0,0 };
	string S;
	char c;
	infile >> T;
	for (int i = 0; i < T; i++)
	{
		for (int abc = 0; abc < 10; abc++)
			numbers[abc] = 0;
		infile >> S;
		for (int b = 0; b < S.size() ; b++)
		{
			c = S[b];
			switch (c)
			{
			case 'E': letters[0]++; break;
			case 'I': letters[1]++; break;
			case 'O': letters[2]++; break;
			case 'Z': letters[3]++; break;
			case 'R': letters[4]++; break;
			case 'N': letters[5]++; break;
			case 'W': letters[6]++; break;
			case 'H': letters[7]++; break;
			case 'F': letters[8]++; break;
			case 'U': letters[9]++; break;
			case 'V': letters[10]++; break;
			case 'X': letters[11]++; break;
			case 'S': letters[12]++; break;
			case 'T': letters[13]++; break;
			case 'G': letters[14]++; break;
			default:
				break;
			}
		}
		while (letters[3] > 0)
		{
			letters[3]--;
			letters[0]--;
			letters[4]--;
			letters[2]--;
			numbers[0]++;
		}
		while (letters[6] > 0)
		{
			letters[6]--;
			letters[13]--;
			letters[2]--;
			numbers[2]++;
		}
		while (letters[9] > 0)
		{
			letters[9]--;
			letters[8]--;
			letters[2]--;
			letters[4]--;
			numbers[4]++;
		}
		while (letters[2] > 0)
		{
			letters[2]--;
			letters[5]--;
			letters[0]--;
			numbers[1]++;
		}
		while (letters[11] > 0)
		{
			letters[11]--;
			letters[12]--;
			letters[1]--;
			numbers[6]++;
		}
		while (letters[12] > 0)
		{
			letters[12]--;
			letters[0]--;
			letters[0]--;
			letters[10]--;
			letters[5]--;
			numbers[7]++;
		}
		while (letters[10] > 0)
		{
			letters[10]--;
			letters[8]--;
			letters[1]--;
			letters[0]--;
			numbers[5]++;
		}
		while (letters[14] > 0)
		{
			letters[14]--;
			letters[1]--;
			letters[0]--;
			letters[7]--;
			letters[13]--;
			numbers[8]++;
		}
		while (letters[13] > 0)
		{
			letters[13]--;
			letters[7]--;
			letters[4]--;
			letters[0]--;
			letters[0]--;
			numbers[3]++;
		}
		while (letters[5] > 0)
		{
			letters[5]--;
			letters[5]--;
			letters[1]--;
			letters[0]--;
			numbers[9]++;
		}
		outfile << "Case #" << i+1 << ": ";
		for (int r = 0; r < 10; r++)
		{
			for (int p = 0; p < numbers[r]; p++)
				outfile << r;
		}
		outfile << endl;
	}
}