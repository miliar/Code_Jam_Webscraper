#include <cstdio>

using namespace std;

const int dx[] = {0, 1, 1, 1, 0, -1, -1, -1};
const int dy[] = {-1, -1, 0, 1, 1, 1, 0, -1};

int main(){
	int n;
	scanf("%d", &n);
	for(int T = 0; T < n; T++){
		char masu[5][5];
		for(int i = 0; i < 4; i++){
			scanf("%s", masu[i]);
		}
		bool emp = false;
		int result = 0;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				if(masu[i][j] == '.'){
					emp = true;
					continue;
				}
				for(int k = 0; k < 8; k++){
					int cnt = 0;
					for(int l = 0; l < 4; l++){
						int nx = j+dx[k]*l, ny = i+dy[k]*l;
						if(nx < 0 || nx >= 4 || ny < 0 || ny >= 4) break;
						char c = masu[ny][nx];
						if(masu[i][j] == c || c == 'T') cnt++;
					}
					if(cnt == 4) result = (masu[i][j] == 'X')?1:2;
				}
				if(result != 0) break;
			}
			if(result != 0) break;
		}
		if(result == 0 && !emp) printf("Case #%d: Draw\n", T+1);
		if(result == 0 && emp) printf("Case #%d: Game has not completed\n", T+1);
		if(result == 1) printf("Case #%d: X won\n", T+1);
		if(result == 2) printf("Case #%d: O won\n", T+1);
	}
	
	return 0;
}