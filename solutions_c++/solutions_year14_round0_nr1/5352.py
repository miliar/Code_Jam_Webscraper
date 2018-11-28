#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

string solve(int a, vector<vector<int> > arr1, int b, vector<vector<int> > arr2)
{
	a--; b--;

	set<int> possible1, possible2;
	for (int i = 0; i < 4; i++)
	{
		possible1.insert(arr1[a][i]);
		possible2.insert(arr2[b][i]);
	}	

	vector<int> pos;
	for (auto i = possible1.begin(); i != possible1.end(); i++)
		if (possible2.find(*i) != possible2.end())
			pos.push_back(*i);

	if (pos.size() == 1)
		return to_string(pos[0]);

	if (pos.size() == 0)
		return "Volunteer cheated!";

	return "Bad magician!";
}

int main(int argc, char* argv[])
{
	FILE* fin = NULL;
	FILE* fout = NULL; 

	fin = freopen("input.txt", "r", stdin);
	fout = freopen("output.txt", "w", stdout);

	int T; cin >> T;
	for (int test = 1 ; test<= T; test++)
	{
		int a, b;
		vector<vector<int> > arr1(4, vector<int>(4)), arr2 = arr1;

		cin >> a;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin >> arr1[i][j];

		cin >> b;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin >> arr2[i][j];

		printf("Case #%d: %s\n", test, solve(a, arr1, b, arr2).c_str());
	}

	if (fin) fclose(fin);
	if (fout) fclose(fout);

	return 0;
}

