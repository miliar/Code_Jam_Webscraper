#include <cstdio>

using namespace std;

typedef long long lld;

char buff[20];
bool isPalin(lld v) {
	int len = sprintf(buff, "%lld", v);
	for (int i=0; i<len; i++) {
		if (buff[i] != buff[len-i-1]) return false;
	}
	return true;
}

/*
 **precalculated sequence in python((
	def isPalin(s):
		return s == s[::-1]
	
	for i in range(1, 10000000+1) :
		if isPalin(str(i)) :
			if isPalin(str(i*i)) :
				print "%d, " % (i*i)
				ct = ct+1
*/

lld seq[] = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004, 0, 0, 0, 0, 0, 0, 0, 0};

int main() {
	freopen("big1in.txt", "r", stdin);
	freopen("big1out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int ti=0; ti<t; ti++) {
		lld a, b;
		scanf("%lld%lld", &a, &b);
		int count = 0;
		for (int i=0; i<39; i++) {
			if (seq[i] >= a && seq[i] <= b) {
				count++;
			}
		}
		printf("Case #%d: %d\n", ti+1, count);
	}
	return 0;
}