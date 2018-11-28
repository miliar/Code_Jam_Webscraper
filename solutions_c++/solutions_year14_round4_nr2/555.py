#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <sstream>
#include <functional>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <list>
#include <numeric>
using namespace std;
const double PI = 3.14159265358979323846;
const double EPS = 1e-12;
const int INF = 1<<25;
typedef pair<int,int> P;
typedef long long ll;
typedef unsigned long long ull;


int main(){
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		int n;
		cin>>n;
		vector<int> d(n);
		for(int i = 0; i < n; i++){
			cin>>d[i];
		}
		/*
		int M = 0, p = -1;
		for(int i = 0; i < n; i++){
			if(d[i]>M){
				M = d[i];
				p = i;
			}
		}*/
		vector<int> d2(d);
		sort(d2.begin(),d2.end());
		int m = n;
		int res = 0;
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				if(d2[i]==d[j]){
					res += min(j,m-j-1);
					for(int k = j; k < m-1; k++){
						d[k] = d[k+1];
					}
					m--;
					break;
				}
			}
		}
		printf("Case #%d: %d\n", Case, res);
	}
	return 0;
}

