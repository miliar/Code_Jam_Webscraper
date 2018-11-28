#include<iostream>
#include<fstream>
#include<string>
#include<math.h>
using namespace std;

int numbers[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
bool insomnia = false;
ofstream myout;
void myfunc(int n, int c);
int main()
{
	long long int N = 0, total = 0, count = 1;
	string str;
	std::string::size_type sz;
	myout.open("output.txt");
	bool temp = false;
	ifstream fin;
	fin.open("A-large.in");
	getline(fin, str, '\n');
	total = std::stoi(str, &sz);
	while (count <= total)
	{
		string s;
		getline(fin, s, '\n');
		N = std::stoi(s, &sz);
		myfunc(N, count);
		count++;
		insomnia = false;
		for (int i = 0; i < 10; i++)numbers[i] = 0;
	}
	myout.close();
	system("pause");
}

void myfunc(int n, int c)
{
	long long int lastOne, mul = 0;
	int t = 1;
	bool flag = true;
	if (n == 0)
	{
		insomnia = true;
		myout << "CASE #" << c << ": INSOMNIA" << '\n';
	}
	if (!insomnia)
	{
		while (flag)
		{
			mul = n*t;
			t++;
			long long int temp = mul;
			while (temp != 0)
			{
				int d = temp % 10;
				numbers[d] = 1;
				temp = temp / 10;
			}
			if (numbers[0] == 1 && numbers[1] == 1 && numbers[2] == 1 && numbers[3] == 1 && numbers[4] == 1 && numbers[5] == 1 && numbers[6] == 1 && numbers[7] == 1 && numbers[8] == 1 && numbers[9] == 1)
			{
				flag = false;
				lastOne = mul;
			}
		}
		myout << "CASE #" << c << ": " << mul << '\n';
	}

}