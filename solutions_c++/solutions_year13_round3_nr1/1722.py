#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
using namespace std;
typedef long long i64;

int n;
string str;
const char vowels[5] = {'a', 'i', 'u', 'e', 'o'};

bool is_consonants(char c)
{
	for (int j=0;j<5;++j) {
		if (c == vowels[j]) return false;
	}
	return true;
}
bool is_n_consonants(int i)
{
	for (int j=0;j < n;++j) {
		if (i+j >= str.size()) return false;
		if (!is_consonants(str[i+j])) return false;
	}
	return true;
}

int main() {
  int T; scanf("%d", &T);
  for (int Ti = 1; Ti <= T; ++Ti) {
	fprintf(stderr, "Case #%d of %d...\n", Ti, T);

	char buf[101];
	scanf("%s %d", buf, &n);
	str.assign(buf);

	set< pair<int,int> > substrs;
	for (int i=0;i < str.size(); ++i) {
		if (is_n_consonants(i)) {
			for (int f=0;f<=i;++f) {
				for (int l=i+n;l <= str.size(); ++l) {
					substrs.insert(pair<int,int>(f,l));
				}
			}
		}
	}

	printf("Case #%d: %lld\n", Ti, substrs.size());
  }
  return 0;
}
