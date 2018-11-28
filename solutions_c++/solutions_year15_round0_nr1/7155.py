#include<iostream>
#include <fstream>
using namespace std;

int get_number(char c)
{
	switch (c)
	{
	case '0':return 0;
	case '1':return 1;
	case '2':return 2;
	case '3':return 3;
	case '4':return 4;
	case '5':return 5;
	case '6':return 6;
	case '7':return 7;
	case '8':return 8;
	case '9':return 9;
	default:
		break;
	}
}

ofstream fout("test.out");
ifstream fin("A-large.in");

int main()
{
	int T;
	while (fin >> T)
	{
		int i;
		for (i = 1; i <= T; i++)
		{
			int count;
			fin >> count;
			char shy_level[2000];
			fin >> shy_level;
			bool is_start = false;
			int answer = 0;
			int answer2 = 0;
			for (int j = 0, k = 0; j <= count; k++)
			{
				if (shy_level[k] >= 48 && shy_level[k] <= 57)
				{
					is_start = true;
				}
				else
					is_start = false;
				if (is_start)
				{
					if (answer2 < j)
					{
						answer++;
						answer2++;
					}
					int person = get_number(shy_level[k]);
					answer2 += person;
					j++;
				}
			}
			fout << "Case #" << i << ": " << answer << endl;
		}
	}
	return 0;
}