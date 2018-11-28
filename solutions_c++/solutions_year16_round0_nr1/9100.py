
#include<cstdio>
#include<cmath>
#include<cstring>
#include<string>
#include<iostream>
#include<algorithm>

using namespace std;
bool x[10];
bool digits() {
	for (int i = 0; i < 10; i++)
		if (!x[i])
			return 0;
	return 1;
}
int main() {
	freopen("A-large.in","r",stdin);
	int n, t,c=1;
	int temp, i;
	scanf("%d", &t);
	while (t--) {
		scanf("%d", &n);
		if(!n){
			printf("Case #%d: INSOMNIA\n",c++);
			continue;
		}
		for(int i=0;i<10;i++)
			x[i]=0;
		for (i = n; !digits(); i += n) {
			temp = i;
			while (temp) {
				x[temp % 10] = 1;
				temp /= 10;
			}
		}
		printf("Case #%d: %d\n",c++, i - n);
	}
	return 0;
}
