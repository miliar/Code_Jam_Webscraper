#include <stdio.h>
#include <string.h>
#include <vector>
#include <math.h>

__int64 MAX = 10000000000;
int MAX_N = 10;

using namespace std;

struct big {

	__int64 *arr;
	int len;
	char b;
	int last_div;

	big(int n, char base) {
		len = (n / MAX_N + (n % MAX_N ? 1 : 0));
		arr = new __int64[len];
		b = base;


		for(int i = 0; i < len; ++ i) {
			arr[i] = 0;
		}

		arr[0] = 1;

		for(int i = 0; i < n - 1; ++ i) {
			(*this) *= base;
		}

		(*this) += 1;
	}

	void set(vector<char> num) {
		for(int i = 0; i < len; ++ i) {
			arr[i] = 0;
		}

		for(int i = num.size() - 1; i >= 0; -- i) {
			(*this) *= b;

			if(num[i] == '1') {
				arr[0] += 1;
			}		
		}
	}

	void operator*= (char c) {
		int m = 0;
		for(int i = 0; i < len; ++ i) {
			arr[i] = arr[i] * c + m;
			
			if(arr[i] >= MAX) {
				arr[i] -= MAX;
				m = 1;
			} else {
				m = 0;
			}
		}
	} 

	void operator+= (char c) {
		int m = 0;
		arr[0] += c;
		for(int i = 0; i < len; ++ i) {
			arr[i] = arr[i] + m;

			if(arr[i] >= MAX) {
				arr[i] -= MAX;
				m = 1;
			} else {
				return;
			}
		}
	}

	void inc() {
		(*this) += b;
	}

	bool div(__int64 num) {
		__int64 m = 0;
		for(int i = len - 1; i >= 0; -- i) {
			m = (m * MAX + arr[i])%num;
		}
		return m == 0;
	}

	int find_div() {
		if(div(2)) {
			last_div = 2;
			return 2;
		}
		int sq = sqrt((float)arr[0]) +2;

		int realN = 0;
		for(int i = 0; i < len; ++ i) {
			if(arr[i] > 0) {
				realN = i + 1;
			}
		}

		for(int i = 3; i < 1000000 && (realN > 1 || i < sq); i += 2) {
			if(div(i)) {
				last_div = i;
				return i;
			}
		}

		last_div = 0;
		return 0;
	}

	~big() {
		//delete []arr;
	}

	vector<char> print2() {
		vector<char> result;

		for(int i = 0; i < len; ++ i) {
			int copy = arr[i];

			while(copy > 0) {
				result.push_back('0' + (copy & 1));
				copy = copy >> 1;
			}
		}

		return result;
	}
};

int main() {

	FILE* in = fopen("3s.txt", "rb");
	FILE* out = fopen("3s2_out.txt", "wb");

	int n = 0;
	fscanf(in, "%d", &n);

	for(int i = 1; i <= n; ++ i) {
		int N, J;

		fscanf(in, "%d%d", &N, &J);

		vector<big> nums;

		for(char b = 2; b <= 10; ++ b) {
			nums.push_back(big(N, b));
		}

		fprintf(out, "Case #%d:\n", i);

		for(int j = 0; j < J; ++ j) {
			printf("%d...\n", j + 1);
			while(true) {
				bool exist = true;

				for(int k = 0; k < nums.size(); ++ k) {
					if(nums[k].find_div() == 0) {
						exist = false;
						break;
					}
				}

				if(exist) {
					break;
				} 

				nums[0].inc();
				vector<char> seq = nums[0].print2();
				for(int k = 1; k < nums.size(); ++ k) {
					nums[k].set(seq);
				}
			}

			vector<char> num = nums[0].print2();
			for(int c = num.size() - 1; c >= 0; -- c) {
				fprintf(out, "%c", num[c]);
			}

			for(int k = 0; k < nums.size(); ++ k) {
				fprintf(out, " %d", nums[k].last_div);
			}
			fprintf(out, "\n");

			nums[0].inc();
			vector<char> seq = nums[0].print2();
			for(int k = 1; k < nums.size(); ++ k) {
				nums[k].set(seq);
			}
		}
	}

	return 0;
}