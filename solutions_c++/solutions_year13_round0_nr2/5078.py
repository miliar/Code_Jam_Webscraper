#include <fstream>
#include <vector>

using namespace std;

main(){
	ifstream fin ("B-large.in");
	ofstream fout ("b.out");
	
	int T;

	fin >> T;

	for(int i = 1; i <= T; i++){
		int N, M;
		fin >> N >> M;

		vector<vector<int> > G;
		for(int n = 0; n < N; n++){
			vector<int> q;
			G.push_back(q);
			for(int m = 0; m < M; m++){
				int t;
				fin >> t;
				G[n].push_back(t);
			}
		}
		bool pathexists = 1;
		for(int ix = 0; ix < N; ix++){
			for(int jx = 0; jx< M; jx++){
				int hij = G[ix][jx];
				for(int p = 0; p < M; p++){
					if(G[ix][p] > hij){
						pathexists = 0;
						break;
					}
				}
				if(!pathexists)
				for(int p = 0; p < N; p++){
					if(G[p][jx] > hij){
						break;
					}
					else if(p == N - 1)
						pathexists = 1;
				}
				if(!pathexists)	break;
			}
			if(!pathexists)	break;
		}
		fout << "Case #" << i << ": ";
		if(pathexists)	fout << "YES";
		else	fout << "NO";
		fout << "\n";
	}
	
	return 0;
}
