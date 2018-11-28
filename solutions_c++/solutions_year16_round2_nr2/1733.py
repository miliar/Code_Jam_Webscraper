#include <iostream>
#include <string>
#include <stdio.h>
#include <math.h>
using namespace std;
string a, b;
int numbera[100];
int numberb[100];
long long ansa, ansb;
string resa, resb;
long long minn;
inline void dfs(int dep, int numa, int numb, int big) {
	if (dep == a.size()) {
		long long tansa = 0;
		long long tansb = 0;
		for (int i = 0; i < dep; i++) {
			tansa = tansa * 10 + numbera[i];
			tansb = tansb * 10 + numberb[i];
		}
		if (abs(tansa - tansb) < minn) {
			minn = abs(tansa - tansb);
			resa = "";
			resb = "";
			for (int i = 0; i < dep; i++) {
				resa = resa + char(numbera[i] + '0');
				resb = resb + char(numberb[i] + '0');
			}
		}
		return;
	}
	numbera[dep] = numa;
	numberb[dep] = numb;
	if (a[dep+1] == '?' && b[dep+1] == '?') {
		if (numa == numb) {
			
			if (big > 0){
				dfs(dep+1, 0, 0, big);
				dfs(dep+1, 0, 1, 1);
				dfs(dep+1, 1, 0, 1);
			}
			else if (big == 0) {
				dfs(dep+1, 0, 0, big);
				dfs(dep+1, 0, 1, -1);
				dfs(dep+1, 1, 0, 1);
			}
			else {
				dfs(dep+1, 0, 0, big);
				dfs(dep+1, 0, 1, -1);
				dfs(dep+1, 1, 0, -1);
			}
		}
		else if (numa < numb) {
			if (big > 0)
				dfs(dep+1, 0, 9, 1);
			else {
				dfs(dep+1, 9, 0, -1);
			}
		}
		else {
			if (big < 0)
				dfs(dep+1, 9, 0, -1);
			else
				dfs(dep+1, 0, 9, 1);
		}
	}
	else if (a[dep+1] != '?' && b[dep+1] == '?') {
		if (numa == numb) {
			if (a[dep+1] != '0') {
				dfs(dep+1, a[dep+1] - '0', a[dep+1] - '0' - 1, 1);
			}
			dfs(dep+1, a[dep+1] - '0', a[dep+1] - '0', big);
			if (a[dep+1] != '9') {
				dfs(dep+1, a[dep+1] - '0', a[dep+1] - '0' + 1, -1);
			}
		}
		else if (numa < numb) {
			if (big > 0)
				dfs(dep+1, a[dep+1] - '0', 9, 1);
			else
				dfs(dep+1, a[dep+1] - '0', 0, -1);
		}
		else {
			if (big < 0)
				dfs(dep+1, a[dep+1] - '0', 0, -1);
			else
				dfs(dep+1, a[dep+1] - '0', 9, 1);
		}
	}
	else if (a[dep+1] == '?' && b[dep+1] != '?') {
		if (numa == numb) {
			if (b[dep+1] != '0') {
				dfs(dep+1, b[dep+1] - '0' - 1, b[dep+1] - '0', -1);
			}
			dfs(dep+1, b[dep+1] - '0', b[dep+1] - '0', big);
			if (b[dep+1] != '9') {
				dfs(dep+1, b[dep+1] - '0' + 1, b[dep+1] - '0', 1);
			}
		}
		else if (numa < numb) {
			if (big > 0)
				dfs(dep+1, 0, b[dep+1] - '0', 1);
			else
				dfs(dep+1, 9, b[dep+1] - '0', -1);
		}
		else {
			if (big < 0)
				dfs(dep+1, 9, b[dep+1] - '0', -1);
			else
				dfs(dep+1, 0, b[dep+1] - '0', 1);
		}
	}
	else {
		if (big == 0){
			if (a[dep+1] == b[dep+1])
				dfs(dep+1, a[dep+1] - '0', b[dep+1] - '0', 0);
			else if (a[dep+1] > b[dep+1])
				dfs(dep+1, a[dep+1] - '0', b[dep+1] - '0', 1);
			else
				dfs(dep+1, a[dep+1] - '0', b[dep+1] - '0', -1);
		}
		else {
			dfs(dep+1, a[dep+1] - '0', b[dep+1] - '0', big);
		}
	}
}
int main() {
	int t;
	scanf("%d",&t);
	for (int ii = 1; ii <= t; ii++) {
		printf("Case #%d: ", ii);
		cin>>a>>b;
		minn = 9223372036854775807;
		if (a[0] == '?' && b[0] == '?') {
			dfs(0, 0, 0, 0);
			dfs(0, 0, 1, -1);
			dfs(0, 1, 0, 1);
		}
		else if (a[0] == '?' && b[0] != '?') {
			
			if (b[0] != '0') {
				dfs(0, b[0] - '0' - 1, b[0] - '0', -1);
			}
			dfs(0, b[0] - '0', b[0] - '0', 0);
			if (b[0] != '9') {
				dfs(0, b[0] - '0' + 1, b[0] - '0', 1);
			}
		}
		else if (a[0] != '?' && b[0] == '?') {
			
			if (a[0] != '0') {
				dfs(0, a[0] - '0', a[0] - '0' - 1, 1);
			}
			dfs(0, a[0] - '0', a[0] - '0', 0);
			if (a[0] != '9') {
				dfs(0, a[0] - '0', a[0] - '0' + 1, -1);
			}
		}
		else {
			if (a[0] == b[0])
				dfs(0, a[0] - '0', b[0] - '0', 0);
			else if (a[0] > b[0]) 
				dfs(0, a[0] - '0', b[0] - '0', 1);
			else 
				dfs(0, a[0] - '0', b[0] - '0', -1);
		}
		
		cout<<resa<<' '<<resb<<endl;
	}
}