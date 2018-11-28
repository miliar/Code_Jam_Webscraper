#include<iostream>
#include<string>
#define f first
#define s second
#define mp make_pair
using namespace std;

int T, r, c;

char grid[100][100];

string dirc = ">v<^";
pair<int, int> move[4] = {mp(0, 1), mp(1, 0), mp(0, -1), mp(-1, 0)};

pair<int, int> operator+(pair<int, int> l, pair<int, int> r) {
	return mp(l.f + r.f, l.s + r.s);
}




int main() {
	cin.sync_with_stdio(false);
	
	cin >> T;
	
	for(int TCASE = 0; TCASE < T ; TCASE++) {
		cin >> r >> c;
		
		for(int i=0;i<r;i++)
			for(int j=0;j<c;j++)
				cin >> grid[i][j];
				
		
		
		
		int result = 0;
		
		for(int sy = 0; sy < r && result != -1; sy++)
			for(int sx = 0; sx < c && result != -1; sx++) {
				pair<int, int> curp = mp(sy, sx);
				
				if(grid[curp.f][curp.s] == '.')
					continue;
				
				
				int curd = dirc.find(grid[curp.f][curp.s]);
				
				//Next check if it goes over the edge
				
				bool crosses = true;
				
				curp = curp + move[curd];
				
				while(curp.f >= 0 && curp.f < r && curp.s >= 0 && curp.s < c) {
					if(grid[curp.f][curp.s] != '.') {
						crosses = false;
						break;
					}
					curp = curp + move[curd];
				}
				
				
				if(!crosses)
					continue;
					
					
				//Finally check whether it is possible to fix the arrow
				
				for(int d=0; d < 4; d++) {
					curp  = mp(sy, sx) + move[d];
					
					while(curp.f >= 0 && curp.f < r && curp.s >= 0 && curp.s < c) {
						if(grid[curp.f][curp.s] != '.') {
							crosses = false;
							break;
						}
						curp = curp + move[d];
					}
				}
				
				result++;
				
				if(crosses)
					result = -1;
				
			}
		
		
		cout << "Case #" << TCASE + 1 << ": ";
		
		if(result == -1)
			cout << "IMPOSSIBLE\n";
		else
			cout << result << '\n';
	}
	
	return 0;
}

































