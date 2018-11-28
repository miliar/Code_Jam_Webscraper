#include <cstring>
#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;
int get(int n,string s)
{
	int sum = 0,ans = 0;
	for(int i=1;i<=n;i++){
		sum = sum + (s[i-1]-'0');
		if(sum<i){
			ans+=(i-sum);
			sum = i;
		}
	}
	return ans;
}
int main()
{
	int t,n,cas = 0;
	string s;
	freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
	cin>>t;
	while(t--){
		cin>>n>>s;
		printf("Case #%d: %d\n", ++cas, get(n,s));
	}
	return 0;
}

