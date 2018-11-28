#include <iostream>


int check(char board[4][5]);
int main(){
int loop;
char dump;
char board[4][5];
do{
scanf("%d",&loop);
}while(loop<1 || loop > 10);

for(int i=0;i<loop;i++){
	for(int a=0;a<4;a++){
	scanf("%s",board[a]);
		fflush(stdin);
	}

	getchar();
	switch(check(board)){
	case 0 : printf("Case #%d: Draw",i+1);break;
	case 1 : printf("Case #%d: O won",i+1);break;
	case 2 : printf("Case #%d: X won",i+1);break;
	case 3 : printf("Case #%d: Game has not completed",i+1);break;
	default : printf("error !");
	}

	getchar();
}
return 0 ;
}

int check(char board[4][5]){
char main,player;
int flag=0,help=0;
// horizontal check
for(int i=0;i<4;i++){
	help=0;
	main=board[i][0];
	flag=0;
	player=board[i][0];
	//if(main=='.'){break;}
	if(player=='T'){player=board[i][1];flag++;main=board[i][1];help=1;}
	
	for(int j=1+help;j<4;j++){
		if(main==board[i][j]||board[i][j]=='T'){
			flag++;
		}
		if(flag==3 && player=='O'){
		return 1;}
		else if(flag==3 && player == 'X'){
			return 2;}}
}
// vertical check
for(int i=0;i<4;i++){
	help=0;
	main=board[0][i];
	flag=0;
	player=board[0][i];
	//if(main=='.'){break;}
	if(player=='T'){player=board[1][i];flag++;main=board[1][i];help=1;}
	for(int j=1+help;j<4;j++){
		if(main==board[j][i]||board[j][i]=='T'){
			flag++;
		}
		if(flag==3 && player=='O'){
		return 1;}
		else if(flag==3 && player == 'X'){
			return 2;}}
}
// diagonal check
help=0;
main=board[0][0];
flag=0;
player=board[0][0];
//if(main=='.'){goto skipd; }

	if(player=='T'){player=board[1][1];flag++;main=board[1][1];help=1;}
	for(int i=1+help;i<4;i++){if(main==board[i][i]||board[i][i]=='T'){
	flag++;}
		if(flag==3 && player=='O'){
		return 1;}
		else if(flag==3 && player == 'X'){
			return 2;}
	}
// right diagon check
		help=0;
main=board[0][3];
flag=0;
player=board[0][3];
//if(main=='.'){goto skip2;}
	if(player=='T'){help=1;player=board[2][2];flag++;main=board[2][2];}
	for(int i=2-help;i>=0;i--)
	{if(main==board[3-i][i]||board[3-i][i]=='T'){
		flag++;}
		if(flag==3 && player=='O'){
		return 1;}
		else if(flag==3 && player == 'X'){
			return 2;}
	}

	// empty check
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(board[i][j]=='.'){
			return 3;}}
	}
		return 0;
}