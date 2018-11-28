
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cassert>
#include <deque>
#include <iostream>
#include <list>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
using namespace std;

int a[110][110];


int main() {
	freopen("E:/TDDOWNLOAD/B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, Te=1;
	cin>>T;
	while(T--) {
		int n, m;
		cin>>n>>m;
		for(int i=0;i<n;i++) for(int j=0;j<m;j++) cin>>a[i][j];
		bool fail = false;

		for(int i=0;i<n;i++) {
			for(int j=0;j<m;j++) {
				bool bigger;

				bigger = false;
				for(int ni = 0;ni<n;ni++) if(a[ni][j] > a[i][j]) bigger = true;
				if(!bigger) continue;
				bigger = false;
				for(int nj=0;nj<m;nj++) if(a[i][nj] > a[i][j]) bigger = true;
				if(!bigger) continue;
				fail = true;
			}
		}
		printf("Case #%d: %s\n", Te++, fail?"NO":"YES");
	}

}