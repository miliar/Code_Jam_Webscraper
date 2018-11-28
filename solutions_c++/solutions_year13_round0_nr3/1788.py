#include <stdio.h>
#include <algorithm>
using namespace std;

#define MAX_FS 1000010

int t; long long a,b;
long long fsq[MAX_FS];
int fs=0;

bool isPal(long long x) {
	char tmp[20];
	sprintf(tmp,"%lld",x);
	int l=strlen(tmp);

	for (int i=0; i<=l; i++)
		if (tmp[i]!=tmp[l-i-1])
			return false;
	return true;
}

void pre() {
	for (long long x=1; x<10000010; x++) {
		if (!isPal(x)) continue;
		if (isPal(x*x))
			fsq[fs++]=x*x;
	}
}

int main() {
	pre();
	scanf("%d", &t);

	for (int casen=1; casen<=t; casen++) {
		scanf("%lld %lld", &a,&b);

		long long* low = lower_bound(fsq,fsq+fs,a);
		long long* up = upper_bound(fsq,fsq+fs,b);

		printf("Case #%d: %ld\n", casen,up-low);
	} 	

	return 0;
}
