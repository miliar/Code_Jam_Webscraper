#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <utility>
#include <functional>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <climits>
#include <cassert>
#include <memory>
#include <time.h>
using namespace std;
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef long long ll;
#define ALL(a) (a).begin(),(a).end()
#define RALL(a) (a).rbegin(),(a).rend()
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
const double EPS = 1e-9;
const double PI  = acos(-1.0);

int dy[]={-1,-1,-1,0,1,1,1,0};
int dx[]={-1,0,1,1,1,0,-1,-1,-1};

bool isInBoard(vs &board,int y,int x){
	return y>=0&&x>=0&&y<board.size()&&x<board[0].size();
}

bool canPropagate(vs &board,int y,int x){
	REP(d,8){
		int yy=y+dy[d];
		int xx=x+dx[d];
		if(isInBoard(board,yy,xx)&&board[yy][xx]=='*'){
			return false;
		}
	}
	return true;
}

void openBoard(vs &board,int y,int x){
	if(canPropagate(board,y,x)){
		REP(d,8){
			int yy=y+dy[d];
			int xx=x+dx[d];
			if(isInBoard(board,yy,xx)&&board[yy][xx]=='.'){
				board[yy][xx]='0';
				openBoard(board,yy,xx);
			}
		}
	}
}

bool canOpenInOneClick(vs board,int y,int x){
	if(board[y][x]=='.'){
		board[y][x]='0';
	}else{
		return false;
	}
	openBoard(board,y,x);
	REP(i,board.size()){
		REP(j,board[0].size()){
			if(board[i][j]=='.'){
				return false;
			}
		}
	}
}

vs generateBoard(string s,int h,int w){
	vs board(h,string(w,' '));
	REP(i,h){
		REP(j,w){
			board[i][j]=s[i*w+j];
		}
	}
	return board;
}

vs findAnswer(string s,int h,int w){
	do{
		vs board=generateBoard(s,h,w);
		REP(y,h){
			REP(x,w){
				if(canOpenInOneClick(board,y,x)){
					board[y][x]='c';
					return board;
				}
			}
		}
	}while(next_permutation(ALL(s)));
	return vs();
}

int main(){
	int numTests;
	cin>>numTests;
	REP(test,numTests){
		int h,w,m;
		cin>>h>>w>>m;
		cout<<"Case #"<<test+1<<": "<<endl;
		string s;
		REP(i,m){
			s+='*';
		}
		REP(i,h*w-m){
			s+='.';
		}
		vs answerBoard=findAnswer(s,h,w);
		if(answerBoard.size()==0){
			cout<<"Impossible"<<endl;
		}else{
			REP(i,h){
				cout<<answerBoard[i]<<endl;
			}
		}
	}
}