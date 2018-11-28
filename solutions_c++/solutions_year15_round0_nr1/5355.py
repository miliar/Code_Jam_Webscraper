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
int t,n,m,i,j,k,w,q,g,x,y;
char s[5005];
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
int main(){
	scanf("%d", &t);
	for(i = 0; i < t; i++){
		scanf("%d%s", &n, s);
		int sum = 0;
		int ans = 0;
		for(j = 0; j <= n; j++){
			int g = s[j] - '0';
			if(sum < j && g > 0){
				ans += (j - sum);
				sum = j + g;
			}
			else
			sum+= g;
		}
		printf("Case #%d: %d\n", i + 1, ans);
	}
}


