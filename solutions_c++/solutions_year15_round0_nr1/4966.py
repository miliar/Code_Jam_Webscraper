#include <bits/stdc++.h>

using namespace std;

int main(){
	int t,tmax,count,smax,si,sum;
	string s;
	char c;
	scanf("%d",&t);
	tmax = t;
	while(t--){
		sum = 0;
		count = 0;
		smax = 0;
		scanf("%d",&smax);
		cin >> s;
		for(int i = 0; i <= smax; i++){
			si = (int)(s[i] - '0');
			if((count + sum < i) && (si > 0)) count += (i - sum);
			sum += si;
		}
		printf("Case #%d: %d\n",tmax - t, count);
	}
}