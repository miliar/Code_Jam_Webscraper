#include<stdio.h>


char B[10][10];
bool hasBlank;
int X, O, T;

bool isValid(char ch){
	return (ch=='.' || ch=='X' || ch=='O' || ch=='T');
}

void input(){
	char ch;
	int i, j;
	hasBlank = false;
	for(i=1; i<=4; i++){
		for(j=1; j<=4; j++){
			scanf("%c", &ch);
			if( isValid(ch) ){ B[i][j] = ch; }
			else{ j--; }
			if( ch=='.' )hasBlank = true;
		}
	}
}

void print(char ch){
	printf("%c won\n", ch);
}

int check(){
	if( X==4 || (X==3 && T==1) ){
		print('X');
		return 1;
	}else if( O==4 || (O==3 && T==1) ){
		print('O');
		return 1;
	}
	return 0;
}


void solve(){
	int i, j;
	for(i=1; i<=4; i++){
		X = O = T = 0;
		for(j=1; j<=4; j++){
			X += (B[i][j]=='X');
			O += (B[i][j]=='O');
			T += (B[i][j]=='T');
		}
		if( check() )return;
	}
	for(j=1; j<=4; j++){
		X = O = T = 0;
		for(i=1; i<=4; i++){
			X += (B[i][j]=='X');
			O += (B[i][j]=='O');
			T += (B[i][j]=='T');
		}
		if( check() )return;
	}
	X = O = T = 0;
	for(i=1; i<=4; i++){
		X += (B[i][i]=='X');
		O += (B[i][i]=='O');
		T += (B[i][i]=='T');
	}
	if( check() )return;
	X = O = T = 0;
	for(i=1; i<=4; i++){
		X += (B[i][5-i]=='X');
		O += (B[i][5-i]=='O');
		T += (B[i][5-i]=='T');
	}
	if( check() )return;
	if( hasBlank ){
		puts("Game has not completed");
	}else{
		puts("Draw");
	}
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, cs;
	scanf("%d", &T);
	for(cs=1; cs<=T; cs++){
		input();
		printf("Case #%d: ", cs);
		solve();
	}
	return 0;
}