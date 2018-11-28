#include <string>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <fstream>
#include <sstream>
#include <iomanip>

using namespace std;

int dwar(vector<double>& ma, vector<double>& mb, int N)
{
	if (N <= 0) return 0;
	int n = 0;
	for (int i = 0; i < N; ++i)
	{
		if (ma[i] < mb[0]) ++n;
		else break;
	}
	ma.erase(ma.begin(), ma.begin()+n);
	mb.erase(mb.end()-n, mb.end());

	int s = 0;
	for (int i = 0; i < N-n; ++i)
	{
		if (ma[i] > mb[i]) ++s;
		else break;
	}
	ma.erase(ma.begin(), ma.begin()+s);
	mb.erase(mb.begin(), mb.begin()+s);
	return s+dwar(ma,mb,N-n-s);
}

int war(vector<double>& ma, vector<double>& mb, int N)
{
	int i, j = 0;
	for (i = 0; i < N; ++i)
	{
		if (j == N) return N-i;
		while (ma[i] > mb[j])
		{
			++j;
			if (j == N) return N-i;
		}
		++j;
	}
	return 0;
}

int main(int argc, char* argv[])
{
	ifstream in("D-large.in");
	ofstream out("result.txt");
	int T, N;
	in >> T;
	for (int i = 0; i < T; ++i)
	{
		in >> N;
		vector<double> ma(N, 0);
		vector<double> mb(N, 0);
		for (int j = 0; j < N; ++j)
			in >> ma[j];
		for (int j = 0; j < N; ++j)
			in >> mb[j];
		sort(ma.begin(), ma.end());
		sort(mb.begin(), mb.end());
		out << "Case #" << i+1 << ": " << dwar(ma,mb,N) << " " << war(ma,mb,N) << endl;
	}

	in.close();
	out.close();
	return 0;
}