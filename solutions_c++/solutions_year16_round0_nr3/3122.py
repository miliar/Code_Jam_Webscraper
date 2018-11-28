#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

long long T, N, J, cases = 1, counter = 0;
string str;

pair<bool, long long> values;

vector<string> v1;
vector<long long> v2;

long long BaseNum(string s, long long base)
{
	long long temp = 0;

	reverse(s.begin(), s.end());

	for (long long i = 0; i < s.length(); i++)
	{
		temp += long long(s[i] - '0') * pow(base, i);
	}

	return temp;
}

pair<bool, long long> IsPrime(long long number)
{
	long long i;

	pair<bool, long long> values;

	for (i = 2; i < sqrt(number); i++)
	{
		if (number % i == 0)
		{
			values.first = false;
			values.second = i;
			return values;
		}
	}

	values.first = true;
	values.second = 0;
	return values;
}

void OutPut()
{
	for (long long i = 0; i < v2.size(); i++)
	{
		cout << v2[i];

		if (i != 8)
		{
			cout << " ";
		}
	}
}

void Permutenr(const string& input, string output, int r)
{
	if (counter == J)
	{
		return;
	}

	if (output.length() == r)
	{
		output = "1" + output + "1";

		v2.clear();

		for (long long j = 2; j <= 10; j++)
		{
			values = IsPrime(BaseNum(output, j));

			if (values.first)
			{
				break;
			}

			v2.push_back(values.second);

			if (j == 10)
			{
				counter++;
				cout << output << " ";
				OutPut();
				cout << endl;
			}
		}
	}

	else
	{
		for (int i = 0; i < input.length(); ++i)
		{
			Permutenr(input, output + input[i], r);
		}
	}
}

int main()
{

	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> T;

	while (cases <= T)
	{
		cin >> N >> J;

		cout << "Case #1:" << endl;

		Permutenr("01", "", N-2);

		cases++;
	}

	return 0;
}