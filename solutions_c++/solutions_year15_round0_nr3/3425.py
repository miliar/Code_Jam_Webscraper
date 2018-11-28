#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <fstream>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define cin in
#define cout out

struct quat{
	char value;
	bool positive;
};

int dp[10001][10001];

quat multiply(quat op1, char op2)
{
	quat result;
	
	if (op1.value == op2 || (op1.value == 'i' && op2 == 'k') || (op1.value == 'j' && op2 == 'i') || (op1.value == 'k' && op2=='j'))
		result.positive = false;
	else
		result.positive = true;

	result.positive = (result.positive == op1.positive) ? true : false;

	int koko = log2(7 ^ (1 << (op1.value - 'i') | 1 << (op2 - 'i')));
	result.value = op1.value == op2 ? '1' : op1.value == '1' ? op2 : 'i' + koko;
	return result;
}

std::string repeat(const std::string &word, int times) {
	std::string result;
	result.reserve(times*word.length()); // avoid repeated reallocation
	for (int a = 0; a < times; a++)
		result += word;
	return result;
}

string input;
bool recurse(int index, char cChar) {

	if (index == input.length() && cChar == 'l')
		return true;
	else if (index == input.length() || cChar == 'l')
		return false;

	if (dp[index][cChar] != -1)
		return dp[index][cChar];
	
	int& value = dp[index][cChar];

	quat currentSum;
	currentSum.value = input[index];
	currentSum.positive = true;
	if (currentSum.value == cChar && currentSum.positive)
		if (recurse(index+1, cChar + 1))
			return value = true;

	for (int i = index + 1; i < input.length(); i++)
	{
		currentSum = multiply(currentSum, input[i]);
		if (currentSum.value == cChar && currentSum.positive)
			if (recurse(i + 1, cChar + 1))
				return value = true;
	}
	return value = false;
}

int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");

	int t;
	int l, x;

	cin >> t;
	for (int i = 0; i < t; i++)
	{
		for (int j = 0; j < 10001; j++)
			for (int k = 0; k < 10001; k++)
				dp[j][k] = -1;

		cin >> l >> x;
		cin >> input;

		input = repeat(input, x);

		cout << "Case #" << i + 1 << ": " << (recurse(0, 'i') ? "YES" : "NO") << endl;
	}
	in.close();
	out.close();
}