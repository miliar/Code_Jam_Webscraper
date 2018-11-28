#include<fstream>
#include<iostream>
#include<vector>

using namespace std;

typedef vector<unsigned long long> vull;
typedef unsigned long long ull;

bool is_pal(ull i) {
	vector<int> v;
	while (i) {
		v.push_back(i%10);
		i /= 10;
	}
	int left = 0;
	int right = v.size() - 1;
	while (left < right) {
		if (v[left] != v[right]) {
			return false;
		}
		left++;
		right--;
	}
	return true;
}

int main(int argc, char **argv) {
	vull vec;
	for (ull i = 1; i <= 1e14; ++i) {
		if (i*i > 1e14) {
			break;
		}

		if (is_pal(i)) {
			if (is_pal(i*i)) {
				vec.push_back(i*i);
			}
		}
	}

	ifstream f(argv[1]);
	int case_num;
	f >> case_num;
	case_num++;
	for (int cn = 1; cn < case_num; ++cn) {
		ull start, end;
		f >> start;
		f >> end;
		ull count = 0;
		for (int i = 0; i < vec.size(); ++i) {
			if (vec[i] >= start && vec[i] <= end) {
				count++;
			}
		}
		cout << "Case #" << cn << ": " << count << endl;
	}
	return 0;
}
