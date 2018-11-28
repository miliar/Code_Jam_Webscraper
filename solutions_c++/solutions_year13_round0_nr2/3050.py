#include <iostream>
//#include <algorithm>
using namespace std;

void cs(){
	int a[105][105] = {-1};
	int N, M, i, j, min = 103, posx, posy;
	bool do_x, do_y;
	cin >> N >> M;
	for (i = 0;i < N; ++i)
		for (j = 0;j < M; ++j)
			cin >> a[i][j];
	while (true){
		min = 103;
		for (i = 0;i < N; ++i)
			for(j = 0;j < M; ++j)
				if (a[i][j] < min){
					min = a[i][j];
					posx = i;
					posy = j;
				}
		if (min == 103)
			break;
		do_x = true;
		for (j = 0;j < M; ++j){
			if (a[posx][j] > a[posx][posy] && a[posx][j] != 105){
				do_x = false;
				break;
			}
		}
		do_y = true;
		for (i = 0;i < N; ++i){
			if (a[i][posy] > a[posx][posy] && a[i][posy] != 105){
				do_y = false;
				break;
			}
		}
		if (!do_x && !do_y){
			cout << "NO";
			return;
		}
		if (do_x){
			for (j = 0;j < M; ++j)
				a[posx][j] = 105;
		}
		if (do_y){
			for (i = 0;i < N; ++i)
				a[i][posy] = 105;
		}
	}
	cout << "YES";
}

int main(void){
	int T;
	cin >> T;
	for (int i = 1;i <= T; ++i){
		cout << "Case #" << i << ": ";
		cs();
		cout << endl;
	}
	return 0;
}