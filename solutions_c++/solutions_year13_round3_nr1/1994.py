#include <iostream>
#include <algorithm>
#include <vector>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <string>

using namespace std;

int dp[108][108];

int main(void){

	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);

	freopen("A-small-attempt1.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int T,n;
	string str;

	long long ans = 0;

	scanf("%d",&T);
	
	for(int t = 0; t < T; t++){
		ans = 0;
		memset(dp, 0, sizeof dp);

		cin>>str>>n;

		int sz = str.size();

		for(int len = 1; len < n; len++){
			for(int i = 0; i <= sz - len; i++){
				dp[i][i+len] = 0;
			}
		}

		for(int i = 0; i + n <= sz; i++){
			bool flag = true;
			for(int j = 0; j <= n-1  && j < sz; j++){
				if(str[i+j] == 'a' || str[i+j] == 'e' || str[i+j] == 'i' || str[i+j] == 'o' || str[i+j] == 'u'){
					flag = false;
					break;
				}
			}
			if(flag){
				dp[i][i+n-1] = 1;
				ans++;
			}
		}


		for(int len = n+1; len <= sz; len++){
			for(int i = 0; i <= sz - len; i++){
				dp[i][i+len-1] = (dp[i+1][i+len-1] ||  dp[i][i+len-2]);
				if(dp[i][i+len-1])
					ans++;

			}
		}

		cout<<"Case #"<<t+1<<": "<<ans<<endl;

	}

	return 0;
}