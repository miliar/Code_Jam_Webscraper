#include <stdio.h>
#include <queue>

class Barber {
public:
	int id;
	long long time;

	bool operator<(const Barber& other) const
	{
		if (time > other.time) {
			return true;
		} else if (time < other.time) {
			return false;
		} else {
			if (id > other.id) {
				return true;
			} else {
				return false;
			}
		}
	}
};

int m[1001];
int main(void)
{
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int B;
		unsigned long long N;
		scanf("%d %llu", &B, &N);
		for (int i=0; i<B; i++) {
			scanf("%d", &m[i]);
		}
		unsigned long long k = 1ULL<<55;
		unsigned long long d = 0;
		unsigned long long bf = 0;
		for (; k; k >>= 1) {
			unsigned long long dd = d|k;
			unsigned long long sum = 0;
			for (int i=0; i<B; i++) {
				sum += (dd-1)/m[i]+1;
			}
			if (sum < N) {
				d = dd;
				bf = sum;
			}
		}
		int last = 0;
		int NN = N - bf;
		int cnt = 0;
		for (int i=0; i<B; i++) {
			if (d%m[i] == 0) {
				cnt++;
			}
			if (cnt == NN) {
				last = i;
				break;
			}
		}
		/*
		std::priority_queue<Barber> q;
		for (int i=0; i<B; i++) {
			Barber bb;
			bb.id = i;
			bb.time = m[i]-(d+1)%m[i];
			q.push(bb);
		}
		int last = 0;
		int NN = N - bf;
		for (int i=0; i<NN; i++) {
			Barber bb = q.top();
			bb.time += m[bb.id];
			last = bb.id;
			q.pop();
			q.push(bb);
		}
		*/

		printf("Case #%d: %d\n", t, last+1);
	}
	return 0;
}
