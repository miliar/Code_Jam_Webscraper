#include<iostream>
using namespace std;

int a[101][101];

pair<int, int> find_min(int N, int M){
	int i, j, x, y, min;
	pair<int, int> k;
	min = 101;
	for (i = 0; i < N; i++){
		for (j = 0; j < M; j++){
			if (a[i][j] < min && a[i][j] >= 0){
				min = a[i][j];
				x = i;
				y = j;
			}
		}
	}
	k.first = x;
	k.second = y;
	return k;
}

int check_lawn(pair<int, int> min, int N, int M){
	int i, flag;
	for (i = 0; i < M; i++){
		if (a[min.first][i] <= a[min.first][min.second]){
			flag = 1; 
			continue;
		}else{
			flag = 2;
			break;
		}
	}
	if (flag == 1)
		return 1;
	for (i = 0; i < N; i++){
		if (a[i][min.second] <= a[min.first][min.second]){
			flag = 2;
			continue;
		}else{
			flag = 3;
			break;
		}
	}
	return flag;
}

void change_matrix(int N, int M, int fg, pair<int, int> min){
	int i;
	if (fg == 1){
		for (i = 0; i < M; i++){
			a[min.first][i] = -1;
		}
	}else if (fg == 2){
		for (i = 0; i < N; i++){
			a[i][min.second] = -1;
		}
	}
}

int confirm(int N, int M){
	int i, j;
	for (i = 0; i < N; i++){
		for (j = 0; j < M; j++){
			if (a[i][j] != -1)
				return 1;
		}
	}
	return 0;
}

int main(){
	int t, T, i, j , k, yes, fg, M, N;
	pair<int, int> min;
	cin >> T;
	for (t = 1; t <= T; t++){
		yes = 1;
		cin >> N;
		cin >> M;
		for (i = 0; i < N; i++){
			for (j = 0; j < M; j++){
				cin >> k;
				a[i][j] = k;
			}
		}
		while(confirm(N, M)){
			min = find_min(N, M);
			fg = check_lawn(min, N, M);
			if (fg != 3)
				change_matrix(N, M, fg, min);
			else{
				cout << "Case #" << t << ": NO" << "\n";
				yes = 0;
				break;
			}
		}
		if (yes == 1)
			cout << "Case #" << t << ": YES" << "\n";
	}
	return 0;
}
