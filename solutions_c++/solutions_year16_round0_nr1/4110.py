#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
using namespace std;
int T,n;

int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin>>T;
	for (int _t=1;_t<=T;_t++) {
		cin>>n;
		int s=0,cur,i;
		for (i=1;i<=100;i++) {
			cur=n*i;
			while (cur) {
				s|=1<<(cur%10);
				cur/=10;
			}
			if (s==(1<<10)-1) break;
		}
		if (i<=100) printf("Case #%d: %d\n",_t,n*i);
		else printf("Case #%d: INSOMNIA\n",_t);
	}
	//while(1);
	return 0;
}
