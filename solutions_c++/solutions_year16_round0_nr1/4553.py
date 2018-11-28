#include <cstdio>
#include <cstdlib>
#include <set>

using namespace std;

typedef long long ll;

void printset(set<int> s) { for (int i : s) printf("%d ", i); printf("\n");}

int main() {
	FILE *in;
	FILE *out;
	in = fopen("input.txt", "r");
	out = fopen("output.txt", "w");
	int T;
	fscanf(in, "%d", &T);
	for (int t = 0; t < T; t++) {
		set<int> seen;
		char buffer[100];
		fscanf(in, "%s", buffer);
		ll n = strtoll(buffer, nullptr, 10);
		if (n==0){
			 fprintf(out, "Case #%d: INSOMNIA\n", t+1);
			 continue;
		 }
		ll n1 = n;
		while ((int)seen.size() < 10) {
			char* c = buffer;
			while (*c) {
				seen.insert((int)((*c++)-'0'));
			}
			n1 += n;
			sprintf(buffer, "%lld", n1);
		}
		n1 -= n;
		sprintf(buffer, "%lld", n1);
		fprintf(out, "Case #%d: %s\n",t+1 , buffer);
	}
}
