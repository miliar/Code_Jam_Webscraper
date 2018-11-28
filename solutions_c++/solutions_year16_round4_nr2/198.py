#include <iostream>
#include <vector>
#include <map>
#include <list>
#include <cstring>
#include <string>
#include <algorithm>
#include <ctime>
#pragma warning(disable:4996)


#define N 3
#define SIZE N*N
#define ARRAYSIZE 400000
using namespace std;

struct status
{
	string s;       
	int zero;       
	int g;       
	int father;      
};

status goal;
status start;
status puzzle[ARRAYSIZE];

int direction[4] = { -N, N, -1, 1 };

vector<string> close;
multimap<int, int> open;   
int p;

int f(status &);
int astar();
bool abletomove(string &, int);
bool hasanswer();

int main()
{
	freopen("data.txt", "r", stdin);
	freopen("out.txt", "a+", stdout);
	for (int i = 0; i < SIZE; i++)
	{
		start.s += cin.get();
		cin.get();
		if (start.s[i] == '0')start.zero = i;
	}
	for (int i = 0; i < SIZE; i++)
	{
		goal.s += cin.get();
		cin.get();
		if (goal.s[i] == '0')goal.zero = i;
	}
	int index;
	time_t start, end;
	if (hasanswer())
	{
		start = clock();
		index = astar();
		end = clock();
		cout << index << endl;
		cout << double(end - start) / CLOCKS_PER_SEC << endl;
	}
	else
	{
		cout << "No Answer" << endl;
		cout << 0 << endl;
	}
	return 0;
}

bool hasanswer()
{
	int cs=0, cg=0;
	for (int i = 0; i < N;i++)
	for (int j = 0; j < i; j++)
	{
		if (start.s[j] < start.s[i])cs++;
		if (goal.s[j] < goal.s[i])cg++;
	}
	if (cs % 2 == cg % 2)return true;
	else return false;
}



int f(status &p)
{
	int cnt = 0;
	for (int i = 0; i < SIZE; i++)
	{
		if (p.s[i] != goal.s[i])
			cnt++;
	}
	return cnt;
}

bool abletomove(int zero, int direct)
{
	switch (direct)
	{
		case 0:
			if (zero < N)return false;
			break;
		case 1:
			if (zero > SIZE-N-1)return false;
			break;
		case 2:
			if (zero%N == 0)return false;
			break;
		case 3:
			if (zero%N == N - 1)return false;
			break;
	}
	return true;
}


int astar()
{
	p = 0;
	start.g = 0;
	start.father = 0;
	puzzle[p] = start; 
	open.insert(pair<int, int>(f(puzzle[p]),p));
	while (!open.empty())
	{
		int index = open.begin()->second;

		open.erase(open.begin());
		close.push_back(puzzle[index].s);
		if (puzzle[index].s == goal.s)
			return index;
		for (int i = 0; i < 4; i++)
		{
			if (abletomove(puzzle[index].zero, i))
			{
				string s = puzzle[index].s;
				int j = puzzle[index].zero;
				s[j] = s[j + direction[i]];
				s[j + direction[i]] = '0';

				if (find(close.begin(), close.end(), s) != close.end())
					continue;
				p++;
				if (p >= ARRAYSIZE)
					return -2;
				puzzle[p].s = s;
				puzzle[p].zero = j + direction[i];
				puzzle[p].father = index;
				puzzle[p].g = puzzle[index].g + 1;
				for (auto x = open.begin(); x != open.end(); x++)
				if (puzzle[p].s == puzzle[x->second].s
					&&f(puzzle[p]) < f(puzzle[x->second]))
				{
					open.erase(x);
					break;
				}

				open.insert(pair<int, int>(f(puzzle[p]), p));
			}
		}
	}
	return -1;
}