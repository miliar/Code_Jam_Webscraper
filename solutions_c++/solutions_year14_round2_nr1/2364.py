#include <iostream>
#include <vector>
#include <iomanip>
#include <string>

using std::cin;
using std::string;
using std::vector;

void solveCase() {
	int N;
	cin >> N;
	string s1, s2;
	cin >> s1 >> s2;
	vector<char> order;
	vector<int> counts;
	int counter = 1;
	char last = s1[0];
	for (int i = 1; i < s1.length(); ++i)
	{
		if (last == s1[i]) {
			++counter;
		}
		else {
			order.push_back(last);
			counts.push_back(counter);
			counter = 1;
			last = s1[i];
		}
	}

	order.push_back(last);
	counts.push_back(counter);

	//int counter = 1;
	//char last = s2[0];
	int idx = 0;
	int diff = 0;
	//for (int i = 1; i < s2.length(); ++i)
	//{
	//	if (last == s1[i]) {
	//		++counter;
	//	}
	//	else {
	//		if (order[idx] != last) {
	//			std::cout << "Fegla Won";
	//			return;
	//		}
	//		dif += abs()
	//		counter = 1;
	//		last = s1[i];
	//	}
	//}

	counter = 0;
	for (int i = 0;  i < s2.length(); ++i)
	{
		if (order[idx] == s2[i]) {
			++counter;
		}
		else if (counter > 0 && idx + 1 < order.size() && order[idx+1] == s2[i]) {
			diff += abs(counts[idx] - counter);
			++idx;
			counter = 1;
		}
		else {
			std::cout << "Fegla Won";
			return;
		}
	}

	if (idx < order.size() - 1) {
		std::cout << "Fegla Won";
		return;
	}

	diff += abs(counts[idx] - counter);

	std::cout << diff;
}

int main() {
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	int T;
	std::cin >> T;
	for (int i = 1; i < T + 1; ++i)
	{
		std::cout << "Case #" << i << ": ";
		solveCase();
		if (i < T)
			std::cout << std::endl;
	}
	return 0;
}