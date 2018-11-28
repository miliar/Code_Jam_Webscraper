#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int compare_to(const std::string& s1, const std::string& s2)
{
	if (s1 == s2)
		return 0;
	int res = 0;
	if (s1.length() == 0 || s2.length() == 0)
		return -1;
	if (s1[0] != s2[0])
		return -1;
	int i = 0, j = 0;
	while (i < s1.length() && j < s2.length())
	{
		if (s1[i] == s2[j])
		{
			i++;
			j++;
			continue;
		}
		if ( s1[i] == s1[i-1])
		{
			i++;
			res++;
			continue;
		}
		if ( s2[j] == s2[j-1])
		{
			j++;
			res++;
			continue;
		}
		return -1;
	}
	if (i < s1.length())
	{
		for (int x = i; x < s1.length(); ++x)
			if (s1[x] != s1[x-1])
				return -1;
		res += s1.length() - i;
	}
	if (j < s2.length())
	{
		for (int x = j; x < s2.length(); ++x)
			if (s2[x] != s2[x-1])
				return -1;
		res += s2.length() - j;
	}
	return res;
}

int multi_check(const std::vector<std::string>& v)
{
	int res = 0;
	std::vector<int> indexes;
	int n = v.size();
	char cur_char = v[0][0];
	for (int i = 0; i < n; ++i)
		if (v[i][0] != cur_char)
			return -1;
	for (int i = 0; i < n; ++i)
		indexes.push_back(1);
	bool working = true;

	while (working)
	{
		int add_count = 0;
		int del_count = 0;
		for (int i = 0; i < n; ++i)
		{
			if (indexes[i] < v[i].length())
			{
				if (v[i][ indexes[i] ] == cur_char)
					++del_count;
				else
					++add_count;
			}
			else
			{
					++add_count;
			}
		}
		if (add_count == 0 || del_count == 0)
		{
			for (int i = 0; i < n; ++i)
				if (indexes[i] < v[i].length())
				{
					cur_char = v[i][indexes[i]];
					break;
				}
			for (int i = 0; i < n; ++i)
				indexes[i] += 1;
		}
		else
		if (add_count < del_count)
		{
			for (int i = 0; i < n; ++i)
				if (indexes[i] < v[i].length())
				{
					if (v[i][ indexes[i] ] == cur_char)
						indexes[i] += 1;
				}
			res += add_count;
		}
		else
		{
			for (int i = 0; i < n; ++i)
				if (indexes[i] < v[i].length())
				{
					if (v[i][ indexes[i] ] == cur_char)
						indexes[i] += 1;
				}
			res += del_count;
		}
		working = false;
		for (int i = 0; i < n; ++i)
			if (indexes[i] < v[i].length())
				working = true;
	}
	return res;
}

int main()
{
	int T;
	std::ifstream input("input.txt");
	std::ofstream output("output.txt");
	input >> T;
	for (int t = 1; t <= T; ++t)
	{
		output << "Case #" << t << ": ";
		int n;
		input >> n;
		std::vector<std::string> v;
		for (int i = 0; i < n; ++i)
		{
			std::string str;
			input >> str;
			v.push_back(str);
		}
		bool has_answer = true;
		for (int i = 0; i < n-1 && has_answer; ++i)
			for (int j = 1; j < n; ++j)
				if (compare_to(v[i], v[j]) == -1)
				{
					has_answer = false;
					break;
				}
		if (has_answer)
		{
			int res = multi_check(v);
			output << res << "\n";
		}
		else
			output << "Fegla Won\n";
	}
	input.close();
	output.close();
	return 0;
}