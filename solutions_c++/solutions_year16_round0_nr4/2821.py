//#include<iostream>
#include<vector>
#include<fstream>
using namespace std;
long long mypow(long long a, long long b)
{
	if (a == 0) return 0;
	if (b == 0) return 1;
	long long temp = mypow(a, b / 2);
	if (b % 2) return a*temp*temp;
	return temp*temp;
}

vector<long long> cnt(int K, int C, int S)
{
	vector<long long> pos(S, 0);
	for (int i = 0; i < K; i++)
	{

		pos[i] = i*mypow(K, C - 1);
	}
	return pos;
}
int main()
{
	ofstream cout("output.txt");
	ifstream cin("input.txt");
	int K, C, S,T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		cin >> K >> C >> S;
		cout << "Case #" << i << ": ";
		if (S < K)cout << "IMPOSSIBLE" << endl;
		else
		{
			vector<long long> ret = cnt(K, C, S);
			for (int i = 0; i < ret.size(); i++)
			{
				cout << ret[i]+1 << " ";
			}
			cout << endl;
		}
	}
	 
	return 0;
}