#include <iostream>
#include <bits/stdc++.h>
using namespace std;


int ihop(int num_ppl, vector<int> dist)
{
	int minimum, maximum, size, temp_move;
	
	sort(dist.begin(),dist.end());
	reverse(dist.begin(),dist.end());
	maximum = dist.front();
	minimum = 1e9;
	
	for (float j = 1; j <= maximum; j++)
	{
		temp_move = 0;
		for (int i: dist)
		{
			if (i<= j) break;
			temp_move += ceil(i/j) - 1.0;
		}
		if (minimum > temp_move+j) minimum = temp_move+j;
	}
	return minimum;
}

int main() {
	int n, ppl_num, temp;
	vector<int> distr;
	cin >> n;
	
	for (int i = 0; i < n; i++)
	{
		distr.clear();
		cin >> ppl_num;
		for (int j = 0; j < ppl_num; j++)
		{
			cin >> temp;
			distr.push_back(temp);
		}
		
		cout << "Case #" << i+1 << ": " << ihop(ppl_num, distr) <<endl;
	}
	
	return 0;
}