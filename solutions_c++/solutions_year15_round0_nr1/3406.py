#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <stack>
#include <queue>
using namespace std;
int tt;
char str[1550];
int n,m;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>tt;
	int cas = 1;
	while(tt--){
		cin>>n>>str;
		int l = strlen(str);
		int ans = 0;
		int sum = 0;
		for (int i = 0; i <= n;i++){
			int sub = i - sum;
			int add = str[i] - '0';
			if (sub <= 0){
				sum += add;
			}else {
				ans += sub;
				sum += sub;
				sum += add;
			}
		}
		printf("Case #%d: %d\n",cas++, ans );
		//cout<<"Case #: " << ans << endl;
	}
}
