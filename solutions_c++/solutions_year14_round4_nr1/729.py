#include<iostream>
#include<algorithm>
#include<cstring>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<list>
#include<deque>
using namespace std;

int m1[10001], ans, t, n, x;

int main(int argc, const char *argv[])
{
	int cc = 0;
	cin>>t;
	while(t--){
		cin>>n>>x;
		for(int i = 0 ; i < n ; i ++)
			cin>>m1[i];
		ans = 0;
		sort(m1, m1+n);
		for(int i = n-1 ; i >= 0 ; i --){
			if(m1[i] == -1){
				continue;
			}
			int j = i-1;
			for( ; j >= 0 ; j --){
				if(m1[j] == -1) continue;
				if(m1[i] + m1[j] <= x) break;
			}
			if( j == -1) ans ++;
			else{
				ans ++;
				m1[j] = -1;
			}
		}

		printf("Case #%d: %d\n", ++cc, ans);
	}
	return 0;
}
