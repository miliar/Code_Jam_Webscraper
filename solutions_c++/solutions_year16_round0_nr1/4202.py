#include <set>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

bool putset(set<int>& s, int n)
{
	while (n != 0)
	{
		s.insert(n % 10);
		n /= 10;
	}
	if (s.size() == 10) return true;
	return false;
}

int findNum(int n)
{
	if (n == 0) return -1;
	set<int> found;	
	int k = n;
	int i = 2;
	for (; !putset(found, k); i++)
		k = n*i;
	return k;
}

int main()
{
	ifstream f;
	f.open("A-large.in", ios::in);

	string line;
	getline(f, line);
	int t = atoi(line.c_str());

	for (int i = 0; i < t; i++)
	{
		getline(f, line);
		int n = atoi(line.c_str());
		int p = findNum(n);
		if (p == -1) std::cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
		else std::cout << "Case #" << i + 1 << ": " << p << endl;;
	}
	return 0;	
}