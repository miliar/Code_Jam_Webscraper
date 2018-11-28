#include <cstdio>
#include <string.h>

using namespace std;

bool map[5][5];
bool visited[5][5];
int neigh[8][2] = { {-1,-1}, {-1,0}, {-1,1}, {0,-1}, {0,1}, {1,-1}, {1,0}, {1,1} };

int cx, cy;


int R, C, M;

int bfs(int x, int y) {
	if(map[x][y] || visited[x][y])
		return 0;
	visited[x][y]=true;
	int num=0;
	bool hasmine = false;	
	for(int i=0; i<8; i++) {
		int nx = x+neigh[i][0];
		int ny = y+neigh[i][1];
		if(nx >=0 && ny >=0 && nx <R && ny<C) {
			if(map[nx][ny]) hasmine = true;
		}
	}
	if(!hasmine) {
		for(int i=0; i<8; i++) {
			int nx = x+neigh[i][0];
			int ny = y+neigh[i][1];
			if(nx >=0 && ny >=0 && nx <R && ny<C) {
				num += bfs(nx, ny);
			}
		}
	}
	//printf("bfs bei %d %d, kriegt: %d\n", x, y, num);
	

	return 1+num;
}

char out[40];
void printMap2() {
	int index=0;
	for(int i=0; i<R; i++) {
		for(int j=0; j<C; j++) {
			if(map[i][j])
				out[index++]='*';
			else if(cx==i && cy==j) {
				out[index++]='c';
			} else {
				out[index++]='.';
			}
		}
		out[index++]='\\';
		out[index++]='n';
	}
	out[index]='\0';
}

void printMap() {
	for(int i=0; i<R; i++) {
		for(int j=0; j<C; j++) {
			if(map[i][j])
				printf("*");
			else if(cx==i && cy==j) {
				printf("c");
			} else {
				printf(".");
			}
		}
		printf("\n");
	}
}


int glob=0;
bool checkMap() {

	// debug
	//cx=0; cy=0;
	//printf("%d\n", glob++);
	//printMap();

	for(int i=0; i<R*C; i++) {
		if(!map[i/C][i%C]) { // wenn keine miene da liegt
			for(int j=0; j<R*C; j++) {
				visited[j/C][j%C] = false;
			}
			int bfsr = bfs(i/C, i%C);
			//printf("%d %d: %d == %d\n", i/C, i%C, bfsr, R*C-M);
			if(bfsr==R*C-M) // und alle anderen felder erreichbar sind
			{
				cx = i/C; cy=i%C;
				return true;
			}
		}
	}
	return false;
}


bool backtrack(int i, int m) {

	if(i>=R*C) {
		if(m>0)
			return false;
		return checkMap();
	}
	
	if(m>0) {
		map[i/C][i%C]=true; // setze mine
		if (backtrack(i+1, m-1)) return true;
	} 
	{
		map[i/C][i%C]=false; // setze keine miene
		if(backtrack(i+1, m)) return true;
	}
	return false;
}

char alle[5][5][25][40];

