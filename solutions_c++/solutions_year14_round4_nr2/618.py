#include <iostream>
#include <iomanip>
#include <stdio.h>
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

struct num {
	int ind;
	int A;
} B[1000];

inline int cmpB (const void* p1, const void* p2) {
	if (((num*)p1)->A == ((num*)p2)->A) {
		return 0;
	} else {
		return (((num*)p1)->A < ((num*)p2)->A ? -1 : 1);
	}
}

class DynamicSums {
	int N;
	int layers;
	int** data;

	int sumUpToAt(int ind, int l) {
		if (ind == 0) {
			return 0;
		} else if (ind == 1) {
			return data[l][0];
		} else {
			return ((ind % 2 == 1)?data[l][ind - 1]:0) + sumUpToAt(ind/2, l + 1);
		}
	}
public:
	DynamicSums(int N_) {
		int n;
		int l;

		N = N_;

		n = N;
		layers = 1;
		while (n > 1) {
			n = (n / 2) + (n % 2);
			layers++;
		}

		data = new int*[layers];

		n = N;
		for (l = 0; l < layers; l++) {
			data[l] = new int[n];
			n = (n / 2) + (n % 2);
		}
	}

	~DynamicSums() {
		int l;

		for (l = 0; l < layers; l++) {
			delete[] data[l];
		}
		delete[] data;
	}

	void clear(int value) {
		int n,nSize,bSize;
		int l;

		nSize = N;
		bSize = 1;
		for (l = 0; l < layers; l++) {
			for (n = 0; n < nSize; n++) {
				data[l][n] = value*bSize;
			}
			nSize = (nSize / 2) + (nSize % 2);
			bSize *= 2;
		}
	}

	void add(int value, int at) {
		int l;

		for (l = 0; l < layers; l++) {
			data[l][at] += value;
			at /= 2;
		}
	}

	int sumUpTo(int ind) {
		return sumUpToAt(ind,0);
	}
};

int main() {
	int T,N;
	int A[1000];
	int total;
	DynamicSums* sums;

	cin >> T;

	for (int t = 1; t <= T; t++) {
		cin >> N;

		sums = new DynamicSums(N);
		sums->clear(1);

		for (int i = 0; i < N; i++) {
			cin >> A[i];
			(B[i]).ind = i;
			(B[i]).A = A[i];
		}

		qsort(B, N, sizeof(num), cmpB);

		total = 0;
		for (int i = 0; i < N; i++) {
			total += min(sums->sumUpTo(B[i].ind), N - 1 - i - sums->sumUpTo(B[i].ind));
			sums->add(-1, B[i].ind);
		}
		
		cout << "Case #" << t << ": " << total << endl;

		delete sums;
	}

	return 0;
}
