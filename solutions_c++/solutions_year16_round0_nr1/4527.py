#include <iostream>
#include <fstream>

using namespace std;

#define NMAX 100

int N;
int data[NMAX];
int answer[NMAX];

void get_input()
{
	fstream fp;
	fp.open("input.in");
	
	int itor;

	fp >> N;
	for (itor = 0; itor < N; ++itor)
		fp >> data[itor];

	fp.close();
}

void print_answer()
{
	fstream fp;
	fp.open("output.out");

	int itor;
	for (itor = 0; itor < N; ++itor)
	{
		fp << "Case #" << itor + 1 << ": ";
		if (answer[itor] == -1)
			fp << "INSOMNIA" << endl;
		else
			fp << answer[itor] << endl;
	}

	fp.close();
}

int find_answer(int number)
{
	int itor;
	int check[10];
	int flag;

	__int64 multiple;
	__int64 divider;
	__int64 result;

	if (number == 0)
		return -1;
	
	for (itor = 0; itor < 10; ++itor)
		check[itor] = 0;

	flag = 1;
	multiple = (__int64)number;

	while (flag == 1)
	{
		//flag = 0;
		divider = multiple;
		while (divider)
		{
			result = divider % 10;
			if (check[result] == 0)
			{
				flag = 1;
				check[result] = 1;
			}

			divider = divider / 10;
		}

		for (itor = 0; itor < 10; ++itor)
		{
			if (check[itor] == 0)
				break;
		}

		if (itor == 10)
			break;

		multiple += number;
	}

	for (itor = 0; itor < 10; ++itor)
	{
		if (check[itor] == 0)
		{
			return -1;
		}
	}

	return multiple;
}

void get_answer()
{
	int itor;
	for (itor = 0; itor < N; ++itor)
		answer[itor] = find_answer(data[itor]);
}

int main()
{
	get_input();
	get_answer();
	print_answer();
	return 0;
}