#include<iostream>
#include<fstream>
#include<cstdio>
#include<algorithm>
using namespace std;
struct Node
{
	int n;
	char c;
	bool operator <(const Node &v) const
	{
		return n > v.n;
	}
} node[30];
int main()
{
	ifstream ifs;
	ofstream ofs;

	ifs.open("input.txt");
	ofs.open("output.txt");

	int testCase;
	ifs >> testCase;
	for (int cases = 1; cases <= testCase; cases++)
	{
		int room, total = 0;

		ifs >> room;
		for (int i = 0; i < room; i++)
		{
			ifs >> node[i].n;
			total += node[i].n;
			node[i].c = i + 'A';
		}
		ofs << "Case #" << cases << ": ";
		while (total)
		{
			sort(node, node + room);
			if (node[0].n)
			{
				node[0].n--;
				ofs << node[0].c;
				total--;
			}
			if (total == 2 && !node[0].n)
			{
				ofs << " ";
				continue;
			}
			if (node[1].n)
			{
				node[1].n--;
				ofs << node[1].c;
				total--;
			}
			ofs << " ";
		}
		ofs << "\n";
	}
}