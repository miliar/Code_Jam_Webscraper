#include <cstdio>
#include <cstdlib>
#include <cstring>

bool testCase()
{
	int l, x;
	scanf("%d%d", &l, &x);
	char input[10240];
	memset(input, 0, sizeof(input));
	scanf("%s", input);
	for (int i = 0; i < x; i++)
	{
		for (int j = 0; j < l; j++)
		{
			input[i * l + j] = input[j];
		}
	}
	char conv[128][128];
	conv['1']['1'] = '1';
	conv['1']['i'] = 'i';
	conv['1']['j'] = 'j';
	conv['1']['k'] = 'k';
	conv['i']['1'] = 'i';
	conv['i']['i'] = -'1';
	conv['i']['j'] = 'k';
	conv['i']['k'] = -'j';
	conv['j']['1'] = 'j';
	conv['j']['i'] = -'k';
	conv['j']['j'] = -'1';
	conv['j']['k'] = 'i';
	conv['k']['1'] = 'k';
	conv['k']['i'] = 'j';
	conv['k']['j'] = -'i';
	conv['k']['k'] = -'1';

	char table[10240];
	table[0] = input[0];
	for (int i = 1; i < l * x; i++)
	{
		bool negative = !(table[i - 1] > 0);
		table[i] = conv[abs(table[i - 1])][input[i]];
		table[i] = negative ? -table[i] : table[i];
	}
	if (table[l * x - 1] != -'1')
	{
		return false;
	}

	bool state = false;
	for (int i = 0; i < l * x; i++)
	{
		if (state == false)
		{
			if (table[i] == 'i')
			{
				state = true;
			}
		}
		else
		{
			if (table[i] == 'k')
			{
				return true;
			}
		}
	}
	return false;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d: %s\n", i, testCase() ? "YES" : "NO");
	}
}