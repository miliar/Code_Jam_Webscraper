#define  _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include<fstream>
#include <memory.h>
#include<vector>
using namespace std;
int used[10];
vector<int> input;
bool get_numbers(int a)
{
	int div = 1;
	while (a > 0)
	{
		used[a % 10] = true;
		a /= 10;
	}
	bool k = true;
	for (int i = 0; i < 10; i++)
		if (!used[i]) k = false;
	return k;
}

int main()
{
	freopen("input.in.txt", "r", stdin);
	freopen("output.in", "w", stdout);
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		int a;
		cin >> a;
		input.push_back(a);
	}
	fclose(stdin);
	for (int i = 0; i < input.size(); i++)
	{
		int b = input[i];
		int count = 1;
		if (b != 0){
			while (!get_numbers(count *b))
			{
				count++;

			}
			memset(used, 0, sizeof(used));
			cout << "Case #" << i + 1 << ": " << count*b << "\n";
		}
		else
		{
			cout << "Case #" << i + 1 << ": " << "INSOMNIA" << "\n";
		}
	}
	fclose(stdout);
	return 0;
}