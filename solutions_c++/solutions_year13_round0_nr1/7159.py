#include <cstdio>
#include <cstdlib>

char tablero[6][6];

char comodin = 'T';
char letter[2] = {'X','O'};

int estaCompleto(){
	int resp = 0;
	for (int i = 1; i <= 4; ++i){
		for (int j = 1; j <= 4; ++j){
			if (tablero[i][j]=='.') return false;
		}
	}
	return true;
}

int letraValida(int player, char letra){
	return (letra == letter[player] || letra == comodin);
}

int vertCheck(int playerNum){
	int resp = 0;
	for (int j = 1; j <= 4; ++j){
		int subtot = 0;
			for (int i = 1; i <= 4; ++i){	
			subtot += letraValida(playerNum,tablero[i][j]);
		}
		if (subtot==4) return true;
	}
	return false;
}

int horizCheck(int playerNum){
	int resp = 0;
	for (int i = 1; i <= 4; ++i){
		int subtot = 0;
		for (int j = 1; j <= 4; ++j){
			subtot += letraValida(playerNum,tablero[i][j]);
		}
		if (subtot==4) return true;
	}
	return false;
}

int diagCheck(int playerNum) {
	int subtot = 0;
	for (int i = 1; i<=4; ++i) {
		subtot += letraValida(playerNum,tablero[i][i]);
	}
	if (subtot == 4) return true;
	subtot = 0;
	for (int i = 1; i<=4; ++i) {
		subtot += letraValida(playerNum,tablero[i][5-i]);
	}
	if (subtot == 4) return true;
	return false;
}

bool gano(int pNum){
	return vertCheck(pNum)||horizCheck(pNum)||diagCheck(pNum);
}

int main() {
	unsigned N;
	char buff[10];
	for (int i = 0; i < 6; ++i)
		for (int j = 0; j < 6; ++j)
			tablero[i][j] = '_';
	char ign;
	scanf("%u\n",&N);


	for (size_t c = 1; c <= N; ++c) {
		
		for(size_t i=1;i<5;++i){
			//scanf("%c%c%c%c%c",&tablero[i][1],&tablero[i][2],&tablero[i][3],&tablero[i][4]);
			scanf("%s",buff);
			for(size_t j=1;j<5;++j) tablero[i][j] = buff[j-1];
		}
		bool ganoX = gano(0);
		bool ganoO = gano(1);
		if (!ganoX && !ganoO && !estaCompleto()){
			printf("Case #%d: Game has not completed\n",c);
		} else {
			
			if (ganoX == ganoO){
				printf("Case #%d: Draw\n",c);
			}else {
				printf("Case #%d: %c won\n",c,letter[ganoO]);
			}

		}
		
	}
}