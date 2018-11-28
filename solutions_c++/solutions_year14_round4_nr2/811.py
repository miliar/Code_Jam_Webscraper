#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <string>

using namespace std;

const int MAXN = 1010;

void solve(int test){
	int n;
	scanf("%d", &n);
	
	int seq[MAXN];
	int left[MAXN], right[MAXN];
	bool is[MAXN];
	
	for(int i = 0; i < n; i++)
		scanf("%d", &seq[i]), is[i] = true;
	
	int swaps = 0;
	for(int i = 0; i < n; i++){
		
		int stl, str;
		for(int j = 0; j < n; j++)
			if(is[j]){
				left[j] = 0;
				stl = j;
				break;
				}
				
		for(int j = stl+1; j < n; j++)
			left[j] = left[j-1] + is[j];
		
		right[n-1] = is[n-1];
		for(int j = n-1; j >= 0; j--)
			if(is[j]){
				right[j] = 0;
				str = j;
				break;
				}
		
		for(int j = str-1; j >= 0; j--)
			right[j] = right[j+1] + is[j];
	
		//~ cout << "Left" << endl;
		//~ for(int j = 0; j < n; j++)
			//~ cout << left[j] << " ";
		//~ cout << endl;
		//~ cout << "Right" << endl;
		//~ for(int j = 0; j < n; j++)
			//~ cout << right[j] << " ";
		//~ cout << endl;
		
		int minp, minnum = 0x7fffffff;
		for(int j = 0; j < n; j++)
			if(is[j] && minnum > seq[j])
				minp = j, minnum = seq[j];
		//~ cout << minp  << " " << min(left[minp], right[minp])<< endl;
		
		swaps += min(left[minp], right[minp]);
		is[minp] = false;
		}
	
	printf("Case #%d: %d\n", test, swaps);
	}

int main(){	
	int testcases;
	scanf("%d", &testcases);
	
	for(int test = 0; test < testcases; test++)
		solve(test+1);
	
	return 0;
}
