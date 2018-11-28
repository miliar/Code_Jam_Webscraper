#include<iostream>
#include<vector>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<fcntl.h>
#include<unistd.h>
using namespace std;

int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	int idx = 0;
	while(idx ++ < T){
		int N, X;
		scanf("%d%d", &N, &X);
		vector<int> vec(N);
		for(int i = 0;i < N;++ i)
			scanf("%d", &vec[i]);
		sort(vec.begin(), vec.end());
		int res = 0;
		int left = 0, right = N - 1;
		while(left <= right) {
			if(left == right){
				++ res;
				left ++;
				continue;
			}
			if(vec[left] + vec[right] <= X){
				left ++;
				right --;
				res ++;
				continue;
			}
			right --;
			res ++;
		}
		printf("Case #%d: %d\n",idx, res);
	}
	return 0;
}
