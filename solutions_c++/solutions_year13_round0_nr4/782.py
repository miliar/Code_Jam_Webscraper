// round0.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <utility>
#include <unordered_set>
#include <windows.h>

using namespace std;

struct chest
{
	int lock;
	vector<int> keys;
	bool hasopen;
};

string treasure(vector<int> keys, vector<chest> chests, int numopen);

string to_string(int i)
{
	stringstream ss;
	ss << i;
	return ss.str();
}

string treasure_wrap(vector<int> keys, vector<chest> chests)
{
	vector<int> allkeys(keys), toopen;
	for (int i = 0; i < chests.size(); i++)
	{
		allkeys.insert(allkeys.end(), chests[i].keys.begin(), chests[i].keys.end());
		toopen.push_back(chests[i].lock);
	}
	sort(allkeys.begin(), allkeys.end());
	sort(toopen.begin(), toopen.end());
	if (!includes(allkeys.begin(), allkeys.end(), toopen.begin(), toopen.end())) return "IMPOSSIBLE";
	return treasure(keys, chests, 0);
}

bool check_dependency(int key, vector<int> keys, vector<chest> chests)
{
	if (find(keys.begin(), keys.end(), key) != keys.end()) return true;
	int numvalid = 0, tmp;
	for (int i = 0; i < chests.size(); i++)
	{
		if (!chests[i].hasopen)
		{
			if (chests[i].lock == key || find(chests[i].keys.begin(), chests[i].keys.end(), key) != chests[i].keys.end())
			{
				numvalid ++;
				tmp = i;
			}
			if (numvalid > 1) return true;
		}
	}
	if (numvalid == 1 && chests[tmp].lock == key)
	{
		return false;
	}
	return true;
}

string treasure(vector<int> keys, vector<chest> chests, int numopen)
{
	cout << "\nkeys:";
	for (int i = 0; i < keys.size(); i++) cout << keys[i] << " ";
	cout << "   opened:";
	for (int i = 0; i < chests.size(); i++) if (chests[i].hasopen) cout << i+1 << " ";
	//Sleep(200);

	if (numopen == chests.size()) return "";
	else if (keys.size() == 0) return "IMPOSSIBLE";
	for (int i = 0; i < chests.size(); i++)
	{
		if (!chests[i].hasopen)
		{
			vector<int>::iterator it = find(keys.begin(), keys.end(), chests[i].lock);
			if (it != keys.end())
			{
				vector<chest> chests1(chests);
				chests1[i].hasopen = true;
				vector<int> keys1 = keys;
				keys1.erase(keys1.begin()+(it-keys.begin()));
				keys1.insert(keys1.end(), chests[i].keys.begin(), chests[i].keys.end());
				if (!check_dependency(chests[i].lock, keys1, chests1))
					continue;
				string res = treasure(keys1, chests1, numopen+1);
				if (res != "IMPOSSIBLE")
					return to_string(i+1) + " " + res;
			}
		}
	}
	return "IMPOSSIBLE";
}

vector<int> parse_line(string line, int n)
{
	int p = 0, lp = 0;
	vector<int> v1;
	for (int k = 0; k < n; k++)
	{
		p = line.find(' ', lp);
		if (p == string::npos) p = line.length();
		v1.push_back(atoi(line.substr(lp, p-lp).c_str()));
		lp = p + 1;
	}
	return v1;
}

int main(int argc, char* argv[])
{
	ifstream in("D-small-attempt1.in");
	ofstream out("output.txt");
	string line;

	getline(in, line);
	int T = atoi(line.c_str());
	for (int i = 0; i < T; i++)
	{
		getline(in, line);
		int pos = line.find(' ');
		int K = atoi(line.substr(0, pos).c_str());
		int N = atoi(line.substr(pos+1).c_str());
		getline(in, line);
		vector<int> start_keys = parse_line(line, K);
		vector<chest> chests;
		for (int j = 0; j < N; j++)
		{
			getline(in, line);
			int p = line.find(' ');
			int tj = atoi(line.substr(0, p).c_str());
			int lp = p + 1;
			p = line.find(' ', lp);
			int kj = atoi(line.substr(lp, p-lp).c_str());
			vector<int> v = parse_line(line, kj+2);
			vector<int> v1(v.begin()+2, v.end());
			chest c;
			c.lock = tj;
			c.keys = v1;
			c.hasopen = false;
			chests.push_back(c);
		}
		out << "Case #" << i+1 << ": " << treasure_wrap(start_keys, chests) << endl;
		cout << "\n" <<  i << "\n";
	}
	getchar();
	return 0;
}