void initthemap() {
strcpy(alle[0][0][0],"c\n");
strcpy(alle[0][1][0],"c.\n");
strcpy(alle[0][1][1],"*c\n");
strcpy(alle[0][2][0],"c..\n");
strcpy(alle[0][2][1],"*.c\n");
strcpy(alle[0][2][2],"**c\n");
strcpy(alle[0][3][0],"c...\n");
strcpy(alle[0][3][1],"*.c.\n");
strcpy(alle[0][3][2],"**.c\n");
strcpy(alle[0][3][3],"***c\n");
strcpy(alle[0][4][0],"c....\n");
strcpy(alle[0][4][1],"*.c..\n");
strcpy(alle[0][4][2],"**.c.\n");
strcpy(alle[0][4][3],"***.c\n");
strcpy(alle[0][4][4],"****c\n");
strcpy(alle[1][0][0],"c\n.\n");
strcpy(alle[1][0][1],"*\nc\n");
strcpy(alle[1][1][0],"c.\n..\n");
strcpy(alle[1][1][1],"Impossible\n");
strcpy(alle[1][1][2],"Impossible\n");
strcpy(alle[1][1][3],"**\n*c\n");
strcpy(alle[1][2][0],"c..\n...\n");
strcpy(alle[1][2][1],"Impossible\n");
strcpy(alle[1][2][2],"*.c\n*..\n");
strcpy(alle[1][2][3],"Impossible\n");
strcpy(alle[1][2][4],"Impossible\n");
strcpy(alle[1][2][5],"***\n**c\n");
strcpy(alle[1][3][0],"c...\n....\n");
strcpy(alle[1][3][1],"Impossible\n");
strcpy(alle[1][3][2],"*.c.\n*...\n");
strcpy(alle[1][3][3],"Impossible\n");
strcpy(alle[1][3][4],"**.c\n**..\n");
strcpy(alle[1][3][5],"Impossible\n");
strcpy(alle[1][3][6],"Impossible\n");
strcpy(alle[1][3][7],"****\n***c\n");
strcpy(alle[1][4][0],"c....\n.....\n");
strcpy(alle[1][4][1],"Impossible\n");
strcpy(alle[1][4][2],"*.c..\n*....\n");
strcpy(alle[1][4][3],"Impossible\n");
strcpy(alle[1][4][4],"**.c.\n**...\n");
strcpy(alle[1][4][5],"Impossible\n");
strcpy(alle[1][4][6],"***.c\n***..\n");
strcpy(alle[1][4][7],"Impossible\n");
strcpy(alle[1][4][8],"Impossible\n");
strcpy(alle[1][4][9],"*****\n****c\n");
strcpy(alle[2][0][0],"c\n.\n.\n");
strcpy(alle[2][0][1],"*\n.\nc\n");
strcpy(alle[2][0][2],"*\n*\nc\n");
strcpy(alle[2][1][0],"c.\n..\n..\n");
strcpy(alle[2][1][1],"Impossible\n");
strcpy(alle[2][1][2],"**\n..\nc.\n");
strcpy(alle[2][1][3],"Impossible\n");
strcpy(alle[2][1][4],"Impossible\n");
strcpy(alle[2][1][5],"**\n**\n*c\n");
strcpy(alle[2][2][0],"c..\n...\n...\n");
strcpy(alle[2][2][1],"*.c\n...\n...\n");
strcpy(alle[2][2][2],"Impossible\n");
strcpy(alle[2][2][3],"***\n...\nc..\n");
strcpy(alle[2][2][4],"Impossible\n");
strcpy(alle[2][2][5],"***\n*..\n*.c\n");
strcpy(alle[2][2][6],"Impossible\n");
strcpy(alle[2][2][7],"Impossible\n");
strcpy(alle[2][2][8],"***\n***\n**c\n");
strcpy(alle[2][3][0],"c...\n....\n....\n");
strcpy(alle[2][3][1],"*.c.\n....\n....\n");
strcpy(alle[2][3][2],"**.c\n....\n....\n");
strcpy(alle[2][3][3],"*.c.\n*...\n*...\n");
strcpy(alle[2][3][4],"****\n....\nc...\n");
strcpy(alle[2][3][5],"Impossible\n");
strcpy(alle[2][3][6],"****\n*...\n*.c.\n");
strcpy(alle[2][3][7],"Impossible\n");
strcpy(alle[2][3][8],"****\n**..\n**.c\n");
strcpy(alle[2][3][9],"Impossible\n");
strcpy(alle[2][3][10],"Impossible\n");
strcpy(alle[2][3][11],"****\n****\n***c\n");
strcpy(alle[2][4][0],"c....\n.....\n.....\n");
strcpy(alle[2][4][1],"*.c..\n.....\n.....\n");
strcpy(alle[2][4][2],"**.c.\n.....\n.....\n");
strcpy(alle[2][4][3],"***.c\n.....\n.....\n");
strcpy(alle[2][4][4],"**.c.\n*....\n*....\n");
strcpy(alle[2][4][5],"*****\n.....\nc....\n");
strcpy(alle[2][4][6],"**.c.\n**...\n**...\n");
strcpy(alle[2][4][7],"*****\n*....\n*.c..\n");
strcpy(alle[2][4][8],"Impossible\n");
strcpy(alle[2][4][9],"*****\n**...\n**.c.\n");
strcpy(alle[2][4][10],"Impossible\n");
strcpy(alle[2][4][11],"*****\n***..\n***.c\n");
strcpy(alle[2][4][12],"Impossible\n");
strcpy(alle[2][4][13],"Impossible\n");
strcpy(alle[2][4][14],"*****\n*****\n****c\n");
strcpy(alle[3][0][0],"c\n.\n.\n.\n");
strcpy(alle[3][0][1],"*\n.\nc\n.\n");
strcpy(alle[3][0][2],"*\n*\n.\nc\n");
strcpy(alle[3][0][3],"*\n*\n*\nc\n");
strcpy(alle[3][1][0],"c.\n..\n..\n..\n");
strcpy(alle[3][1][1],"Impossible\n");
strcpy(alle[3][1][2],"**\n..\nc.\n..\n");
strcpy(alle[3][1][3],"Impossible\n");
strcpy(alle[3][1][4],"**\n**\n..\nc.\n");
strcpy(alle[3][1][5],"Impossible\n");
strcpy(alle[3][1][6],"Impossible\n");
strcpy(alle[3][1][7],"**\n**\n**\n*c\n");
strcpy(alle[3][2][0],"c..\n...\n...\n...\n");
strcpy(alle[3][2][1],"*.c\n...\n...\n...\n");
strcpy(alle[3][2][2],"*.c\n*..\n...\n...\n");
strcpy(alle[3][2][3],"***\n...\nc..\n...\n");
strcpy(alle[3][2][4],"***\n*..\n..c\n...\n");
strcpy(alle[3][2][5],"Impossible\n");
strcpy(alle[3][2][6],"***\n***\n...\nc..\n");
strcpy(alle[3][2][7],"Impossible\n");
strcpy(alle[3][2][8],"***\n***\n*..\n*.c\n");
strcpy(alle[3][2][9],"Impossible\n");
strcpy(alle[3][2][10],"Impossible\n");
strcpy(alle[3][2][11],"***\n***\n***\n**c\n");
strcpy(alle[3][3][0],"c...\n....\n....\n....\n");
strcpy(alle[3][3][1],"*.c.\n....\n....\n....\n");
strcpy(alle[3][3][2],"**.c\n....\n....\n....\n");
strcpy(alle[3][3][3],"**.c\n*...\n....\n....\n");
strcpy(alle[3][3][4],"****\n....\nc...\n....\n");
strcpy(alle[3][3][5],"****\n*...\n..c.\n....\n");
strcpy(alle[3][3][6],"****\n**..\n...c\n....\n");
strcpy(alle[3][3][7],"****\n*...\n*.c.\n*...\n");
strcpy(alle[3][3][8],"****\n****\n....\nc...\n");
strcpy(alle[3][3][9],"Impossible\n");
strcpy(alle[3][3][10],"****\n****\n*...\n*.c.\n");
strcpy(alle[3][3][11],"Impossible\n");
strcpy(alle[3][3][12],"****\n****\n**..\n**.c\n");
strcpy(alle[3][3][13],"Impossible\n");
strcpy(alle[3][3][14],"Impossible\n");
strcpy(alle[3][3][15],"****\n****\n****\n***c\n");
strcpy(alle[3][4][0],"c....\n.....\n.....\n.....\n");
strcpy(alle[3][4][1],"*.c..\n.....\n.....\n.....\n");
strcpy(alle[3][4][2],"**.c.\n.....\n.....\n.....\n");
strcpy(alle[3][4][3],"***.c\n.....\n.....\n.....\n");
strcpy(alle[3][4][4],"***.c\n*....\n.....\n.....\n");
strcpy(alle[3][4][5],"*****\n.....\nc....\n.....\n");
strcpy(alle[3][4][6],"*****\n*....\n..c..\n.....\n");
strcpy(alle[3][4][7],"*****\n**...\n...c.\n.....\n");
strcpy(alle[3][4][8],"*****\n***..\n....c\n.....\n");
strcpy(alle[3][4][9],"*****\n**...\n*..c.\n*....\n");
strcpy(alle[3][4][10],"*****\n*****\n.....\nc....\n");
strcpy(alle[3][4][11],"*****\n**...\n**.c.\n**...\n");
strcpy(alle[3][4][12],"*****\n*****\n*....\n*.c..\n");
strcpy(alle[3][4][13],"Impossible\n");
strcpy(alle[3][4][14],"*****\n*****\n**...\n**.c.\n");
strcpy(alle[3][4][15],"Impossible\n");
strcpy(alle[3][4][16],"*****\n*****\n***..\n***.c\n");
strcpy(alle[3][4][17],"Impossible\n");
strcpy(alle[3][4][18],"Impossible\n");
strcpy(alle[3][4][19],"*****\n*****\n*****\n****c\n");
strcpy(alle[4][0][0],"c\n.\n.\n.\n.\n");
strcpy(alle[4][0][1],"*\n.\nc\n.\n.\n");
strcpy(alle[4][0][2],"*\n*\n.\nc\n.\n");
strcpy(alle[4][0][3],"*\n*\n*\n.\nc\n");
strcpy(alle[4][0][4],"*\n*\n*\n*\nc\n");
strcpy(alle[4][1][0],"c.\n..\n..\n..\n..\n");
strcpy(alle[4][1][1],"Impossible\n");
strcpy(alle[4][1][2],"**\n..\nc.\n..\n..\n");
strcpy(alle[4][1][3],"Impossible\n");
strcpy(alle[4][1][4],"**\n**\n..\nc.\n..\n");
strcpy(alle[4][1][5],"Impossible\n");
strcpy(alle[4][1][6],"**\n**\n**\n..\nc.\n");
strcpy(alle[4][1][7],"Impossible\n");
strcpy(alle[4][1][8],"Impossible\n");
strcpy(alle[4][1][9],"**\n**\n**\n**\n*c\n");
strcpy(alle[4][2][0],"c..\n...\n...\n...\n...\n");
strcpy(alle[4][2][1],"*.c\n...\n...\n...\n...\n");
strcpy(alle[4][2][2],"*.c\n*..\n...\n...\n...\n");
strcpy(alle[4][2][3],"***\n...\nc..\n...\n...\n");
strcpy(alle[4][2][4],"***\n*..\n..c\n...\n...\n");
strcpy(alle[4][2][5],"***\n*..\n*.c\n...\n...\n");
strcpy(alle[4][2][6],"***\n***\n...\nc..\n...\n");
strcpy(alle[4][2][7],"***\n***\n*..\n..c\n...\n");
strcpy(alle[4][2][8],"Impossible\n");
strcpy(alle[4][2][9],"***\n***\n***\n...\nc..\n");
strcpy(alle[4][2][10],"Impossible\n");
strcpy(alle[4][2][11],"***\n***\n***\n*..\n*.c\n");
strcpy(alle[4][2][12],"Impossible\n");
strcpy(alle[4][2][13],"Impossible\n");
strcpy(alle[4][2][14],"***\n***\n***\n***\n**c\n");
strcpy(alle[4][3][0],"c...\n....\n....\n....\n....\n");
strcpy(alle[4][3][1],"*.c.\n....\n....\n....\n....\n");
strcpy(alle[4][3][2],"**.c\n....\n....\n....\n....\n");
strcpy(alle[4][3][3],"**.c\n*...\n....\n....\n....\n");
strcpy(alle[4][3][4],"****\n....\nc...\n....\n....\n");
strcpy(alle[4][3][5],"****\n*...\n..c.\n....\n....\n");
strcpy(alle[4][3][6],"****\n**..\n...c\n....\n....\n");
strcpy(alle[4][3][7],"****\n**..\n*..c\n....\n....\n");
strcpy(alle[4][3][8],"****\n****\n....\nc...\n....\n");
strcpy(alle[4][3][9],"****\n****\n*...\n..c.\n....\n");
strcpy(alle[4][3][10],"****\n****\n**..\n...c\n....\n");
strcpy(alle[4][3][11],"****\n****\n*...\n*.c.\n*...\n");
strcpy(alle[4][3][12],"****\n****\n****\n....\nc...\n");
strcpy(alle[4][3][13],"Impossible\n");
strcpy(alle[4][3][14],"****\n****\n****\n*...\n*.c.\n");
strcpy(alle[4][3][15],"Impossible\n");
strcpy(alle[4][3][16],"****\n****\n****\n**..\n**.c\n");
strcpy(alle[4][3][17],"Impossible\n");
strcpy(alle[4][3][18],"Impossible\n");
strcpy(alle[4][3][19],"****\n****\n****\n****\n***c\n");
strcpy(alle[4][4][0],"c....\n.....\n.....\n.....\n.....\n");
strcpy(alle[4][4][1],"*.c..\n.....\n.....\n.....\n.....\n");
strcpy(alle[4][4][2],"**.c.\n.....\n.....\n.....\n.....\n");
strcpy(alle[4][4][3],"***.c\n.....\n.....\n.....\n.....\n");
strcpy(alle[4][4][4],"***.c\n*....\n.....\n.....\n.....\n");
strcpy(alle[4][4][5],"*****\n.....\nc....\n.....\n.....\n");
strcpy(alle[4][4][6],"*****\n*....\n..c..\n.....\n.....\n");
strcpy(alle[4][4][7],"*****\n**...\n...c.\n.....\n.....\n");
strcpy(alle[4][4][8],"*****\n***..\n....c\n.....\n.....\n");
strcpy(alle[4][4][9],"*****\n***..\n*...c\n.....\n.....\n");
strcpy(alle[4][4][10],"*****\n*****\n.....\nc....\n.....\n");
strcpy(alle[4][4][11],"*****\n*****\n*....\n..c..\n.....\n");
strcpy(alle[4][4][12],"*****\n*****\n**...\n...c.\n.....\n");
strcpy(alle[4][4][13],"*****\n*****\n***..\n....c\n.....\n");
strcpy(alle[4][4][14],"*****\n*****\n**...\n*..c.\n*....\n");
strcpy(alle[4][4][15],"*****\n*****\n*****\n.....\nc....\n");
strcpy(alle[4][4][16],"*****\n*****\n**...\n**.c.\n**...\n");
strcpy(alle[4][4][17],"*****\n*****\n*****\n*....\n*.c..\n");
strcpy(alle[4][4][18],"Impossible\n");
strcpy(alle[4][4][19],"*****\n*****\n*****\n**...\n**.c.\n");
strcpy(alle[4][4][20],"Impossible\n");
strcpy(alle[4][4][21],"*****\n*****\n*****\n***..\n***.c\n");
strcpy(alle[4][4][22],"Impossible\n");
strcpy(alle[4][4][23],"Impossible\n");
strcpy(alle[4][4][24],"*****\n*****\n*****\n*****\n****c\n");
}


int main2() {
	// do all:
	
	for(R=1; R<=5; R++) {
		for(C=1; C<=5; C++) {
			for(M=0;M<R*C;M++) {
				if(backtrack(0, M)) {
					printMap2();
					printf("strcpy(alle[%d][%d][%d],\"%s\");\n", R-1, C-1, M, out);
				} else {
					printf("strcpy(alle[%d][%d][%d],\"Impossible\\n\");\n", R-1, C-1, M);
				}				
			}
		}
	}
}

int main() {

	int T;
	scanf("%d ", &T);
	for(int t=0; t<T; t++) {
		printf("Case #%d:\n", t+1);
		
		scanf("%d %d %d ", &R, &C, &M);		
		
		initthemap();
			
		printf ("%s", alle[R-1][C-1][M]);
	
	}



	return 0;
}
