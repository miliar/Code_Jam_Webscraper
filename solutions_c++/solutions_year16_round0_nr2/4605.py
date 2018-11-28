#include <iostream>
#include <fstream>

using namespace std;

#define TMAX 101
#define LENGTH 101

int N;
char data[TMAX][LENGTH];
int answer[TMAX];

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
		fp << answer[itor] << endl;
	}

	fp.close();
}

int find_answer(int case_num)
{
	int itor;
	int length;
	int answer;

	int itor_flip;

	answer = 0;

	for (itor = 0; itor < LENGTH; ++itor)
	{
		if (data[case_num][itor] == NULL)
		{
			length = itor;
			break;
		}
	}
	
	for (itor = length - 1; itor >= 0; --itor)
	{
		if (data[case_num][itor] == '+')
			continue;

		++answer;

		for (itor_flip = 0; itor_flip <= itor; ++itor_flip)
		{
			if (data[case_num][itor_flip] == '-')
			{
				data[case_num][itor_flip] = '+';
			}
			else
			{
				data[case_num][itor_flip] = '-';
			}
		}
	}
		
	return answer;
}

void get_answer()
{
	int itor;
	for (itor = 0; itor < N; ++itor)
		answer[itor] = find_answer(itor);
}

int main()
{
	get_input();
	get_answer();
	print_answer();
	return 0;
}