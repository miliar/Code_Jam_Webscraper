#include <iostream>
#include <string>
#include <cmath>

using namespace std;

template <typename T, size_t n>
struct fenwick {
	T tree[n+1];	
  size_t find_bit_mask;
	fenwick() {
		this->clear(n);
		find_bit_mask = n;
		while (find_bit_mask - (find_bit_mask & -find_bit_mask))
			find_bit_mask -= find_bit_mask & -find_bit_mask;
	}
	fenwick& clear(size_t x=n) {
		fill(tree, tree+x+1, static_cast<T>(0));
	}
	fenwick& update(size_t idx, const T& val) {
		while (idx <= n) {
			tree[idx] += val;
			idx += idx & -idx;
		}
		return *this;
	}

	T cumulative_freq(size_t idx) {
		T sum = T(0);
		while (idx) {
			sum += tree[idx];
			idx -= idx & -idx;
		}
		return sum;
	}

	T freq(size_t idx) {
	/*
		T sum = tree[idx];
		if (idx > 0) {
			size_t z = idx - idx & -idx;
			--idx;
			while (idx != z) {
				sum -= tree[idx];
				idx -= idx & -idx;
			}
		}
		return sum;
	*/
		T sum = tree[idx];
		if (idx > 0) {
			return cumulative_freq(idx) - cumulative_freq(idx-1);
		} else return sum;	
	}

	fenwick& scale(const T c) {
		for (size_t i = 1; i <= n; ++i)
			tree[i] = tree[i] * c;
	}

	size_t find(T cf) {
		size_t idx = 0;
		size_t mask = this->find_bit_mask;
		while ((mask != 0) && (idx < n)) {
			size_t tIdx = idx + mask;
			if (cf >= tree[tIdx]) {
				idx = tIdx;
				cf -= tree[tIdx];
			}
			mask >>= 1;
		}
		if (cf) return -1;
		else return idx;
	}

	void print() {
		cerr << "t\t";
		for (size_t i = 0; i < 8; ++i) {
			cerr << tree[i] << "\t";
		}
		cerr << endl;
		cerr << "f\t";
		for (size_t  i = 0; i < 8; ++i) {
			cerr << this->freq(i) << '\t';
		}
		cerr <<endl;
		cerr << "c\t";
		for (size_t i = 0; i < 8; ++i) 
			cerr << this->cumulative_freq(i) << '\t';
		cerr <<endl;
	}

};

int digits[1024];
bool is_palindrome(size_t i) {
	int j = 0;
	for (j; i; ++j) {
		digits[j] = i%10;
		i = (i-digits[j])/10;
	}
	--j;
	bool f = true;
	for (int k = 0; k <= j/2; ++k) {
		//cerr << digits[k] << " != " << digits[j-k] << " k == " << k << ", j == " << j << ", j-k == " << (j-k) << endl;
		if (digits[k] != digits[j-k]) f =  false;
	}
	return f;
}

int main() {
	fenwick<long int, 1024> f;
	for (int i = 1; i <= 1000; ++i) {
		if (is_palindrome(i))
			if (is_palindrome(i*i))
				f.update(i*i, 1);
	}
//	cout << "is_palindrome(121) == " << is_palindrome(121) << endl;
	int T;
	cin >> T;
	for (int kase = 1; kase <= T; ++kase) {
		int a,b;
		cin >> a >> b;
		cout << "Case #" << kase << ": " << (f.cumulative_freq(b) - f.cumulative_freq(a - 1)) << endl;
	}
}
