#include <fstream>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

bool is_palindrome(int num)
{
	int reverse = 0, safe = num;
	while (safe > 0)
	{
		reverse = reverse * 10 + safe % 10;
		safe /= 10;
	}
	return reverse == num;
}

int main()
{
	int N;

	fin >> N;
	

	for (int T = 0; T < N; ++T)
	{
		int x, y;
		fin >> x >> y;
		int result = 0;
		for (int i = x; i <= y; ++i)
		{
			int root = (int) sqrt(i);
			if (root * root == i && is_palindrome(i) && is_palindrome(root))
				++result;
		}
		fout << "Case #" << (T+1) << ": " << result << "\n";
	}
	return 0;
}