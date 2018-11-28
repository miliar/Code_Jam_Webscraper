#include "stdafx.h"

typedef unsigned long long uint64;

void go(int caseN);

int main()
{
	ifstream in("B-large.in");
	ofstream out("out.txt");
	cin.rdbuf(in.rdbuf());
	cout.rdbuf(out.rdbuf());

	int T; 
	cin >> T;
	for (int t = 1; t <= T; ++t) go(t);
    return 0;
}



void go(int caseN)
{
	cout << "Case #" << caseN << ": ";

	string S;
	cin >> S;

	char ch = S[0];
	int flips = 0;
	for (int i = 0; i < S.size(); ++i)
	{
		if (ch == S[i]) continue;
		ch = S[i];
		++flips;
	}
	
	if (ch == '-') ++flips;

	cout << flips << endl;
}

