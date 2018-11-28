#include <iostream>
#include <cstdlib>

#ifdef _WIN32
#define LL "%I64d"
#else
#define LL "%lld"
#endif

#define inp(x) scanf("%d",&x)
#define inpf(x) scanf("%f",&x)

using namespace std;

typedef long long int ll;
typedef long long unsigned int ull;

int cmp (const void* p1, const void* p2) {
	if (*(double*) p1 == *(double*) p2) {
		return 0;
	} else {
		return (*(double*) p1 < *(double*) p2 ? -1 : 1);
	}
}

int main() {
	int T,N;
	double Naomi[1000];
	double Ken[1000];
	int s1;
	int s2;
	int i,j;

	cin >> T;

	for (int t = 1; t <= T; t++) {
		cin >> N;

		for (int n = 0; n < N; n++) {
			cin >> Naomi[n];
		}
		qsort(Naomi, N, sizeof(double), cmp);

		for (int n = 0; n < N; n++) {
			cin >> Ken[n];
		}
		qsort(Ken, N, sizeof(double), cmp);

		s1 = 0;
		i = 0;
		j = 0;
		while (i < N && j < N) {
			if (Naomi[i] < Ken[j]) {
				i++;
				j++;
			} else {
				j++;
				s1++;
			}
		}

		s2 = 0;
		i = 0;
		j = 0;
		while (i < N && j < N) {
			if (Naomi[i] > Ken[j]) {
				i++;
				j++;
				s2++;
			} else {
				i++;
			}
		}

		cout << "Case #" << t << ": " << s2 << " " << s1 << endl;
	}

	return 0;
}
