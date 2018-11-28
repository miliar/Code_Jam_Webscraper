#pragma comment(linker, "/STACK:65777216")
#include <iostream>
#include <string.h>
#include <string>
#include <math.h>
#include <algorithm>
#include <memory.h>
#include <vector>
#include <stdio.h>
#include <deque>
#include <map>
#include <set>
#include <stack>
  
using namespace std;
  
#define fs first
#define sc second
#define mp make_pair
#define pb push_back
  
typedef long long li;
typedef unsigned long long uli;

int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	int z;
	for(z = 0; z < t; z++){
		int ans1, ans2;
		int a[10][10], b[10][10];
		int i, j;
		cin >> ans1;
		ans1--;
		for(i = 0; i < 4; i++)
			for(j = 0; j < 4; j++)
				cin >> a[i][j];
		cin >> ans2;
		ans2--;
		for(i = 0; i < 4; i++)
			for(j = 0; j < 4; j++)
				cin >> b[i][j];
		int k = 0;
		int ans;
		for(i = 0; i < 4; i++)
			for(j = 0; j < 4; j++){
				if(a[ans1][i] == b[ans2][j]){
					k++;
					ans = a[ans1][i];
				}
			}
		cout << "Case #" << z + 1 << ": ";
		if(k == 0){
			cout << "Volunteer cheated!" << "\n";
			continue;
		}
		if(k == 1){
			cout << ans << "\n";
			continue;
		}
		cout << "Bad magician!" << "\n";
	}
	return 0;
}
/*

*/