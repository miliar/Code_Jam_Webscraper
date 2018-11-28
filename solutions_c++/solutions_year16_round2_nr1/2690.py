#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <deque>
#include <unordered_map>
#include <algorithm>
using namespace std;

int main()
{
	ifstream f("A-large.in", std::ios::in);
	int t;	f >> t;
	string a; getline(f, a);
	for (int i = 0; i < t; i++)
	{
		string s;
		getline(f, s);

		unordered_map<char, int> chars;
		vector<int> nums;
		for (auto it : s)
			chars[it]++;

		while (chars.find('Z') != chars.end() && chars['Z'] != 0)
		{
			nums.push_back(0);
			chars['Z']--; chars['E']--; chars['R']--; chars['O']--;
		}
		while (chars.find('W') != chars.end() && chars['W'] != 0)
		{
			nums.push_back(2);
			chars['T']--; chars['W']--; chars['O']--;
		}
		while (chars.find('U') != chars.end() && chars['U'] != 0)
		{
			nums.push_back(4);
			chars['F']--; chars['O']--; chars['U']--; chars['R']--;
		}
		while (chars.find('X') != chars.end() && chars['X'] != 0)
		{
			nums.push_back(6);
			chars['S']--; chars['I']--; chars['X']--;
		}
		while (chars.find('S') != chars.end() && chars['S'] != 0)
		{
			nums.push_back(7);
			chars['S']--; chars['E']--; chars['V']--; chars['E']--; chars['N']--;
		}
		while (chars.find('G') != chars.end() && chars['G'] != 0)
		{
			nums.push_back(8);
			chars['E']--; chars['I']--; chars['G']--; chars['H']--; chars['T']--;
		}
		while (chars.find('O') != chars.end() && chars['O'] != 0)
		{
			nums.push_back(1);
			chars['O']--; chars['N']--; chars['E']--;
		}
		while (chars.find('V') != chars.end() && chars['V'] != 0)
		{
			nums.push_back(5);
			chars['F']--; chars['I']--; chars['V']--; chars['E']--;
		}
		while (chars.find('N') != chars.end() && chars['N'] != 0)
		{
			nums.push_back(9);
			chars['N']--; chars['I']--; chars['N']--; chars['E']--;
		}
		while (chars.find('R') != chars.end() && chars['R'] != 0)
		{
			nums.push_back(3);
			chars['T']--; chars['H']--; chars['R']--; chars['E'] -= 2;
		}
		sort(nums.begin(), nums.end());
		cout << "Case #" << i + 1 << ": ";
		for (auto it : nums)
			cout << it;
		cout << endl;
		nums.clear();
		chars.clear();
	}
	return 0;
}