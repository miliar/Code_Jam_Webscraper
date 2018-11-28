#include <iostream>
#include <memory>
#include <list>
#include <cstdint>

using namespace std;

struct elem {
	const long base;
	long cur;
	int div;

	elem(long base) : base(base), cur(base), div(1) {
	}

	long incdiv() {
		div++;
		cur = base / div;
		if (cur * div < base)
			cur++;
		return cur;
	}
};

long nextcycle(list< unique_ptr<elem> > &elems) {
	auto first = move(*elems.begin());
	(*first).incdiv();
	auto cur = (*first).cur;
	elems.pop_front();
	for (auto it = elems.begin();; it++) {
		if (it == elems.end() || (**it).cur <= cur) {
			elems.insert(it, move(first));
			break;
		}
	}
	return (**elems.begin()).cur;
}

uint64_t process(list< unique_ptr<elem> > &elems) {
	long splits = 0, res = (**elems.begin()).base;
	bool improved = true;
	while (improved) {
		/*
		auto thisres = nextcycle(elems) + (++splits);
		if (thisres >= res)
			return res;
		res = thisres;
		*/
		improved = false;
		for (int i = 0; i < elems.size(); i++) {
			auto thisres = nextcycle(elems) + (++splits);
			if (thisres < res) {
				improved = true;
				res = thisres;
			}
		}
	}
	return res;
}

int main(int argc, char *argv[]) {
	/*for (auto it = a.begin();; it++) {
		if (it == a.end() || (*it) > ins) {
			a.insert(it, ins);
			break;
		}
	}*/
	int cnum;
	cin >> cnum;
	for (int ic = 0; ic < cnum; ic++) {
		list< unique_ptr<elem> > elems;
		int en;
		cin >> en;
		for (int ie = 0; ie < en; ie++) {
			long cur;
			cin >> cur;
			auto e = new elem(cur);
			for (auto it = elems.begin();; it++)
				if (it == elems.end() || (**it).base <= cur) {
					elems.insert(it, move(unique_ptr<elem>(e)));
					break;
				}
		}
		cout << "Case #" << ic+1 << ": " << process(elems) << endl;
	}
}