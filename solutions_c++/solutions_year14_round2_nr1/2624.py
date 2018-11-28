#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>
using namespace std;
typedef long long i64;

int N;
vector<vector<pair<char, int>>> strings;
vector<pair<char, int>> target;

bool make_target()
{
	target.clear();
	for (int j=0;j<strings[0].size();++j) {
		int sum=strings[0][j].second;
		for (int i=1;i<N;++i) {
			if (strings[0].size() != strings[i].size()) return false;
			if (strings[0][j].first != strings[i][j].first) {
				return false;
			}
			sum += strings[i][j].second;
		}
		target.push_back(pair<char, int>(strings[0][j].first, (sum + N/2) / N));
	}
	return true;
}

int solve()
{
	int count = 0;
	for (int i=0;i<N;++i) {
		auto& str = strings[i];
		for (int j=0;j<str.size();++j) {
			count += std::abs(target[j].second - str[j].second);
		}
	}
	return count;
}

int main(int argc, char **argv) {
	FILE *fd = argc > 1 ? fopen(argv[1], "r") : stdin;
	int T; fscanf(fd, "%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {
		fprintf(stderr, "Case #%d of %d...\n", Ti, T);

		fscanf(fd, "%d", &N);

		strings.clear();
		char str[101];
		for (int i=0;i<N;++i) {
			fscanf(fd, "%s", str);
			vector<pair<char, int>> string;
			for (char *p=str; *p != '\0';++p) {
				if (!string.empty() && string.back().first == *p) {
					string.back().second++;
				} else {
					string.push_back(pair<char,int>(*p, 1));
				}
			}
			strings.push_back(std::move(string));
		}

		if (make_target()) {
			printf("Case #%d: %d\n", Ti, solve());
		} else {
			printf("Case #%d: Fegla Won\n", Ti);
		}
	}
	if (fd != stdin) {
		fclose(fd);
	}
	return 0;
}
