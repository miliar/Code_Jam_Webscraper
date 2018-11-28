/**************************************************
 * Author	 : xiaohao Z
 * Blog	 : http://www.cnblogs.com/shu-xiaohao/
 * Last modified : 2014-04-12 20:39
 * Filename	 : 2014_pre_B.cpp
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
const double eps = 1E-8;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T, kase = 1;
   	double c, f, x;
	cin >> T;
	while(T--){
		cin >> c >> f >> x;
		double min = x/2.0, loc = x/2.0;
		for(int i=1; ; i++){
			double tans = 0;
			for(int j=0; j<i; j++) tans += c/(2.0+f*j);
			tans += x/(2.0+f*i);
			if(loc < tans || loc-tans < eps) break;
			loc = tans;
			if(tans < min) min = tans;
		}
		printf("Case #%d: ", kase++);
		printf("%.7lf\n", min);	
	}
	return 0;
}

