#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<vector>
#include<map>
#include<queue>
#include<set>
using namespace std;
typedef long long LL;
#define For(i,a,n) for((i)=(a);(i)<=(n);(i)+=1)
#define refresh(a) memset((a),0,sizeof(a))
#define IN_S(x) scanf("%s",(x))
#define P_S(x) printf("%s\n",x)
#define IN_D(x) scanf("%d",&(x))
#define P_D(x) printf("%d\n",x)
#define IN_F(x) scanf("%lf",&(x))
#define P_F(x) printf("%lf\n",x)
#define IN_L(x) scanf("%lld",&(x))
#define P_L(x) printf("%lld\n",x)
#define P_NL printf("\n")
#define read() freopen("A-large.in","r",stdin)
#define write() freopen("A_large_out.out","w",stdout)
#define INF 1000000
#define mod 1000000007
#define maxn 300
char board[10][10];
int cnt_row[maxn],cnt_col[maxn],cnt_d1[maxn],cnt_d2[maxn];

int main()
{
    read();write();
	int cases,n,i,j,winner,case_no;
	bool game_complete;
	IN_D(cases);
	For(case_no,1,cases)
	{
	    game_complete=true;winner=0;
	    For(i,0,3)
            IN_S(board[i]);
        refresh(cnt_d1);refresh(cnt_d2);
        For(i,0,3)
        {
            refresh(cnt_row);refresh(cnt_col);
            For(j,0,3)
            {
                if(board[i][j]=='.')
                    game_complete=false;
                cnt_row[(int)board[i][j]]+=1;
                cnt_col[(int)board[j][i]]+=1;
                cnt_d1[(int)board[i][i]]+=(i==j)?1:0;
                cnt_d2[(int)board[i][j]]+=(i+j==3)?1:0;
            }
            if(cnt_row[(int)'X']+cnt_row[(int)'T']==4 ||
               cnt_col[(int)'X']+cnt_col[(int)'T']==4 ||
                cnt_d1[(int)'X']+cnt_d1[(int)'T']==4 ||
                cnt_d2[(int)'X']+cnt_d2[(int)'T']==4)
                {winner=1;break;}
            if(cnt_row[(int)'O']+cnt_row[(int)'T']==4 ||
               cnt_col[(int)'O']+cnt_col[(int)'T']==4 ||
                cnt_d1[(int)'O']+cnt_d1[(int)'T']==4 ||
                cnt_d2[(int)'O']+cnt_d2[(int)'T']==4)
                {winner=2;break;}
        }
        if(winner==1)
            printf("Case #%d: X won\n",case_no);
        else if(winner==2)
            printf("Case #%d: O won\n",case_no);
        else if(game_complete)
            printf("Case #%d: Draw\n",case_no);
        else
            printf("Case #%d: Game has not completed\n",case_no);
    }
	return 0;
}
