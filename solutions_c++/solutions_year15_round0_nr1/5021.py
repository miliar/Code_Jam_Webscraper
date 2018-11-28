#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;

int t, n;
string s;

int main() {
	//freopen("input.txt","r", stdin); 
	//freopen("output.txt","w", stdout);
	cin>>t;
	for (int x=0; x<t; x++) {
		cin>>n>>s;
		int sum=s[0]-'0';
		int res=0;
		for (int i=1; i<=n; i++) {
			if (sum<i) {
				sum++;
				res++;
			}
			sum+=(s[i]-'0');
		}
		printf("Case #%d: %d\n", x+1, res);
	}
	return 0;
}