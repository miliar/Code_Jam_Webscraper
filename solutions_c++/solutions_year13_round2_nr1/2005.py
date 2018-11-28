#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

void absorb(int& A, vector<int>& motes) {
                bool smaller = true;
                while(smaller) {
                        bool inc = false;
                        for (int j = 0; j < motes.size(); ++j) {
                                if (A > motes[j]) {
                                        A += motes[j];
                                        motes.erase(motes.begin()+j);
                                        inc = true;
                                        break;
                                }
                        }   
                        if (!inc) smaller = false;
                };
}

int inc(int A, int N, vector<int> motes) {
	for (int i = 0; i < N; i++) {
		A += A-1;
		absorb(A,motes);
	}
	return A;
}
	

int main () {
        int T;  
        cin >> T;
        string line;
        getline(cin,line);
        for (int i = 0; i < T; ++i) {
		int A, N;
		cin >> A >> N;
		getline(cin,line);
		vector<int> motes;
		for (int j = 0; j < N; ++j) {
			int tmp;
			cin >> tmp;
			motes.push_back(tmp);
		}
		sort(motes.begin(), motes.end());
                getline(cin,line);
		absorb(A,motes);
		int count = 0;

		N = motes.size();

		while (motes.size() > 1 && count < N) {
			count++;
			A += A-1;
			absorb(A,motes);
			if (motes.size() == 0) break;
		}
	
		int tmp = count+motes.size();
                cout << "Case #" << i+1 << ": " << min(N,tmp) <<endl;
        }   
}
