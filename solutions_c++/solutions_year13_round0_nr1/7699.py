#include <stdio.h>

FILE *inn = fopen ( "INPUT.TXT", "r" );
FILE *out = fopen ( "OUTPUT.TXT", "w" );

bool r[2];
char m[4][4+1];
int D[8][2]={-1,-1,-1,0,-1,1,0,-1,0,1,1,-1,1,0,1,1};

void input (){
	int i;

	for (i=0; i<4; i++) fscanf ( inn, "%s", &m[i] );
}

void dfs ( int y, int x, int d, int Cnt, int ox ){
	if (y<0 || x<0 || y>=4 || x>=4) return;
	if ( !(m[y][x]==m[ y- D[d][0]*(Cnt-1) ][ x- D[d][1]*(Cnt-1) ] || m[y][x]=='T') ) return;

	if (Cnt==4){
		r[ox]=true;
		return;
	}

	dfs ( y+D[d][0], x+D[d][1], d, Cnt+1, ox );
}

void process (){
	int i, u, j;
	r[0]=r[1]=false;

	for (i=0; i<4; i++){
		for (u=0; u<4; u++){
			if (m[i][u]=='O' && r[0]==false) for (j=0; j<8; j++) dfs ( i, u, j, 1, 0 );
			if (m[i][u]=='X' && r[1]==false) for (j=0; j<8; j++) dfs ( i, u, j, 1, 1 );
		}
	}
}

void output ( int in ){
	int i, u;

	if (r[0]) fprintf ( out, "Case #%d: O won\n", in );
	else if (r[1]) fprintf ( out, "Case #%d: X won\n", in );

	else{
		for (i=0; i<4; i++){
			for (u=0; u<4; u++) if (m[i][u]=='.') break;
			if (u<4) break;
		}

		if (i==4) fprintf ( out, "Case #%d: Draw\n", in );
		else fprintf ( out, "Case #%d: Game has not completed\n", in );
	}
}

int main (){
	int T, i=1;

	fscanf ( inn, "%d", &T );

	while ( T-- ){
		input ();
		process ();
		output ( i++ );
	}

	return 0;
}
