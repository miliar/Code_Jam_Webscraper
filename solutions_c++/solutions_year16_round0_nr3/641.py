#include "stdafx.h"
#include <math.h> 
#include <iostream>
#include <fstream>
#include <sstream> 
#include <set> 
#include <map> 
#include <vector> 
#include <list> 
#include <string>
#include <algorithm>
#include <cassert>
#include <bitset>

//Using MPIR from mpir.org
#pragma warning(disable: 4800)
#include <mpirxx.h>
#pragma warning(default: 4800)


using namespace std;

struct JamCoin {
	JamCoin(int size)
	  : size_(size) {
	   init();
	   bits_.set(0);
	   bits_.set(size - 1);
	   if (size_ > 6) {
		   bits_.set(size - 2);
		   bits_.set(size - 3);
		   bits_.set(size - 4);
	   }
	   setNumInBase();
	   setDiv();
    }
	void setNumInBase() {
		for (int i = 0; i < size_; ++i) {
			if (bits_[i]) {
				for (int b = 0; b < 9; ++b) {
					if (!i) numInBase_[b] = 0;
					numInBase_[b] += Bases[b][i];
				}
			}
		}
	}
	void setDiv() {
		//base+1 expected
		for (int b = 0; b < 9; ++b) {
			divs_[b] = b + 3;
		}
	}

	void plus() {
		do {
			bits_ = bitset<32>(bits_.to_ulong() + 1);
		} while (!bits_[0] || !bits_[size_ - 1]);
		setNumInBase();
	}
	bool checkDiv() {
		bool bAllDiv = true;
		for (int b = 0; b < 9; ++b) {
			if (numInBase_[b] % divs_[b] != 0) {
				bAllDiv = false;
				break;
			}
		}
		return bAllDiv;
	}
	bool operator<(const JamCoin& oth) const {
		return bits_.to_ulong() < oth.bits_.to_ulong();
	}
	int size_;
	bitset<32> bits_ = {};
	mpz_class numInBase_[9] = {};
	mpz_class divs_[9] = {};

	 void init() {
		for (int i = 0; i < size_; ++i) {
			for (int b = 0; b < 9; ++b) {
				if (i == 0) Bases[b][i] = 1;
				else {
					Bases[b][i] = b + 2;
					Bases[b][i] *= Bases[b][i - 1];
				}
			}
		}
	}
	mpz_class Bases[9][32];
};

ostream&
operator<<(ostream& os, const JamCoin& coin)
{
	for (int i = coin.size_ - 1; i >= 0; --i) {
		os << coin.bits_[i];
	}

	for (auto& div : coin.divs_) {
		os << " " << div;
	}
	//for (auto& num : coin.numInBase_) {
	//	os << " - " << num;
	//}
	return os;
}

void
PrintResult(int i, const set<JamCoin>& res)
{
	cout << "Case #" << i << ":" << endl;
	for (auto& coin : res) {
		cout << coin << endl;
	}
}

set<JamCoin>
Solve(int size, int num)
{
	JamCoin current(size);
	set<JamCoin> result;

	while (result.size() != num) {
		if (current.checkDiv()) {
			result.insert(current);
		}
		current.plus();
	}
	return result;

}

int
main()
{
	ifstream in("in.txt");
	cin.rdbuf(in.rdbuf());

	ofstream out("out.txt");
	cout.rdbuf(out.rdbuf());

	int T;
	cin >> T;

	for (int i = 1; i <= T; ++i) {
		int size, num;
		cin >> size >> num;
		assert(size <= 32);
		auto r = Solve(size, num);
		PrintResult(i, r);
	}

	return 0;
}
