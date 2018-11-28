#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>

#define io_r freopen("input.txt","r",stdin);
#define io_w freopen("output.txt","w",stdout);
#define io_file io_r; io_w;

#define PB push_back
#define MP make_pair
#define ll long long

#define rep(i,n) for (int i = 0; i<n; ++i)
#define clr(x, y) memset(x, y, sizeof x)
#define all(x) (x).begin(), (x).end()

#define MAX 1000100
#define MOD 1000000007

using namespace std;

int solve(int n){
	bool vis[10] = {false};
	int cnt = 0;
	
	for(int i = 1, k = n; i<=100; i++, k+= n){
		int aux = k;
		
		while(aux){
			int x = aux%10;
			if(!vis[x]){
				cnt++;
				vis[x] = true;
			}
			aux /= 10;
		}
		
		if(cnt == 10) return k;
	}
	
	return -1;
}

int ans[MAX];

int main (){
	int T, n;
	
	ans[0] = -1;
	for(int i = 1; i<=1000000; i++) ans[i] = solve(i);

	scanf("%d", &T);
	
	rep(i, T){
		scanf("%d", &n);
		printf("Case #%d: ", i+1);
		if(n == 0) puts("INSOMNIA");
		else printf("%d\n", ans[n]);
	}
	
	return 0;
}
