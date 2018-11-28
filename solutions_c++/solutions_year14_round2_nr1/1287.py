#include <iostream>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <climits>
#include <vector>
#include <algorithm>
#include <map>
typedef long long ll;
using namespace std;
const int N = 101;
int n = 0;
int num = 0;
int icInx[N];
vector<vector<int> > icSet;
vector<string> source;
inline int iabs(int a) { return a > 0 ? a : -a; }
inline int imax(int a, int b) { return a > b ? a : b; }
inline int imin(int a, int b) { return a < b ? a : b; }
inline int find(vector<int> &d)
{
	int ret = INT_MAX;
	int tmp = 0;
	int i = 0, j = 0;
	for(i = d[0]; i <= d[d.size() - 1]; ++i)
	{
		tmp = 0;
		for(j = 0; j < d.size(); ++j)
		{
			tmp += iabs(i - d[j]);
		}
		if(tmp < ret) { ret = tmp; }
	}
	return ret;
}
inline int solve()
{
	int i = 0, j = 0, k = 0;
	int tc = 0, ret = 0;
	char tmp = 0;
	num = 0;
	memset(icInx, 0, sizeof(icInx));
	icSet.clear();

	for(i = 0; i < source[0].size(); ++i)
	{
		tmp = source[0][i];
		vector<int> vtmp;
		while(i < source[0].size() && source[0][i] == tmp) { ++i; }
		i -= 1;
		for(j = 0; j < n; ++j)
		{
			if(icInx[j] >= source[j].size() || source[j][icInx[j]] != tmp) { return -1; }			

			for(k = icInx[j], tc = 0; k < source[j].size() && source[j][k] == tmp; ++tc, ++k);
			icInx[j] = k;
			vtmp.push_back(tc);
		}
		sort(vtmp.begin(), vtmp.end());
		icSet.push_back(vector<int>(vtmp.begin(), vtmp.end()));
		num += 1;
	}
	for(i = 0; i < source.size(); ++i)
	{
		if(icInx[i] != source[i].size()) { return -1; }
	}
	for(i = 0; i < num; ++i)
	{
		ret += find(icSet[i]);
	}
	return ret;
}
int main()
{
	int t = 0, r = 0;		
	int i = 0, j = 0;
	char buffer[2048];

	FILE* in = freopen("D:/Lab/Contests/Contests/file/A-large.in", "r", stdin);
	FILE* out = freopen("D:/Lab/Contests/Contests/file/A-large.out", "w", stdout);

	fscanf(in, "%d", &t);

	for(i = 0; i < t; i++)
	{
		source.clear();
		fscanf(in, "%d", &n);

		for(j = 0; j < n; ++j)
		{
			fscanf(in, "%s", buffer);
			source.push_back(string(buffer));
		}
		r = solve();
		if(r == -1)
		{
			fprintf(out, "Case #%d: %s\n", (i + 1), "Fegla Won");
		}
		else
		{
			fprintf(out, "Case #%d: %d\n", (i + 1), r);
		}
	}

	fclose(out);
	fclose(in);

	return 0;
}