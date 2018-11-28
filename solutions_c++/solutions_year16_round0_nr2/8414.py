#include <bits/stdc++.h>

using namespace std;

typedef bitset<10> bset;

typedef pair<bset, int> pbi;

typedef unsigned long ul;

int main(){
	int cases;
	scanf("%d", &cases);

	for(int e = 0; e<cases; e++){

		string raw;
		cin >> raw;

		int S = raw.size();

		vector<int> visited(1<<S, -1);

		bset bs;
		for(int i = 0; i<S; i++){
			if(raw[i] == '+'){
				bs[i] = 1;
			}
		}

		queue<pbi> que;
		que.push(pbi(bs, 0));

		while(!que.empty()){
			pbi node = que.front();
			que.pop();

			// printf("\nPopped "); for(int i = 0; i<S; i++) cout << node.first[i]; cout << endl;

			bset bs = node.first;
			ul bs_ul = node.first.to_ulong();
			int dist = node.second;

			if(visited[bs_ul] != -1){
				continue;
			}
			visited[bs_ul] = dist;

			if(bs_ul == (1<<S)-1){
				break;
			}

			for(int cut = 0; cut<S; cut++){

				// printf("Cutting until %d\n", cut);

				bset next_bs = bs;
				for(int j = 0; j<=cut; j++){
					next_bs[cut-j] = bs[j] ^ 1;
					// printf("Next bs[%d] set to %d from bs[%d] ", cut-j, bs[j] ^1, j); cout << bs[j] << endl;
				}

				ul next_ul = next_bs.to_ulong();
				// printf("Looking next: "); for(int i = 0; i<S; i++) cout << next_bs[i]; cout << endl;
				// printf("Next ul is %lu\n", next_ul);
				// cout << "Next ul is " << next_ul << endl;
				if(visited[next_ul] != -1){
					continue;
				}
				// printf("Pushing "); for(int i = 0; i<S; i++) cout << next_bs[i]; cout << endl;
				que.push(pbi(next_bs, dist+1));
			}
		}

		printf("Case #%d: %d\n", e+1, visited[(1<<S)-1]);


	}

	return 0;

}