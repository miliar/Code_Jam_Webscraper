#include <vector>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <math.h>
#include <set>

#ifndef min
#define min(A,B) (B < A) ? B : A
#endif
#ifndef max
#define max(A,B) (B > A) ? B : A
#endif
#ifndef s
#define s(...) fscanf(in, __VA_ARGS__)
#endif
#ifndef r
#define r(...) fscanf(in, __VA_ARGS__)
#endif
#ifndef p
#define p(...) fprintf(out, __VA_ARGS__)
#endif
#ifndef w
#define w(...) fprintf(out, __VA_ARGS__)
#endif
#ifndef MAX_S
#define MAX_S 1000123
#endif


using namespace std;
typedef long long ll;
typedef unsigned long long llu;
typedef set<pair<int, int> > Tp;

FILE *in, *out;
int n;
char s[MAX_S];
Tp p1, p2, p3;

int run() {
	int s_size = (int)strlen(s), cont = 0, i;
	p1.clear();
	for(i = 0; i < s_size; ++i) {
		if (s[i] != 'a' && s[i] != 'e' && s[i] != 'i' &&
		s[i] != 'o' && s[i] != 'u') {
			cont++;
		} else {
			if (cont >= n)
				p1.insert(make_pair(i-cont, i-1));
			cont = 0;
		}
	}
	if (cont >= n)
		p1.insert(make_pair(i-cont, i-1));
	p2.clear();
	for(Tp::iterator it = p1.begin(); it != p1.end(); ++it)
		for(int i = it->first; i <= it->second+1-n; ++i) {
			p2.insert(make_pair(i, i+n-1));
		}
	p3.clear();
	for(Tp::iterator it = p2.begin(); it != p2.end(); ++it)
		for(int i = 0; i <= it->first; ++i) {
			for(int j = it->second; j < s_size; ++j) {
				p3.insert(make_pair(i, j));
			}
		}
	//for(Tp::iterator it = p3.begin(); it != p3.end(); ++it)
	//	p("%d-%d\n", it->first, it->second);
	return p3.size();
}

int counter = 0;
void make() {
    p("Case #%d: ", ++counter);
    r("%s %d", s, &n);
	int res = run();
	p("%d\n", res);
}

void preprocessing() {}

int main() {
    preprocessing();
	in = fopen("A-small-attempt0.in", "r");
	out = fopen("A.out", "w");
    int t; s("%d", &t);
    while(t--) {
        make();
    }
	fclose(in);
	fclose(out);
    return 0;
}
