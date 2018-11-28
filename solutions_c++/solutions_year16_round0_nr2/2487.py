#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cmath>
using namespace std;
int main(){
	int T;
	cin >> T;
	for(int _=1;_<=T;_++){
		int ans = 0;
		char ch[128];
		cin >> ch;
		for(int i=1;ch[i];i++)
			if(ch[i] != ch[i-1] && ch[i] == '-'){
				ans += 2;
			}
		if(ch[0] == '-')
			ans++;
		printf("Case #%d: %d\n",_,ans);
	}
	return 0;
}