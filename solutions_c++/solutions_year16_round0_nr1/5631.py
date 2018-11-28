#include <cstdio>
#include <vector>

bool hasFalse(const std::vector<bool>& v) {
	for (unsigned i=0; i<v.size(); ++i) {
		if (!v[i]) {
			return true;
		}
	}
	return false;
}

int main(int argc, char **argv) {

	unsigned T;
	scanf("%u\n",&T);
	for (unsigned i=0; i<T; ++i) {
		int N;
		scanf("%d\n",&N);
		if (N == 0) {
			printf("Case #%u: INSOMNIA\n",i+1);
			continue;
		}
		std::vector<bool> found(10,false);
		int S = 0;
		while(hasFalse(found)) {
			S += N;
			char buf[20];
			snprintf(buf,20,"%u",S);
			unsigned j = 0;
			while(buf[j]) {
				found[buf[j]-'0'] = true;
				++j;
			}
		}
		printf("Case #%u: %d\n",i+1,S);
	}

	return 0;
}



