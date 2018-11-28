#include <fstream>
#include <vector>
#include <string>

using namespace std;

long long calculate(long long start, long long end);
bool isPalindrome(long long n);

int main()
{
	ifstream in("/home/kyle/Downloads/input.txt");
	ofstream out("/home/kyle/Downloads/output.txt");

	int numberOfCases;
	in >> numberOfCases;
	for (int i = 1; i <= numberOfCases; ++i) {
		long long start, end;
		in >> start >> endl;
		long long result = calculate(start, end);
		out << "Case #" << i << ": " << result << endl;
	}
	return 0;
}

long long calculate(long long start, long long end)
{
	long long first = (long long)sqrt(start);
	long long last = (long long)sqrt(end);
	if (first * first != start) {
		first = first + 1;
	}

	long long result = 0;
	for (long long i = first; i <= last; ++i) {
		if (!isPalindrome(i)) {
			continue;
		}
		long long value = i * i;
		if (isPalindrome(value)) {
			++result;
		}
	}
	return result;
}

bool isPalindrome(long long n)
{
	istringstream iss(n);
	string str;
	iss >> str;
	for (string::size_type i = 0; i != str.size() / 2; ++i) {
		if (str[i] != str[str.size() - i - 1]) {
			return false;
		}
	}
	return true;
}