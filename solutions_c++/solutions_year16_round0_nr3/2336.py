// File Name: a.cpp
// Author: ***
// Created Time: 2016年04月09日 星期六 08时44分10秒

#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <cstdlib>
#include <map>
#include <cstring>
#include <cassert>
#include <fstream>
#include <sstream>
#include <cmath>
#define FOR(i,a,b)  for(int i=(int)(a);i<(int)(b);++i)
#define REP(i,a)  FOR(i,0,a)
#define PB push_back
#define MP make_pair
#define VC vector
#define PII pair <int, int>
#define VI VC < int >
#define VF VC < float >
#define VS VC < string >
#define VVS VC < VS >
#define DB(a) cerr << #a << ": " << (a) << endl;
#define VALID(ret) (!isnan(ret) && !isinf(ret))
using namespace std;

int isPrime(long long t)
{
	if (t <= 1) return t;
	if (t == 2) return -1;
	int hf = sqrt(t);
	for (int i = 2;i <= hf;++i) {
		if (t % i == 0) {
			return i;
		}
	}
	return -1;
}
void solve(int n, int j)
{

	//vector<int> mask(1<<n, 1);
	//vector<int> factor(1<<n, -1);
	//mask[0] = 0;
	//mask[1] = 0;
	//for (int p = 2;p < mask.size();++p) {
	//	if (mask[p]) {
	//		int s = p + p;
	//		while (s < mask.size()) {
	//			mask[s] = 0;
	//			factor[s] = p;
	//			s += p;
	//		}
	//	}
	//}
	//for (int i = 0;i < mask.size();++i) {
	//	cout<<i<<' '<<mask[i]<<' '<<factor[i]<<endl;
	//}

	
	vector<vector<long long> > mul(11, vector<long long>(n, 1));
	for (int i = 2;i <= 10;++i) {
		for (int z = 1;z < n;++z) {
			mul[i][z] = i * mul[i][z - 1];
		}
	}
	int cnt = 0;
	long base = (1<<(n - 1)) + 1;
	for (int p = 0;p < (1<<(n - 2));++p) {
		long dig = base + p * 2;

		//cout<<"check:"<<endl;
		//for (int z = n - 1;z >= 0;--z) {
		//	if ((1<<z) & dig) {
		//		cout<<1;
		//	} else {
		//		cout<<0;
		//	}
		//}
		//cout<<endl;


		
		vector<long long> ft(11, 0);
		int bad = 0;
		for (int b = 2;b <= 10;++b) {
			long long t = 0;
			for (int z = 0;z < n;++z) {
				if ((1<<z) & dig) {
					t = t + mul[b][z];
				}
			}
			int factor = isPrime(t);
			if (factor <= 0) {
				bad = 1;
				break;
			} else {
				ft[b] = factor;
			}
		}
		if (bad == 1) continue;
		
		cnt += 1;

		for (int z = n - 1;z >= 0;--z) {
			if ((1<<z) & dig) {
				cout<<1;
			} else {
				cout<<0;
			}
		}
		for (int b = 2;b <= 10;++b) {
			cout<<' '<<ft[b];
		}
		cout<<endl;
		if (cnt >= j) break;
		
		
			
	}

}
int main()
{
  freopen("data", "r", stdin);
  int T;
  cin>>T;
  for (int i = 1;i <= T;++i) {
		int n, j;
		cin>>n>>j;
    cout<<"Case #"<<i<<":"<<endl;
    solve(n, j);
  }
  return 0;
}

