#include<vector>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<set>
#include<string.h>
#include<map>
#include<algorithm>
#include<cassert>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<queue>
#include<stack>
#include<ctype.h>
#define all(c) (c).begin(), (c).end()
#define iter(c) __typeof((c).begin())
#define present(c, e) ((c).find((e)) != (c).end())
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb push_back
#define mp make_pair
#define fia(i,a,b) for(int i=(int)(a);i<(int)(b);i++)
#define fib(i,a,b) for(int i=(int)(b);i>(int)(a);i--)
#define vs vector <string>
#define vi vector <int>
#define vvi vector < vi >
#define srt(v) sort((v).begin(),(v).end())
#define srtc(v) sort(v.begin(),v.end(),cmp)
#define maxi(v) max_element(all(v))
#define mini(v) min_element(all(v))
#define ipow(a,b) (int)pow((double)a,(double)b)
#define fill(a,b) memset(a,b,sizeof(a))
using namespace std;

int read_num()
{
    int num = 0;
    char ch;
    ch = getchar();
    while(!isdigit(ch))
        ch = getchar();
    do{
        num = num*10+(ch-'0');
        ch = getchar();
    }while(isdigit(ch));
    return  num;
}
char board[4][4];
bool diagonalFir(char c)
{
    int cnt = 0;
    for(int i = 0; i < 4; i++)
    {
        if(board[i][i] == c || board[i][i] == 'T')
            cnt++;
    }
    if(cnt == 4)
        return true;
    return false;
}
bool diagonalSec(char c)
{
    int cnt = 0;
    for(int i = 0; i < 4; i++)
    {
        if(board[i][3-i] == c || board[i][3-i] == 'T')
            cnt++;
    }
    if(cnt == 4)
        return true;
    return false;
}
bool rowCheck(char c)
{
    
    int tot = 0;
    for(int i = 0; i < 4; i++)
    {
        int cnt = 0;
        for(int j =0; j < 4; j++)
        if(board[i][j] == c || board[i][j] == 'T')
            cnt++;
        if(cnt == 4)
            tot++;
    }
    if(tot >0)
        return true;
    return false;
}
bool colCheck(char c)
{
    
    int tot = 0;
    for(int i = 0; i < 4; i++)
    {
        int cnt = 0;
        for(int j =0; j < 4; j++)
            if(board[j][i] == c || board[j][i] == 'T')
                cnt++;
        if(cnt == 4)
            tot++;
    }
    if(tot >0)
        return true;
    return false;
}

bool Xcheck()
{
    if(colCheck('X') || rowCheck('X') || diagonalFir('X') || diagonalSec('X'))
        return true;
    return false;
}
bool Ocheck()
{
    if(colCheck('O') || rowCheck('O') || diagonalFir('O') || diagonalSec('O'))
        return true;
    return false;
}
bool filled()
{
    int cnt = 0;
    for(int i = 0; i < 4; i++)
    {
        for(int j =0; j < 4; j++)
            if(board[i][j] == 'O' || board[i][j] == 'X' || board[i][j] == 'T')
                cnt++;
        
    }
    if(cnt == 16)
        return true;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int n = read_num();
    fia(tt, 1, n+1)
    {
        for(int i = 0; i < 4; i++)
        {
            cin>>board[i];
        }
        if(Xcheck())
        {
            cout<<"Case #"<<tt<<": X won"<<endl;
        }
        else if(Ocheck())
        {
            cout<<"Case #"<<tt<<": O won"<<endl;
        }
        else if(filled())
        {
            cout<<"Case #"<<tt<<": Draw"<<endl;
        }
        else
        {
            cout<<"Case #"<<tt<<": Game has not completed"<<endl;
        }
    }
}