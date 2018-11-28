#include "stdafx.h"

void go(int caseN);

int main()
{
	ifstream in("A-large.in");
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

	string result;
	for (unsigned char ch: S)
	{
		if (result.size() == 0 || ch >= (unsigned char)result.front()) 
			result.insert(result.begin(), ch);
		else
			result.push_back(ch);
	}

	cout << result << endl;
}

