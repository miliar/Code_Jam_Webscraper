#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>
#include <set>

using namespace std;

vector<char> divideDigits(int a)
{
	vector<char> res;
	char b[10];
	
	sprintf(b, "%d", a);
	string c = b;
	
	for(int i=0; i<c.length(); i++)
		res.push_back(c[i]);

	return res;
}

int main()
{
	int N, T;

	cin >> T;

	for(int i=0; i<T; i++)
	{
		set<char> resSet;
		vector<char> resVec;

		cin >> N;
		if(N == 0)
		{
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
			continue;
		}
		for(int j=1;;j++)
		{
			resVec = divideDigits(j*N);
			for(int k=0; k<resVec.size(); k++)
			{
				resSet.insert(resVec[k]);
			}
			if(resSet.size() == 10)
			{
				cout << "Case #" << i+1 << ": " << j*N << endl;
				resSet.clear();
				break;
			}
			resVec.clear();
		}

	}

	return 0;
}
