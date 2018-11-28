#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int T, X, N;
  cin >> T;
  for (int t=1;t<=T;t++) {
		cin >> N >> X;
		vector<int> files;
		for (int i=0;i<N;i++) {
			int s;
			cin >> s;
			files.push_back(s);
		}
		sort(files.begin(),files.end());

		int a=0, b=files.size();
		int ans=0;

		while (a<b) {
			if (a<b-1 && files[a] + files[b-1] <= X) {
				a++;
			}
			b--;
			ans++;
		}

		printf("Case #%d: ", t);
		printf("%d\n", ans);
	}

  return 0;
}
