
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <math.h>
#include <iostream>
#include <assert.h>



#include <algorithm>
#include <map>
#include <vector>
#include <set>

using namespace std;

#define PI 3.14159265358979323
#define EPS 0.000000001
#define INF 1000000000

int T;



char lc;


int  f[110][110];
int n, m;

bool is_good(int y, int x) {
	bool goodx = true;
	bool goody = true;
	
	int d = f[y][x];
	
	for (int i=0;i<n;i++) {
		if (f[i][x]>d) {
			goody=false;
			break;
			}
	}
	
	for (int i=0;i<m;i++) {
		if (f[y][i]>d) {
			goodx=false;
			break;
			}
	}
	
	return goody||goodx;
}


int main() {
	cin>>T;
	int cs=1;
	char tc;
	
	while (T-->0) {
		
		
		cin>>n>>m;
		
		for (int i=0;i<n;i++) {
			for (int j=0;j<m;j++) {
				cin>>f[i][j];
			}
		}
		
		bool good = true;
		
		for (int i=0;i<n;i++) {
			for (int j=0;j<m;j++) {
			
//				if (is_good(i, j)) {
//					printf("1");
//				} else printf("0");
				
				good=good&&is_good(i, j);
				
				
			}
//			printf("\n");
		}
		
		printf("Case #%d: %s", cs++, good?"YES":"NO");
		
		
		printf("\n");
	}
	
    return 0;
    
}


