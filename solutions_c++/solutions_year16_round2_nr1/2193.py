#include <map>
#include <set>
#include <list>
#include <cmath>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <vector>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>
 
#define mp       make_pair
#define pb       push_back
#define all(x)   (x).begin(),(x).end()
#define rep(i,n) for(int i=0;i<(n);i++)
#define _D(p) std::cout<<"L"<<__LINE__<<" : " #p " = "<<(p)<<std::endl;
#define _D2(p,q) std::cout<<"L"<<__LINE__<<" : " #p " = "<<(p) << ", " #q " = "<<(q)<<std::endl;
#define _DN(v) std::cout<<"L"<<__LINE__<<" : " #v " = ["; rep(i,(v).size()) {std::cout<<v[i]<<(i==v.size()-1?"":", ");}std::cout<<"]"<<std::endl;
#define _DNN(v) std::cout<<"L"<<__LINE__<<" : " #v " = [" << std::endl; rep(i,(v).size()) {std::cout<<"	[";rep(j,(v)[0].size()){std::cout<<v[i][j]<<(j==v[0].size()-1?"":", ");}std::cout<<"],"<<std::endl;}std::cout<<"]"<<std::endl;
 
using namespace std;
 
typedef    long long          ll;
typedef    unsigned long long ull;
typedef    vector<bool>       vb;
typedef    vector<int>        vi;
typedef    vector<vb>         vvb;
typedef    vector<vi>         vvi;
typedef    pair<int,int>      pii;
 
const int INF=1<<29;
const double EPS=1e-9;
 
const int dx[]={1,0,-1,0},dy[]={0,-1,0,1};

int main(int argc, char const *argv[])
{
	int n;
	cin >> n;
	for (int h = 0; h < n; ++h)
	{		/* code */
		cout << "Case #"<< h + 1<<": ";
	string s;
	cin >> s;
	int a['Z' - 'A' + 1] = {0};
	for (int j = 0; j < s.size(); ++j)
	{
		a[s[j] - 'A']++;
	}

	int ans[10];
	ans[0] = a['z'- 'a'];
	ans[2] = a['w'- 'a'];
	ans[6] = a['x'- 'a'];
	ans[8] = a['g' - 'a'];
	ans[3] = a['h' - 'a'] - ans[8];
	ans[4] = a['r' - 'a'] - ans[0] - ans[3];
	ans[5] = a['f' - 'a'] - ans[4];
	ans[1] = a['o' - 'a'] - ans[0] -ans[2] -ans[4];
	ans[7] = a['v' - 'a'] - ans[5];
	ans[9] = a['i' - 'a'] - ans[5] - ans[6] - ans[8];


	for (int j = 0; j < ans[0]; ++j)
	{
		cout << 0;
	}
	for (int i = 0; i < ans[1]; ++i)
	{
		cout << 1;
	}
		for (int i = 0; i < ans[2]; ++i)
	{
		cout << 2;
	}
		for (int i = 0; i < ans[3]; ++i)
	{
		cout << 3;
	}
		for (int i = 0; i < ans[4]; ++i)
	{
		cout << 4;
	}
		for (int i = 0; i < ans[5]; ++i)
	{
		cout << 5;
	}
		for (int i = 0; i < ans[6]; ++i)
	{
		cout << 6;
	}
		for (int i = 0; i < ans[7]; ++i)
	{
		cout << 7;
	}
		for (int i = 0; i < ans[8]; ++i)
	{
		cout << 8;
	}
		for (int i = 0; i < ans[9]; ++i)
	{
		cout << 9;
	}
	cout << endl;
}
	return 0;
}