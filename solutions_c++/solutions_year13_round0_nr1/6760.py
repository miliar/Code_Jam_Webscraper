#include <cstdio>
#include <algorithm>
#define FOR(a,b,c) for(int i=a; i<b; i+=c)

using namespace std;

int ans=0;
char board[5][5];

int main()
{
	int T=0,cas=1,undone=0,flag=0,j;
	char curChar,win=0;
	scanf("%d",&T);
	
	while(T--)
	{
        win=undone=0;
		FOR(0,4,1) scanf("\n%s",board[i]);
		scanf("\n");
		/*FOR(0,4,1){
            for(j=0;j<4;j++){
                scanf("%c",&board[i][j]);
            }
		}
		FOR(0,4,1){
            for(j=0;j<4;j++){
                printf("%c",board[i][j]);
            }
            printf("\n");
		}*/
		FOR(0,4,1)
		{
            for(j=0;j<4;j++)
            {
                if(board[i][j]=='.')
                {
                    undone++;
                    break;
                }
            }
		}
		//printf("=un=%d=",undone);
		FOR(0,4,1)
		{
            flag=0;
            if(board[i][0]!='T') curChar = board[i][0];
            else curChar = board[i][1];
            for(j=1;j<4;j++)
            {
                if((board[i][j]==curChar || board[i][j]=='T') && board[i][j]!='.');
                else { 
                    flag++;
                    break;
                }
            }
            if(flag==0)
            {
                //printf("%d",i);
                //win=curChar;
                break;
            }
            flag=0;
            if(board[0][i]!='T') curChar = board[0][i];
            else curChar = board[1][i];
            for(j=1;j<4;j++)
            {
                if((board[j][i]==curChar || board[j][i]=='T') && board[j][i]!='.');
                else {
                    flag++;
                    break;
                }
            }
            if(flag==0)
            {
                //win = curChar;
                break;
            }
		}
		if(flag!=0)
		{
            flag=0;
            if(board[0][0]!='T') curChar = board[0][0];
            else curChar = board[1][1];
            FOR(0,3,1)
            {
                if((curChar==board[i+1][i+1] || board[i+1][i+1]=='T')&&board[i+1][i+1]!='.');
                else {
                    flag++;
                    break;
                }
            }
            if(flag==0)
            {
                //win=curChar;
            }
            else {
                flag=0;
                if(board[0][3]!='T') curChar = board[0][3];
                else curChar= board[1][2];
                FOR(0,3,1)
                {
                    if((curChar==board[i+1][2-i] || board[i+1][2-i]=='T' ) && board[i+1][2-i]!='.');
                    else {
                        flag++;
                        break;
                    }
                }
                if(flag==0)
                {
                    //win=curChar;
                }
            }
		}
		printf("Case #%d: ",cas++);
		if(flag==0) printf("%c won\n",curChar);
		else if(undone==0) printf("Draw\n");
		else printf("Game has not completed\n");
	}
}
