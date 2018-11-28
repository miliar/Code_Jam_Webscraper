#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <set>
#include <cmath>
#include <sstream>
#include <utility>
#include <cctype>
#include <numeric>
#include <queue>
#include <deque>
#include <list>
#include <stack>
#include <bitset>
#include <limits>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <functional>
using namespace std;
#define REP(i,n)    for(int i=1;i<=(n);++i)
#define FOR(n)    for(int i=1;i<(n);++i)
#define FORE(i,e,n) for(int i=(e);i<(n);++i)

#define out(v) cout<<(v)<<endl
#define _(A,v) memset(A,v,sizeof(A))
#define all(A)  (A).begin(), (A).end()
#define rall(A) (A).rbegin(),(A).rend()
#define pb push_back
#define             incontainer(c,x)            ( (c).find(x) != (c).end() )
# define nodo pair <int,int>

#define MAX 10000
#define LMT 100
/*
unsigned flag[MAX>>6];
//vector<int>primos;
string mov="";
#define ifc(x) (flag[x>>6]&(1<<((x>>1)&31)))
#define isc(x) (flag[x>>6]|=(1<<((x>>1)&31)))

void sieve1()
{
	int i, j, k;
	for(i=3; i<LMT; i+=2)
		if(!ifc(i))
			for(j=i*i,k=i<<1; j<MAX; j+=k)
				isc(j);

	for(i=3; i<MAX; i+=2){
		if(!ifc(i)){
			cout<<i<<endl;
		}
	}
}*/

bool found=false;
char boardX [4][4];
char boardO [4][4];

int main() {

   /* freopen("d.in",  "r", stdin);
    freopen("d.out", "w", stdout);*/
    int T;
    cin>>T;
    for( int cases =1; cases<=T;cases++){
        cout<<"Case #"<<cases<<": ";
        int spc=0;
        string lin;
        for(int i=0; i<4; i++){
            cin>>lin;
            for(int j=0; j<4; j++) {
               boardO[i][j]= boardX[i][j]=lin[j];
                if(boardX[i][j]=='.') {
                    spc++;
                }
                if(boardX[i][j]=='T') {
                    boardX[i][j]='X';
                    boardO[i][j]='O';
                }
            }
    }

    if(!found) {
        for(int i=0; i<4; i++) {
            if( boardX[i][0]=='X' && boardX[i][1]=='X' && boardX[i][2]=='X' && boardX[i][3]=='X' ) {
                cout<<"X won";
                found=true;
                break;
            }
        }
    }

    if(!found) {
        for(int i=0; i<4; i++) {
            if( boardX[0][i]=='X'  &&  boardX[1][i]=='X' && boardX[2][i]=='X' && boardX[3][i]=='X' ) {
                cout<<"X won";
                found=true;
                break;
            }
        }
    }

    if(!found) {
        if( boardX[0][0]=='X' && boardX[1][1]=='X' && boardX[2][2]=='X' &&  boardX[3][3]=='X') {
            cout<<"X won";
            found=true;
        }
    }

    if(!found) {
        if( boardX[0][3]=='X' &&  boardX[1][2]=='X' && boardX[2][1]=='X' &&  boardX[3][0]=='X') {
            cout<<"X won";
            found=true;
        }
    }
     if(!found) {
        for(int i=0; i<4; i++) {
            if( boardO[i][0]=='O' && boardO[i][1]=='O' && boardO[i][2]=='O' && boardO[i][3]=='O' ) {
                cout<<"O won";
                found=true;
                break;
            }
        }
    }

    if(!found) {
        for(int i=0; i<4; i++) {
            if( boardO[0][i]=='O'  &&  boardO[1][i]=='O' && boardO[2][i]=='O' && boardO[3][i]=='O' ) {
                cout<<"O won";
                found=true;
                break;
            }
        }
    }

    if(!found) {
        if( boardO[0][0]=='O' && boardO[1][1]=='O' && boardO[2][2]=='O' &&  boardO[3][3]=='O') {
            cout<<"O won";
            found=true;
        }
    }

    if(!found) {
        if( boardO[0][3]=='O' &&  boardO[1][2]=='O' && boardO[2][1]=='O' &&  boardO[3][0]=='O') {
            cout<<"O won";
            found=true;
        }
    }

    if(!found) {
        if(spc>0) cout<<"Game has not completed";
        else cout<<"Draw";
    }
 if(cases!=T) cout<<endl;
    found=false;
    spc=0;
}

return 0;
}
