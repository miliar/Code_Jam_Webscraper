/**************************************************
 * Author	 : xiaohao Z
 * Blog	 : http://www.cnblogs.com/shu-xiaohao/
 * Last modified : 2016-04-09 14:09
 * Filename	 : A.cpp
 * Description	 : 
 * ************************************************/

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <map>
#define MP(a, b) make_pair(a, b)
#define PB(a) push_back(a)

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<unsigned int,unsigned int> puu;
typedef pair<int, double> pid;
typedef pair<ll, int> pli;
typedef pair<int, ll> pil;

const int INF = 0x3f3f3f3f;
const double eps = 1E-6;
const int LEN = 11;

int f[LEN], N;

bool isEnd(int num) {
	char str[LEN];
	sprintf(str, "%d", num);
	int len = strlen(str);
	for(int i=0; i<len; i++) {
		if(f[str[i] - '0'] == 0) {
			f[str[i] - '0'] = 1;
			N ++;
		}
	}
	return N == 10;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T, num, kase = 1;
	cin >> T;
	while(T --) {
		cin >> num;
		if(num == 0) {
			cout << "Case #" << kase ++ << ": " << "INSOMNIA" << endl;
			continue;
		}
		memset(f, 0, sizeof f);
		N = 0;
		int sum = 0;
		while(1) {
			sum += num;
			if(isEnd(sum)) {
				cout << "Case #" << kase ++ << ": " << sum << endl;
				break;
			}
		}
	}
	return 0;
}

