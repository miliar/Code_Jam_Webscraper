/**************************************************
 * Author	 : xiaohao Z
 * Blog	 : http://www.cnblogs.com/shu-xiaohao/
 * Last modified : 2016-04-16 08:48
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

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T, kase = 1;
	string in;
	cin >> T;
	while(T --) {
		cin >> in;
		char str[1010];
		str[0] = in[0];
		for(int i=1; i<in.size(); i++) {
			if(in[i] >= str[0]) {
				for(int j=i; j>0; j--) str[j] = str[j - 1];
				str[0] = in[i];
			}else str[i] = in[i];
		}
		str[in.size()] = 0;
		cout << "Case #" << kase ++ << ": ";
		cout << str << endl;
	}
	return 0;
}

