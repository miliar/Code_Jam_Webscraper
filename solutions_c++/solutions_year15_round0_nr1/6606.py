#include <iostream>
using namespace std;

int main() {
	int t;
	scanf("%d",&t);
	for(int cas = 1; cas<=t; cas++) {
		int n;
		scanf("%d",&n);
		char str[n+1];
		scanf("%s",&str);
		int total = 0;
		int reqd = 0;
		for(int i=0; i<=n; i++) {
			if(total>=i) total += (str[i]-'0');
			else {
				reqd += i-total;
				total+=((i-total)+(str[i]-'0'));
			}
		}
		printf("Case #%d: %d\n",cas, reqd);
	}
	return 0;
}