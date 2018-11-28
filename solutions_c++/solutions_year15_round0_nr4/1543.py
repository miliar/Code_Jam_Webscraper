#include <fstream>

#define MAX_N 20

using namespace std;

ifstream fin("D:\\Input.txt");
ofstream fout("D:\\Output.txt");

int T, N, R, C, answer;

bool check(int n, int r, int c)
{
	if(n > r * c)
		return false;
	if((c * r) % n != 0)
		return false;
	if(n <= 2)
		return true;
	if(n == 3)
		if(min(r, c) == 1)
			return false;
		else
			return true;
	if(n == 4)
		if(min(r, c) <= 2)
			return false;
		else if(min(r, c) == 3 && max(r, c) == 3)
			return false;
		else 
			return true;
	/*if(n == 5)
		return false;
	if(n == 6)
		return false;
	if(n >= 7)
		return false;*/
}

int main(int argc, const char* argv[])
{
	fin >> T;
	for(int i = 0; i < T; i++)
	{
		fin >> N >> R >> C;
		if(check(N, R, C))
			fout << "Case #" << i + 1 << ": " << "GABRIEL" << "\n";
		else
			fout << "Case #" << i + 1 << ": " << "RICHARD" << "\n";
	}
	return 0;
}