#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int main() {
	//p2[0] = 1;
	//for (int i=1;i<38;i++) {
	//	p2[i] = p2[i-1]*2;
	//}
  int T;

  cin >> T;

  for (int t=1;t<=T;t++) {
    int P;
		cin >> P;

		vector<long long> E(P), F(P);

		for (int i=0;i<P;i++) {
			cin >> E[i];
		}
		for (int i=0;i<P;i++) {
			cin >> F[i];
		}

		vector<int> S;
		while (F[0] != 1) {
			F[0] >>= 1;
			S.push_back(0);
		}
		for (int i=1;i<P;i++) F[i] >>= S.size();

		for (int i=1;i<P;i++) {
			while (F[i] != 0) {
				S.push_back(E[i]);
//cout << "add " << E[i] << endl;
				F[i]--;
				int k=i;
				for (int j=i;j<P;j++) {
					if (F[j]==0) continue;
					while (E[k]<E[j]+E[i]) k++;
					F[k] -= F[j];
				}
//for (int x=0;x<P;x++) cout << F[x] << " "; cout << endl;
//if (S.size() > 10) return 0;
			}
		}

		printf("Case #%d:",t);
		for (int s = 0;s<S.size();s++) printf(" %d",S[s]);
		printf("\n");
		
  }

}
