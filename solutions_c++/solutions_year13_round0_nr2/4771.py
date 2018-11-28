#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int n,N,M;
	int lawn[101][101];
	cin >> n;
	for(int Case = 1; Case <= n; ++Case){
		int n_max[101] = {},m_max[101] ={};
		bool end_flag = false;
		cin >> N >> M;
		for(int i = 0; i < N; ++i){
			for(int j = 0; j < M; ++j){
				cin >> lawn[i][j];
				n_max[i] = max(n_max[i],lawn[i][j]);
			}
		}
		for(int i = 0; i < M; ++i){
			for(int j = 0; j < N; ++j){
				m_max[i] = max(m_max[i],lawn[j][i]);
			}
		}
		
		for(int i = 0; i < N && !end_flag; ++i){
			for(int j = 0; j < M && !end_flag; ++j){
				if(!(lawn[i][j] >= n_max[i] || lawn[i][j] >= m_max[j])){
					cout << "Case #" << Case << ": NO" << endl;
					end_flag = true;
				}
			}
		}
		
		if(end_flag){
			continue;
		}
		
		cout <<"Case #" << Case << ": YES" <<endl;
	}
}