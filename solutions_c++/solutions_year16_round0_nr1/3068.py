#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[]){
	freopen("C:\\Users\\Paramdeep Singh\\Desktop\\A-large.in","r",stdin);
	freopen("C:\\Users\\Paramdeep Singh\\Desktop\\output.txt","w",stdout);
	int cases;
	scanf("%d", &cases);

	for(int c=1; c<=cases; c++) {
		int n;
		scanf("%d", &n);

		if(n == 0) {
			printf("Case #%d: INSOMNIA\n", c);
			continue;
		}
  		int val = 0;
  		long long ans;
        for(int mul=1; ; mul++) {
        	long long temp = 1LL * mul * n;
        	string s = to_string(temp);
        	for(int i=0; i<s.size(); i++) {
        		val |= (1 << (s[i]-'0'));
        	}
        	if(val == ((1<<10)-1)) {
        		ans = temp;
        		break;
        	}
        }
        printf("Case #%d: %lld\n", c, ans);
	}
	return 0;
}