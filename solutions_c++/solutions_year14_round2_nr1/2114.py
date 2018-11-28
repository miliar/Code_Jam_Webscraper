#include <cstdio> 
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

string input = "A-small-attempt0.in";
string output = "A-small-attempt0.out";

int fun(string m, string s) {
	string main = m;
	string str = s;
	int res = 0;
	string big = str;
	if (main.length() > str.length()) 
		big = main;
	
	if (main[0] != str[0])
		return -1;
	for (int i = 1; i < big.length(); i++) {
		if (i == main.length() || i == str.length())
			break;
		if (main[i] == str[i])
			continue;
		if (main[i] == main[i - 1]) {
			main = main.substr(0, i) + main.substr(i + 1, main.length() - i - 1);
			i--;
			res++;
			continue;
		}
		if (str[i] == main[i - 1]) {
			main = main.substr(0, i) + main[i - 1] + main.substr(i, main.length() - i);
			i--;
			res++;
			continue;
		}
		return -1;
	}
	if (main[main.length() - 1] == str[str.length() - 1]) {
		res += abs((int)main.length() - (int)str.length());
		int minLen = main.length();
		if (str.length() < minLen)
			minLen = str.length();
		if (main.substr(0, minLen) == str.substr(0, minLen))
			return res;
	}
	if (main == str)
		return res;
	return -1;
}

int main() {
	ifstream in(input);
	ofstream out(output);
	int t;
	in >> t;
	for (int z = 1; z <= t; z++) {
		out << "Case #" << z << ": ";
		int n;
		in >> n;
		string *arr = new string[n];
		for (int i = 0; i < n; i++)
			in >> arr[i];
		int min = 999999999;
		for (int i = 0; i < n; i++) {
			int max = 0, max2 = 0;
			string main2 = arr[i];
			for (int j = 1; j < n; j++) {
				if (main2[j] == main2[j - 1]) {
					main2 = main2.substr(0, j) + main2.substr(j + 1, main2.length() - j - 1);
				}
			}
			for (int j = 0; j < n; j++) {
				int tmp = fun(main2, arr[j]);
				if (tmp >= 0) {
					max2 += tmp;
				}
				else {
					max2 = 999999999;
					break;
				}
			}
			for (int j = 0; j < n; j++) {
				int tmp = fun(arr[i], arr[j]);
				//out << tmp << " ";
				if (tmp >= 0) {
						max += tmp;
				}
				else {
					max = 999999999;
					break;
				}
			}
			if (max2 < max)
				max = max2;
			//out << max << endl;
			if (min > max)
				min = max;
		}
		if (min == 999999999)
			out << "Fegla Won";
		else
			out << min;
		out << endl;
		
	}
	return 0;
}

