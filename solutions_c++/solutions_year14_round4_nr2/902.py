#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

void compress(vector<int>& arr)
{
	vector<int> copy = arr;
	sort(copy.begin(), copy.end());

	unordered_map<int, int> replacements;
	for(int i = 0; i < copy.size(); i++)
	{
		replacements[copy[i]] = i;
	}

	for(int& i : arr)
	{
		i = replacements[i];
	}
}

const int treeSize = 1024;
int tree[treeSize * 2];

void add(int a, int b, int v)
{
	a += treeSize;
	b += treeSize;

	while(a <= b)
	{
		if(a % 2 == 1)
		{
			tree[a] += v;
			a++;
		}
		if(b % 2 == 0)
		{
			tree[b] += v;
			b--;
		}

		a /= 2;
		b /= 2;
	}
}

int read(int i)
{
	int total = 0;

	i += treeSize;

	while(i > 0)
	{
		total += tree[i];
		i /= 2;
	}

	return total;
}

void clearTree()
{
	for(int i = 0; i < treeSize * 2; i++)
	{
		tree[i] = 0;
	}
}


int solve()
{
	int n;
	cin >> n;

	vector<int> arr(n);
	for(int& i : arr)
	{
		cin >> i;
	}
	compress(arr);

	int minSol = INT_MAX;

	unordered_map<int, int> indexes;
	for(int i = 0; i < arr.size(); i++)
	{
		indexes[arr[i]] = i;
	}

	sort(arr.begin(), arr.end());
	do
	{
		int i = 0;
		while(i != arr.size() - 1 && arr[i] < arr[i + 1])
			i++;

		while(i != arr.size() - 1 && arr[i] > arr[i + 1])
			i++;

		if(i != arr.size() - 1) continue;

		int thisSol = 0;
		clearTree();
		for(int j : arr)
		{
			int index = indexes[j];

			thisSol += read(index);
			add(0, index, 1);
		}

		minSol = min(minSol, thisSol);
	}
	while(next_permutation(arr.begin(), arr.end()));

	return minSol;
}

int main()
{
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": " << solve() << endl;
	}

	return 0;
}