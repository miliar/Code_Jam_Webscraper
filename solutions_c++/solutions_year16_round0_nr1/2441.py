#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cmath>
using namespace std;

const int maxn = 1 << 20;
int ans[maxn]={};
int main(){
	int T;
	ans[0] = -1;
	for(int i=1;i<maxn;i++){
		int mask = 0;
		int c = 0;
		while(mask != (1<<10)-1){
			c += i;
			int d = c;
			while(d){
				int dig = d % 10;
				d /= 10;
				mask |= 1 << dig;
			}
			ans[i]++;
		}
		ans[i] *= i;
		// if(i%10000==0)
			// cout << i << endl;
	}
	cin >> T;
	for(int t = 0; t<T; t++){
		int a;
		cin >> a;
		printf("Case #%d: ", t+1);
		if(a == 0)
			cout << "INSOMNIA" << endl;
		else
			cout << ans[a] << endl;
	}
}