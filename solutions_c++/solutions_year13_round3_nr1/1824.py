// Consonants

#include <cstdio>
#include <string.h>
#include <stack>
#include <vector>
#include <algorithm>

#define LL long long int
#define DEBUG(...)
//#define DEBUG(...) fprintf(stderr, __VA_ARGS__)

using namespace std;

int T;

vector<bool> C;
char s[1000005];
LL n;
LL L;

void readInput() {
	scanf("%s %lld", s, &n);
	C.clear();
	for (char* p = s; *p != '\0'; ++p) C.push_back(!(*p=='a' || *p=='e' || *p=='i' || *p=='o' || *p=='u'));
	L = C.size();
}

LL solve() {
	LL res = 0;
	for (int start=0; start<L; ++start) {
		for (int l=1; start+l<=L; ++l) {
			LL c=0;
			bool last = false;
			for (int i=start; i<start+l; ++i) {
				if (last && C[i]) {
					c++;
				} else if (C[i]) {
					c = 1;
				} else {
					c = 0;
				}
				if (c >= n) {
					res++;
					break;
				}
				last = C[i];
				//if (!last) c = 0;
			}
		}
	}
	return res;
}
/*
LL solveDP() {
	LL cs = 0; //current solution (0..i)
	LL cc = 0; //consecutive consonants ending at i
	for (int i=1; i<L; ++i) {
		// don't use i:
		LL newcs = cs;
	}

	return cs;
}
*/
int main() {
   scanf("%d ", &T);
   for (int i=1; i<=T; ++i) {
      readInput();
      printf("Case #%d: %lld\n", i, solve());
   }
   return 0;
}

