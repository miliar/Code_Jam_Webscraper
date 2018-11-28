#include <iostream>
#include <stdio.h>
#include <math.h>
#include <list>
#include <queue>
#include <vector>
#include <functional>
#include <stack>
#include <utility> 
#include <stdlib.h>
#include <map>
#include <string.h>
#include <algorithm>
typedef long long int ll;
#define SWAP(a, b) (((a) ^= (b)), ((b) ^= (a)), ((a) ^= (b)))
#define CLR(a) memset(a, 0, sizeof(a))
using namespace std;
int main() {
	freopen ("output.txt","w",stdout);
	freopen ("input.in","r",stdin);
	int t, i, j, n, ans, mini, maxi, fans;
	char arr[1000][101];
	cin>>t;
	for(int lol = 1; lol <= t; ++lol) {
		cin>>n;
		ans = 1;
		fans = 0;
		for(i=0;i<n;++i) {
			cin>>arr[i];
		}
		
		int pos[1000] = {0};
		while(1) {
			mini = 999999;
			maxi = -999999;
			int count = 0;
			if(pos[0] >= strlen(arr[0])) break;
			char x = arr[0][pos[0]];
			while(arr[0][pos[0]] == x && pos[0] < strlen(arr[0])) {
				++pos[0];
				++count;
			}
			mini = min(count, mini);
			maxi = max(count, maxi);
			for(i=1;i<n;++i) {
				if(arr[i][pos[i]] != x || pos[i] >= strlen(arr[i])) {
					ans = 0;
					break;
				}
				count = 0;
				while(arr[i][pos[i]] == x && pos[i] < strlen(arr[i])) {
					++pos[i];
					++count;
				}
				mini = min(mini, count);
				maxi = max(count, maxi);
			}
			fans += maxi - mini;
		}
		for(i=0;i<n;++i) {
			if(pos[i] < strlen(arr[i])) ans = 0;
		}
		if(ans) {
			cout<<"Case #"<<lol<<": "<<fans<<endl;
		} else {
			cout<<"Case #"<<lol<<": Fegla Won"<<endl;
		}
	}
	return 0;
}