#include <iostream>
using namespace std;

bool isSafe(int*, int, int, int, int);
int main()
{
	int T, N, M;
	int case_id,i,j;
	int* map;
	cin >> T;
	for (case_id = 1; case_id <= T; case_id++) {
		cin >> N >> M;
		map = new int[N*M];
		for (i = 0; i < N; i++)
			for (j = 0; j < M; j++)
				cin >> map[i*M + j];

		for (i = 0; i < N; i++)
			for (j = 0; j < M; j++) {
				if (!isSafe(map, i, j, N, M)) {
					cout << "Case #" << case_id << ": NO" << endl;
					goto end;					
				}
			}

		cout << "Case #" << case_id << ": YES" << endl;
end:
		delete [] map;
	}	

}

bool isSafe(int* map, int i, int j, int N, int M)
{
	int value = map[i*M + j];
	bool flag = false;
	for(int k = 0; k < N; k++) 	
		if (value < map[k*M + j])
			flag = true;
	for(int k = 0; k < M; k++) 	
		if (value < map[i*M + k] && flag)
			return false;

	return true;

}
