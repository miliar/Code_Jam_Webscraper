#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
using namespace std;
int n,m,x,k;
int num[5050],sum[5050];
int ans;
void init(){
	cin >> n;
	ans = 0;
	memset(num,0,sizeof num);
	for (int i = 0; i < n; i++){
		cin >> x;
		num[x]++;
		if (ans < x) ans = x;
	}
}
void slove(){
	k = ans;
	memset(sum,0,sizeof sum);
	for (int i = 2; i <k; i++){
		for (int j = i + 1; j <= k; j++){
			sum[i] += (j-1)/i * num[j];
		}
		if (ans > sum[i] + i) ans = sum[i] + i;
	}
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tt,cas;
	cin >> tt;
	for (cas = 1; cas <= tt; cas++){
		init();
		slove();
		cout << "Case #" << cas <<": " << ans << endl;
	}
	return 0;

}
