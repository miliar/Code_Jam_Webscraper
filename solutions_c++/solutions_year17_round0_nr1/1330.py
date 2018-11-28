#include <stdio.h>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;
int main(){
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	scanf("%d",&test);
	for(int tc=1; tc<=test; tc++){
		string a;
		int k, ans = 0;
		cin>>a>>k;
		for(int i=0; i<=a.size()-k; i++){
			if(a[i] == '-'){
				ans++;
				for(int j=0; j<k; j++){
					if(a[i+j] == '-')a[i+j] = '+';
					else a[i+j] = '-';
				}
			}
		}
		for(int i=0; i<a.size(); i++)if(a[i] == '-')ans = -1;
		if(ans == -1)printf("Case #%d: IMPOSSIBLE\n", tc);
		else printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}
