#include <stdio.h>
#include <stdlib.h>
#define rep(i,n) for(i=0;i<n;++i)
#define REP(i,s,n) for(i=s;i <n;++i)

int main(int argc, char** argv)
{
	int T,k,i,j, row, col;
	char board[4][5], lastchar;
	bool done = false, isempty=false;
	FILE* in = fopen(argv[1], "r");
	FILE*out = fopen("abc.txt","w");
	fscanf(in,"%d\n",&T);
	if(1 > T || T > 10)
		return 0;

	rep(k,T){
			done = false;
			isempty=false;
			rep(row, 4)
			{
				fscanf(in,"%s",&board[row]);
				board[row][4]='\0';
				if(!isempty)
				{	
					rep(i,4)
						if(board[row][i]=='.')
						{
							isempty=true;
							break;
						}
				}
			}

			//left diagonal
			lastchar = board[0][0];
			for(j=1;j<4 && board[j-1][j-1] != '.' && (board[j][j] == 'T' || board[j][j] == board[j-1][j-1] || board[j-1][j-1] == 'T');++j){
				if(lastchar == 'T')lastchar=board[j][j];
				else if(lastchar != board[j][j])
					break;
			}
			if(j ==4){
				for(j=0;j<4,board[j][j] == 'T';++j);
				fprintf(out,"Case #%d: %c won\n",k+1,board[j][j]);
				continue;
			}
			//right diagonal
			lastchar= board[0][3];
			for(j=1;j<4 && board[j-1][4-j] != '.' && (board[j][3-j] == 'T' || board[j][3-j] == board[j-1][4-j] || board[j-1][4-j] == 'T');++j){
				if(lastchar == 'T')lastchar=board[j][j];
				else if(lastchar != board[j][3-j])
					break;
			}
			if(j ==4){
				for(j=0;j<4,board[j][3-j] == 'T';++j);
				fprintf(out,"Case #%d: %c won\n",k+1,board[j][3-j]);
				continue;
			}
			//row
			rep(i,4){
				lastchar = board[i][0];
				for(j=1;j<4 && board[i][j-1] != '.' && (board[i][j] == 'T' || board[i][j] == board[i][j-1] || board[i][j-1] == 'T');++j){
					if(lastchar == 'T')lastchar=board[i][j];
					else if(lastchar != board[i][j])
						break;
				}
				if(j ==4){
					for(j=0;j<4,board[i][j] == 'T';++j);
					fprintf(out,"Case #%d: %c won\n",k+1,board[i][j]);
					done=true;
				}
				if(done)break;
			}
			if(done)
				continue;
			//col
			rep(i,4){
				lastchar = board[0][i];
				for(j=1;j<4 && board[j-i][i] != '.' && (board[j][i] == 'T' || board[j][i] == board[j-1][i] || board[j-1][i] == 'T');++j){
					if(lastchar == 'T')lastchar=board[j][i];
					else if(lastchar != board[j][i])
						break;
				}
				if(j ==4){
					for(j=0;j<4,board[j][i] == 'T';++j);
					fprintf(out,"Case #%d: %c won\n",k+1,board[j][i]);
					done=true;
				}
				if(done)break;
			}

			if(done)
				continue;
			if(isempty)
				fprintf(out,"Case #%d: Game has not completed\n",k+1);
			else
				fprintf(out,"Case #%d: Draw\n",k+1);
	}
	return 0;
}
