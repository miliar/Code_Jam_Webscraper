#include <cstdio>
#include <string>
#include <vector>
#include <iostream>
using namespace std;

int x, y, n;
bool vis[10000];

bool isPalindrome(int i){
	vector <int> a(0);
	while (i){
		a.push_back(i % 10);
		i /= 10;
	}
	for (int i = 0; i < a.size(); i++)
		if (a[i] != a[a.size() - 1 - i])
			return false;
	return true;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w", stdout);
	for (int i = 1; i * i <= 1000; i++){
		if (isPalindrome(i) && isPalindrome(i * i)){
			vis[i * i] = true;
		}
	}
	scanf("%d",&n);
	for (int i = 1; i <= n; i++){
		scanf("%d%d",&x,&y);
		int ans = 0;
		for (int j = x; j <= y; j++)
			ans += vis[j];
		printf("Case #%d: %d\n", i, ans);
	}
    return 0;
}
