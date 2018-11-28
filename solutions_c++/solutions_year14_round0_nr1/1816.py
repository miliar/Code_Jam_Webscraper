#include<sys/types.h>
#include<dirent.h>

#include<algorithm>
#include<iostream>
#include<string>
#include<vector>
#include<cstdio>
#include<cstdlib>
#include<cassert>
#include<sstream>
#include<cmath>
#include<fstream>
#include<map>
#include<tr1/unordered_map>
#include<set>
#include<tr1/unordered_set>

#define MAX(x, y) ((x) > (y) ? (x) : (y))
#define MIN(x, y) ((x) < (y) ? (x) : (y))
#define ABS(x) ((x) > 0 ? (x) : -(x))
#define lt(x, y)	((x) >= 0 && ((x) < (y) || (y) < 0))

#define SWAP(x, y) {(x) += (y); (y) = (x) - (y); (x) -= (y);}

#define EPS 1e-6
#define PI 3.14159265358979323846

using namespace std;

int T;

void filter(vector<int>&a, int ans, vector<int>&good){

	ans--;

	for(int r = 0; r < 4; r++){

		if(r == ans)	continue;

		for(int s = r * 4, i = 0; i < 4; i++, s++){

			good[a[s] - 1] = 0;
		}
	}
}

int main()
{
	cin >> T;

	for(int caseidx = 1; caseidx <= T; caseidx++){

		vector<int> good(16, 1);
		for(int i = 0; i < 2; i++){

			int ans;
			vector<int>a;
			cin >> ans;
			for(int j = 0; j < 16; j++){
				int t;
				cin >> t;
				a.push_back(t);
			}
				
			filter(a, ans, good);
		}

		int ans = -1;

		for(int i = 0; i < 16; i++){
			if(good[i]){
				if(ans >= 0)	ans = 17;
				else ans = i;
			}
		}
		printf("Case #%d: ", caseidx);
		if(ans < 0)	printf("Volunteer cheated!\n");
		else if(ans == 17)	printf("Bad magician!\n");
		else printf("%d\n", ans + 1);
	}

	return 0;
}

// vi: ts=2 sw=2
