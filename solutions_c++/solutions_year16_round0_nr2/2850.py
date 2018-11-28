#include <cstdlib>
#include <vector>
#include <cstdio>
#include <string>
#include <iostream>
#include <queue>
#include <unordered_set>
#include <functional>

using namespace std;

int S;

struct conf {
	vector<char> data;
	int steps;
	int weight;
};

namespace std {
    template <>
        class hash<vector<char>>{
        public :
            size_t operator()(const vector<char> &x) const
			{
				int r = 0;
				for (int i=0; i<S; i++) {
					r += x[i] * (1<<i);
				}
				return hash<int>()(r);
            }
    };
};

/*size_t my_hash(const vector<char>& x) {
	int r = 0;
	for (int i=0; i<S; i++) {
		r += x[i] * (1<<i);
	}
	return hash<int>()(r);
}*/

bool operator<(const conf& lhs, const conf& rhs) {
	if (lhs.steps != rhs.steps) {
		return lhs.steps > rhs.steps;
	} else {
		return lhs.weight < rhs.weight;
	}
	/*if (lhs.weight != rhs.weight) {
		return lhs.weight < rhs.weight;
	} else {
		return lhs.steps > rhs.steps;
	}*/
}


bool flip(conf &c, int n) {
	for (int i=0; i<n/2; i++) {
		const auto tmp = c.data[i];
		c.data[i] = c.data[n-1-i] ^ 1;
		c.data[n-1-i] = tmp ^ 1;
	}
	if (n%2 != 0) {
		c.data[n/2] ^= 1;
	}

	//fprintf(stderr,"%d: ", n);
	for (int i=0; i<S; i++) {
		//fprintf(stderr, "%d", c.data[i]);
	}
	//fprintf(stderr,"\n");
	
	c.steps += 1;
	c.weight = -1;
	//fprintf(stderr, "%d ", n);
	for (int i=0; i<S; i++) {
		if (c.data[S-1-i] == 0) {
			c.weight = i;
			//fprintf(stderr, "(%d)\n", n-1-i);
			break;
		}
	}
	if (c.weight == -1) {
		return true;
	} else {
		return false;
	}
}


int main(int argc, char** argv) {
	int Tmax;
	scanf("%d", &Tmax);
	for (int T=1; T<=Tmax; T++) {
		string str;
		cin >> str;
		S = str.size();
		vector<char> stack(S);
		bool done = true;
		for (int i=0; i<S; i++) {
			if (str[i] == '+') {
				stack[i] = 1;
			} else {
				stack[i] = 0;
				done = false;
			}
		}
		if (done) {
			printf("Case #%d: 0\n", T);
			continue;
		}

		unordered_set<vector<char>> bank = {stack};
		priority_queue<conf> q;
		q.push({stack, 0, 0});
		bool found = false;
		while (!found) {
			auto curr = q.top();
			q.pop();
			for (int i=1; i<=S; i++) {
				auto copy = curr;
				if (flip(copy, i)) {
					found = true;
					printf("Case #%d: %d\n", T, copy.steps);
					for (int i=0; i<S; i++) {
						//fprintf(stderr, "%d", copy.data[i]);
					}
					//fprintf(stderr,"\n");
					break;
				}
				
				if (bank.count(copy.data) == 0) {
					bank.insert(copy.data);
					q.push(copy);
				}
			}
		}
	}
	
	return 0;
}

