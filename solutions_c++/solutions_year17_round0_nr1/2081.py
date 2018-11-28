#include <stdio.h>
#include <iostream>
#include <fstream>
#include <math.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <hash_map>
#include <hash_set>
#include <unordered_map>
#include <unordered_set>
#include <string.h>
#include <queue>
#include <list>
#include <iomanip>
#include <string>

using namespace std;

#define ll long long

ll MODE = 1000000007;

int K;
string S;


void SingleProcess(ofstream& fout)
{
	int count = 0;
	for (int i = 0; i < S.length(); i++)
	{
		if (S[i] == '-')
		{
			if (i + K>S.length())
			{
				fout << "IMPOSSIBLE";
				return;
			}

			for (int j = i; j < i+K; j++)
			{
				if (S[j] == '-') S[j] = '+';
				else S[j] = '-';
			}
			count++;
		}
	}
	fout << count;
}


int main()
{
	FILE* fp = freopen("in.txt", "r", stdin);
	ofstream fout("out.txt");
	int Cases = 0;
	scanf("%d", &Cases);
	for (int time = 0; time < Cases; time++)
	{
		char c[2000];
		cin >> c;
		S = c;
		cin >> K;

		fout << "Case #" << (time + 1) << ": ";
		SingleProcess(fout);
		fout << endl;
		std::cout << time << endl;
	}
	fclose(fp);
	fout.close();

	return 0;

}