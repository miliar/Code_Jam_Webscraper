#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <memory.h>
#include <queue>
#include <map>

using namespace std;


typedef long long ll;
const ll N = 110;

int t;
char tmp[N];

int main(){
	scanf("%d",&t);
	for(int test = 1 ; test <= t ; test++){
		scanf("%s",&tmp);
		int ans = 0;
		int len = strlen(tmp);
		char last = tmp[0];
		for(int i = 1 ; i < len;i++){
			if(tmp[i] != tmp[i - 1]){
				last = tmp[i];
				ans++;
			}
		}
		if(last == '-')
			ans++;
		printf("Case #%d: %d\n",test,ans);
	}

	return 0;
}
