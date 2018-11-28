#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <ctime>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cassert>
#include <bitset>

using namespace std;

const int k=4;

bool f[20];

int main() {
	int cases;
	scanf("%d",&cases);
	for (int o=0; o<cases; ++o) {
		int n;
		memset(f,true,sizeof(f));
		scanf("%d",&n);
		for (int i=0; i<k; ++i) {
			for (int j=0; j<k; ++j) {
				int x;
				scanf("%d",&x);
				if (i+1!=n) {
					f[x-1]=false;
				}
			}
		}
		scanf("%d",&n);
		for (int i=0; i<k; ++i) {
			for (int j=0; j<k; ++j) {
				int x;
				scanf("%d",&x);
				if (i+1!=n) {
					f[x-1]=false;
				}
			}
		}
		int ans,s=0;
		for (int i=0; i<k*k; ++i) {
			if (f[i]) {
				ans=i+1;
				++s;
			}
		}
		if (s==1) {
			printf("Case #%d: %d\n",o+1,ans);
		} else if (s==0) {
			printf("Case #%d: Volunteer cheated!\n",o+1);
		} else {
			printf("Case #%d: Bad magician!\n",o+1);
		}
	}
	return 0;
}

