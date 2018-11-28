#include <fstream>

using namespace std;

const int MAX = 102400;

int T, N, B, ans;
long long pData[MAX];

long long Solve(long long x);

int main()
{
	ifstream fin("B.in");
	ofstream fout("B.out");
	fin >> T;
	for(int i = 1; i <= T; i++)
	{
		fin >> B >> N;
		for(int j = 1; j <= B; j++)
		{ fin >> pData[j]; }
		long long l = 1, r = 100000000000000LL;
		while(l < r)
		{
			long long m = l + (r - l) / 2;
			if(l + 1 == r)
			{
				if(Solve(l) < N) { l++; }
				break;
			}
			if(Solve(m) >= N) { r = m; }
			else { l = m; }
		}
		N -= Solve(l - 1);
		for(ans = 1; ans <= B; ans++)
		{
			if(l % pData[ans] == 0)
			{
				N--;
				if(N == 0) { break; }
			}
		}
		fout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}

long long Solve(long long x)
{
	long long res = 0;
	if(x == 0) { return 0; }
	for(int i = 1; i <= B; i++)
	{ res += x / pData[i] + 1; }
	return res;
}
