#include<cstdio>
#include<algorithm>

using namespace std;
const int MAX = 128;

bool res;
int px, py, top;
int casos, rows, columns;
int m[MAX][MAX], t[MAX][MAX];

int main(){
	scanf(" %d", &casos);
	for(int inst=1;inst<=casos;inst++){
		scanf(" %d %d", &rows, &columns);
		top = -1;
		for(int i=0;i<rows;i++){
			for(int j=0;j<columns;j++){
				t[i][j] = 100;
				scanf(" %d", &m[i][j]);
				if(m[i][j] > top){
					top = m[i][j];
					py = i;
					px = j;
				}
			}
		}
		
		for(int i=0;i<rows;i++)
			for(int j=0;j<columns;j++)
				t[i][j] = min(m[i][px], t[i][j]);
		for(int j=0;j<columns;j++)
			for(int i=0;i<rows;i++)
				t[i][j] = min(m[py][j], t[i][j]);
				
		res = true;
		for(int i=0;i<rows;i++)
			for(int j=0;j<columns;j++)
				if(t[i][j] != m[i][j]) res = false;
		printf("Case #%d: %s\n", inst, res ? "YES" : "NO");
	}
	return 0;
}