#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <string>

using namespace std;

const int MAXN = 10000 + 10;

void solve(int test){
	int n, cap;
	scanf("%d%d", &n, &cap);
	
	int files[MAXN];
	bool used[MAXN];
	
	for(int i = 0; i < n; i++)
		scanf("%d", &files[i]), used[i] = false;
	
	sort(files, files + n);
	
	int disks = 0;
	for(int i = n - 1; i >= 0; i--)
		if(!used[i]){
			disks++;
			used[i] = true;
			for(int j = i - 1; j >= 0; j--)
				if(!used[j] && files[j] + files[i] <= cap){
					used[j] = true;
					break;
					}
			}
		
	
	printf("Case #%d: %d\n", test, disks);
	}

int main(){	
	int testcases;
	scanf("%d", &testcases);
	
	for(int test = 0; test < testcases; test++)
		solve(test+1);
	
	return 0;
}
