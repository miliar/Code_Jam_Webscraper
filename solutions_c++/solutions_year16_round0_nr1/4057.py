#include<iostream>
#include<fstream>
#include<vector>

void splitter(std::vector<int> & obj, long long int n)
{
	bool flag;
	int a;
	while (n > 0)
	{
		flag = true;
		a = n % 10;
		n /= 10;
		for (int i = 0; i < obj.size() && flag; i++) if (obj[i] == a)flag = false;
		if (flag)obj.push_back(a);
	}

}

int main()
{
	int cases;
	long long int n;
	long long int mult;
	bool flag=true;
	std::vector<int> digits;
	std::ifstream fin;
	std::ofstream fout;
	fout.open("output.txt");
	fin.open("input.txt");
	fin >> cases;
	for (int i = 0; i < cases; i++)
	{
		flag = true;
		fin >> n;
		if (n == 0)fout << "Case #" << i + 1 << ": INSOMNIA\n";
		else
		{
			for (int j = 0; flag; j++)
			{
				mult = (j + 1)*n;
				splitter(digits, mult);
				if (digits.size() == 10)
				{
					fout << "Case #" << i + 1 << ": " << mult << "\n";
					flag = false;
				}
			}
			digits.clear();
		}
	}
	system("pause");
}