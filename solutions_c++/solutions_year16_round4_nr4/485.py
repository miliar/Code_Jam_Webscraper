#include <stdio.h>
#include <vector>
#include <string.h>
#include <algorithm>
using namespace std;
int n, res,work[5][5];
int cost;
int perm[5];
bool check[5];
bool machine[5];
bool back(int k){
	if (k == n){
		return true;
	}

	bool ok = 0;
	for (int i = 0; i < n; i++){
		if (work[perm[k]][i] == 1 && !machine[i]){
			ok = 1;
			machine[i] = 1;
			bool x = back(k + 1);
			machine[i] = 0;
			if (!x)
				return false;
		}
	}
	if (ok)
		return true;
	return false;
}
void fill_work(int i,int j){
	if (i == n){
		for (int i = 0; i < n; i++)
			perm[i] = i;
		bool ok;
		do{
			ok = back(0);
			if (!ok)
				break;
		} while (std::next_permutation(perm, perm+n));
		if (ok)
			res = min(cost, res);

		return;
	}
	if (j == n - 1)
		fill_work(i + 1, 0);
	else
		fill_work(i, j+1);

	if (work[i][j] == 0){
		cost++;
		work[i][j] = 1;
		if (j == n - 1)
			fill_work(i + 1, 0);
		else
			fill_work(i, j + 1);
		work[i][j] = 0;
		cost--;
	}
}
int main(){
	int testt;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &testt);
	for (int test = 1; test <= testt; test++){
		res = 100;
		scanf("%d", &n);
		for (int i = 0; i < n; i++){
			for (int j = 0; j < n; j++){
				scanf("%1d", &work[i][j]);
			}	
		}
		fill_work(0, 0);
		printf("Case #%d: %d\n", test, res);
	}
	return 0;
}
