#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<set>
#include<map>
#include<vector>
#include<iostream>
using namespace std;
void solve(int k){
	cout << "Case #" << k << ": ";
	string s;	
	int l,cur=0,curt=0;
	cin >> l >> s;
	for (int i = 0; i <= l; i++){
		if (i > curt+cur && s[i]-48!=0)cur += i - cur-curt;
		curt += s[i]-48;
	}
	cout << cur<<endl;
	return;
}
int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
		solve(i);
	return 0;
}