#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
using namespace std;

int t,smax;

int main(){
	freopen("\\output.txt","w",stdout);
	scanf("%d",&t);
	for(int k = 1; k <= t; k++){
		scanf("%d",&smax);
		int s[smax+1];
		for(int i = 0; i <= smax; i++) scanf("%1d",&s[i]);
		int count = 0;
		int ans = 0;
		for(int i = 0; i <= smax; i++){
			if(i > count){
				ans += i-count;
				count = i;
			}
			count += s[i];
		} 
		printf("Case #%d: %d\n",k,ans);
	}
}