#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
	freopen("A-small-attempt1.in.txt","r",stdin);
	freopen("A-small.out","w",stdout);
	int T,r,t;
	cin >> T;
	int z=0;
	while(T--){
		cin >> r >> t;
		int sum = 0;
		int ret = 0;
		int i = 0;
		while(sum<=t){
			sum += (r+i+1)*(r+i+1) - (r+i)*(r+i);
			i+=2;
			ret ++;
		}
		printf("Case #%d: %d\n",++z,ret-1);
	}
	return 0;
}
