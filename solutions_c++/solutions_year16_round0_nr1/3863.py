#include <iostream>
#include <unordered_set>

using namespace std;

#define ANSWER(no, x) cout << "Case #" << no << ": " << x << '\n'; return;
#define NO_ANSWER "INSOMNIA"

void solve(int no, int problem){
	if(problem == 0){
		ANSWER(no, NO_ANSWER);
	}
	std::unordered_set<int> found;
	found.reserve(10);
	for(int i = 1; i < 10000000; i++){
		long long cur = i * problem;
		long long copy = cur;
		// cerr << "processing problem " << problem << " count " << i << " number " << cur << '\n';
		while(cur > 0){
			int digit = cur % 10;
			// cerr << "digit " << digit << '\n';
			found.insert(digit);
			cur /= 10;
		}

		if(found.size() == 10){
			ANSWER(no, copy);
		}
	}
	ANSWER(no, NO_ANSWER);
}

int main(int argc, char **argv){
	int count;
	cin >> count;

	for(int i = 0; i < count; i++){
		int problem;
		cin >> problem;
		solve(i+1, problem);
	}
}
