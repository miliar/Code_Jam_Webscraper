#define _USE_MATH_DEFINES
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<climits>
#include<string>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<cmath>
#include<queue>
#include<cstring>
#include<stack>
#include<functional>
#include<deque>
#include<cstdlib>
#include<ctime>
using namespace std;

int main(){
	int T;
	cin>>T;
	for(int tc=1;tc<=T;tc++){
		int N;
		char S;
		cin>>N;
		int sum = 0, ans = 0;
		for(int i=0;i<=N;i++){
			cin>>S;
			if(S-'0'>0 && sum<i) ans += i-sum, sum = i;
			sum += S-'0';
		}
		printf("Case #%d: %d\n",tc,ans);
	}
	return 0;
}
