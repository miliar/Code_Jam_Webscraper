#include <fstream>
#include <utility>
#include <set>

using namespace std;

int main(){
	ifstream fin ("A-small-attempt1.in");
	ofstream fout ("A-output.txt");
	int T, R, C, a, n, x;
	fin >> T;
	char grid[100][100];
	for(int i = 1; i <= T; i++){
        fin >> R >> C;
        n = 0;
        for(x = 0; x < R; x++){
            fin >> grid[x];
            //fout << grid[x] << '\n';
        }
        for(x = 0; x < R; x++){
            for(int y = 0; y < C; y++){
                if(grid[x][y] == '^'){
                    for(a = x-1; a >= 0; a--){
                        if(grid[a][y] != '.') break;
                    }
                    if(a == -1){
                        //fout << x << ' ' << y << '\n';
                        for(a = x+1; a < R; a++)
                            if(grid[a][y] != '.') break;
                        if(a != R){
                            n++;
                            continue;
                        }
                        for(a = y-1; a >= 0; a--)
                            if(grid[x][a] != '.') break;
                        if(a != -1){
                            n++;
                            continue;
                        }
                        for(a = y+1; a < C; a++)
                            if(grid[x][a] != '.') break;
                        if(a != C){
                            n++;
                            continue;
                        }
                    }else continue;
                }
                if(grid[x][y] == 'v'){
                    for(a = x+1; a < R; a++){
                        if(grid[a][y] != '.') break;
                    }
                    if(a == R){
                        //fout << x << ' ' << y << '\n';
                        for(a = x-1; a >= 0; a--)
                            if(grid[a][y] != '.') break;
                        if(a != -1){
                            n++;
                            continue;
                        }
                        for(a = y-1; a >= 0; a--)
                            if(grid[x][a] != '.') break;
                        if(a != -1){
                            n++;
                            continue;
                        }
                        for(a = y+1; a < C; a++)
                            if(grid[x][a] != '.') break;
                        if(a != C){
                            n++;
                            continue;
                        }
                    }else continue;
                }
                if(grid[x][y] == '<'){
                    for(a = y-1; a >= 0; a--){
                        if(grid[x][a] != '.') break;
                    }
                    if(a == -1){
                        //fout << x << ' ' << y << '\n';
                        for(a = x-1; a >= 0; a--)
                            if(grid[a][y] != '.') break;
                        if(a != -1){
                            n++;
                            continue;
                        }
                        for(a = x+1; a < R; a++)
                            if(grid[a][y] != '.') break;
                        if(a != R){
                            n++;
                            continue;
                        }
                        for(a = y+1; a < C; a++)
                            if(grid[x][a] != '.') break;
                        if(a != C){
                            n++;
                            continue;
                        }
                    }else continue;
                }
                if(grid[x][y] == '>'){
                    for(a = y+1; a < C; a++)
                        if(grid[x][a] != '.') break;
                    if(a == C){
                        //fout << x << ' ' << y << '\n';
                        for(a = x-1; a >= 0; a--)
                            if(grid[a][y] != '.') break;
                        if(a != -1){
                            n++;
                            continue;
                        }
                        for(a = x+1; a < R; a++)
                            if(grid[a][y] != '.') break;
                        if(a != R){
                            n++;
                            continue;
                        }
                        for(a = y-1; a >= 0; a--)
                            if(grid[x][a] != '.') break;
                        if(a != -1){
                            n++;
                            continue;
                        }
                    }else continue;
                }
                if(grid[x][y] != '.'){
                    fout << "Case #" << i << ": IMPOSSIBLE\n";
                    x = R+1;
                    break;
                }
            }
        }
        if(x == R)
            fout << "Case #" << i  << ": " << n << '\n';
	}
	return 0;
}
