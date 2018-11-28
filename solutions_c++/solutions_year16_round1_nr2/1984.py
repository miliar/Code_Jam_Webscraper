#include <bits/stdc++.h>

using namespace std;

int T, cs = 0, N;
vector < vector <int> > V;
int Org[60], pos;
vector <int> Other;

bool cmp (vector <int> A, vector <int> B) {
	return A[pos] < B[pos];
}

int main (int argc, char const *argv[]) {
	//freopen("input.txt", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);	

	scanf("%d", &T); while (T--) {
		scanf("%d", &N);
		V.resize(N + N - 1);
		for (int i = 0; i < N + N - 1; i++) {  
			V[i].clear();
			for (int j = 0; j < N; j++) {
				int x; scanf("%d", &x);
				V[i].push_back(x);
			} 
		}
		pos = 0; 
		for (int i = 0; i < N; i++) {
			sort(V.begin() + i + i, V.end(), cmp);
			pos++;
		}

		/*for (int i = 0; i < N+N-1; i++){
			for (int j = 0; j<N;j++) cout << V[i][j] << " ";
				cout<<endl;
		}*/

		int lost = N - 1;
		for (int i = 0; i < N - 1; i++) {
			int j = i + i;
			if (V[j][i] != V[j + 1][i]) {
				vector <int> blank;
				V.insert(V.begin() + j + 1, blank);
				lost = i;
				break;
			}
		}
		Other = V[lost + lost];

		//cout<<"ss: ";
		//for(int i = 0; i < N; i++) cout << Other[i] << " "; cout <<endl;

		for (int i = 0; i < N; i++) {
			if (i == lost) {
				Org[i] = Other[i];
				continue;
			}
			int j = i + i;
			Org[i] = V[j][lost];
			if (Org[i] == Other[i]) Org[i] = V[j + 1][lost];
		}

		printf("Case #%d: ", ++cs);
		for (int i = 0; i < N; i++) printf("%d ", Org[i]);
		printf("\n");
	}
	return 0;
}

