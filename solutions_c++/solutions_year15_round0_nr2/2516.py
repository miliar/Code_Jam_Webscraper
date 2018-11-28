
#include <iostream>
#include <cstring>

using namespace std;

class Panc {
	private:
		short counts[1001];
		short max;
	public:
		short getTime() const { return max; }
		
		void put(short size) {
			counts[size]++;
			if (max < size) max = size;
		}

		void brk(short parts) {
			short size = max / parts;
			short left = max % parts;
			for (int i = 0; i < parts; i++) {
				counts[size + (i < left ? 1 : 0)]++;
			}
			counts[max]--;
			while (counts[max] == 0) max--;
		}

		Panc() {
			max = 0;
			memset(counts, 0, sizeof(short) * 1001);
		}

		Panc(const Panc &p) {
			max = p.max;
			memcpy(counts, p.counts, sizeof(short) * 1001);
		}
};


short sqrt[1001];
short best_time;


void compute_sqrt() {
	for (int i = 0; i < 1001; i++) {
		short res = 1;
		while (res * res <= i) {
			res++;
		}
		//cout << "sqrt of " << i << " = " << res << endl;
		sqrt[i] = res;
	}
}


short solve(short time, const Panc &p) {
	short t = p.getTime();
	if (time >= best_time) return time + t;

	short upto = sqrt[t];
	short best = time + t;
	//cout << "for time " << t << " breaking in up to " << upto << " pieces" << endl;
	for (int i = 2; i < upto; i++) {
		Panc p2(p);
		p2.brk(i);
		short nt = solve(time + i - 1, p2);
		//cout << "Breaking into " << i << " parts will lead to time " << nt << endl;
		if (nt < best) best = nt;
	}
	if (best_time > best) best_time = best;
	return best;
}


int main() {
	compute_sqrt();

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		Panc p;
		int D;
		cin >> D;
		for (int i = 0; i < D; i++) {
			short x;
			cin >> x;
			p.put(x);
		}
		best_time = p.getTime();
		cout << "Case #" << t << ": " << solve(0, p) << endl;
	}
}

