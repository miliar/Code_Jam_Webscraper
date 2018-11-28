#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

bool f[10];
int cnt = 0;

void mark(int n) {
	if(n == 0){
		if(f[0] == false) {
			f[0] = true;
			cnt ++;
		}
		return;
	}
	while(n) {
		if(f[n%10] == false){
			cnt++;
			f[n%10] = true;
		}
		n/=10;
	}
}

int main()
{
	int t,cas = 1;
	scanf("%d",&t);
	while(t--) {
		int n;
		scanf("%d",&n);
		if(n == 0)
			printf("Case #%d: INSOMNIA\n",cas++);
		else {
			memset(f,0,sizeof(f));
			cnt = 0;
			long long tmp = 0;
			while(cnt < 10) {
				tmp += 1ll * n;
				mark(tmp);	
			}
			printf("Case #%d: %lld\n",cas++,tmp);
		}	
	}
	return 0;
}

