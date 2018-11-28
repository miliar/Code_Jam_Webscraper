#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <ctime>
#include <stack>
#include <deque>
#include <iostream>
#include <functional>
int ans1,t,n,m,i,j,q,g,x,y,a[5005];
using namespace std;
struct jeremy{
	int x,y;
};
struct node{
	int x,y;
};
struct edge{
	int x,y;
};
bool cmp(jeremy u ,jeremy v){
	return u.y < v.y;
}
void exhaust(int s, int r){
	if(s == 0){
		int g = 0;
		for(int w = 9; w > 0; w--){
			if(a[w])
			g = max(g, w);
		}
		if(r + g < ans1){
			ans1 = r + g;
		}
	}
	else{
		if(!a[s])
		exhaust(s - 1, r);
		else{
			for(int k = 1; k <= s; k++){
				int temp = a[s];
				int temp2 = a[s / k];
				int temp3 = a[s / k + 1];
				a[s] = 0;
				a[s / k] += temp * (k - s % k);
				a[s / k + 1] += temp * (s % k);
				exhaust(s - 1, r + temp *(k - 1));
				a[s] = temp;
				a[s / k] = temp2;
				a[s / k + 1] = temp3;
			}
		}
	}
}
int main(){
	
	scanf("%d", &t);
	for(i = 0; i < t; i++){
		scanf("%d", &n);
		fill(a, a + 1005, 0);
		for(j = 0; j < n; j++){
			scanf("%d", &x);
			a[x]++;
		}
		ans1 = 1001;
		exhaust(9, 0);
		printf("Case #%d: %d\n", i + 1, ans1);
	}
}


