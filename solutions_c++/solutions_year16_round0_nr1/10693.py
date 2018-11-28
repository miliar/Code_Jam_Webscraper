#include <fstream>
void digits(int x);
bool chtest();
bool test[10];
int main() {
	std::ifstream fin("input.in");
	std::ofstream fout("output.in");
	int T;
	fin >> T;
	int *input = new int[T];
	int *output = new int[T];
	for (int i = 0; i < T; i++)
	{
		fin >> input[i];
	}
	for (int i = 0; i < T; i++)
	{
		if (input[i] == 0)
		{
			fout << "Case #" << i +1<< ": INSOMNIA"<< std::endl;
			continue;
		}
		for (int j = 1;; j++)
		{
			digits(input[i]*j);
			if (chtest()) {
				fout << "Case #" << i + 1 << ": " << input[i]*j << std::endl;
				break;
			}
		}
	}
	return 0;
}
void digits(int x) 
{
	do
	{
		test[x % 10]=true;
		x /= 10;
	} while (x);
}
bool chtest() 
{
	for (int i = 0; i < 10; i++)
	{
		if (test[i]==0)
		{
			return false;
		}
	}
	for (int i = 0; i < 10; i++)
	{
		test[i] = 0;
	}
	return true;
}