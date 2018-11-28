/**************************************************
 * Author	 : xiaohao Z
 * Blog	 : http://www.cnblogs.com/shu-xiaohao/
 * Last modified : 2016-04-09 14:41
 * Filename	 : B.cpp
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
string str;

bool check() {
	for(int i=0; i<str.size(); i++) 
		if(str[i] == '-') return false;
	return true;
}

int step1() {
	int ret = 0;
	for(int i=0; i<str.size(); i++) {
		if(str[i] == '-') break;
		str[i] = '-';
		ret = 1;
	}
	//cout << "s1 : " << str << endl;
	return ret;
}

int step2() {
	int i = str.size() - 1;
	while(str[i] == '+' && i >= 0) i--;
	for(int j=0; j<=(i + 1) / 2; j++) {
		char tmp;
		if(str[j] == '-') tmp = '+';
		else tmp = '-';
		if(j == (i + 1) / 2) {
			if(i % 2) break;
			str[j] = tmp;
			break;
		}
		if(str[i - j] == '-') str[j] = '+';
		else str[j] = '-';
		str[i - j] = tmp;
	}
	//cout << "s2 : " << str << " " << i << endl;
	return 1;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T, kase = 1;
	cin >> T;
	while(T --) {
		cin >> str;
		int num = 0;
		while(!check()) {
			num += step1();
			if(check()) break;
			num += step2();
		}
		cout << "Case #" << kase ++ << ": " << num << endl;
	}
	return 0;
}

