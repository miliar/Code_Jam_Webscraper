#include<iostream>
#include<cstdio>
#include<vector>
#include<cstdlib>
#include<cmath>
#include<iomanip>
#include<algorithm>
#include<set>
#include<iomanip>
#include<queue>
#include<map>
#include<deque>

using namespace std;

#define VI vector<int>
#define PI pair<int,int>
#define F first
#define S second
#define MP make_pair
#define LL long long
#define PB push_back
#define MAXN 1000000
#define MAXITER 100000
#define VB vector<bool>

int check(int i){
	int num = i;
	int ans = 0;
	VB vis(10,0);
	int ct = 10;
	while(ct > 0){
		int tmp = num;
		while(tmp){
			int r = tmp % 10;
			if(!vis[r]){
				vis[r] = 1;
				ct--;
			}
			tmp /= 10;
		}
		num += i;
		ans++;
	}
	return ans;
}

int main()
{
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2016/sheep_input2.txt", "r", stdin);
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2016/sheep_output2.txt", "w", stdout);
	int cases;
	scanf("%d", &cases);
	//printf("number of cases %d\n", cases);
	for(int i=1;i<=cases;i++){
		printf("Case #%d: ", i);
		int n;
		scanf("%d", &n);
		if(n==0)
			printf("INSOMNIA\n");
		else
			printf("%d\n", check(n)*n);
	}
	return 0;
}
