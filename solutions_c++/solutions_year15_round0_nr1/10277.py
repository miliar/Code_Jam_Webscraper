#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <cstring>
#include <cstdio>
#include <queue>
#include <cstdio>
#include <cstdlib>

using namespace std;

int cnt[1004];

int main (){

	int T,tmp,n,ans,sum;
	string s;
	cin>>T;

	for(int t =1;t<=T;++t){
		memset(cnt,0,sizeof cnt);
		ans = sum = 0;

		cin>>tmp>>s;
		n = s.length();

		for(int i=0;i<n;++i)
			cnt[i] = s[i]-'0';

		for(int i=0;i<n;++i){
			if(cnt[i] >0 && sum <i){
				ans += i-sum;
				sum += (i-sum);
			}
			sum += cnt[i];
		}

		printf("Case #%d: %d\n",t,ans);
	}

	return 0;
}


