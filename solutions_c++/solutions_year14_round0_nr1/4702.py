#include<iostream>
#include<vector>
#include<string.h>
#include<algorithm>
#include<fstream>
using namespace std;
int main(){
	ifstream in("A-small-attempt0.in");
	ofstream out("A.out");
	int t, grid[4][4], q[2], op;
	int visited[20];
	in >> t;
	for(int x = 1; x <= t; ++ x){
		memset(visited, 0, sizeof(visited));
		op = -1;
		for(int i = 0; i < 2; ++ i){
			in >> q[i];
			for(int j = 0; j < 16; ++ j)
				in >> grid[j/16][j%16];
			for(int j = 0; j < 4; ++ j)
				visited[grid[q[i] - 1][j]] ++;
		}
		for(int i = 1; i < 17; ++ i)
			if (visited[i] == 2) op = (op == -1)? i : 100;
		out << "Case #" << x << ": ";
		if (op == -1) out << "Volunteer cheated!\n";
		else if(op == 100) out << "Bad magician!\n";
		else out << op << endl;
	}
	return 0;
}