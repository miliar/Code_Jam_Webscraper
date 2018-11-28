// {{{ Boilerplate Code <--------------------------------------------------
// vim:filetype=cpp:foldmethod=marker:foldmarker={{{,}}}

#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

#define FOR(I,A,B) for(int I = (A); I < (B); ++I)
#define ALL(A)     (A).begin(), (A).end()

using namespace std;

// }}}

int dx[]={0,1,0,-1};
int dy[]={1,0,-1,0};

int inside(int x, int y, int R, int C){
	if(R<=x)
		return 0;
	if(C<=y)
		return 0;
	if(x<0)
		return 0;
	if(y<0)
		return 0;
	return 1;
}

int main(){
	int T;
	cin>>T;

	FOR(iteration,0,T){
		cout<<"Case #"<<(iteration+1)<<": ";
		int R;
		int C;
		cin>>R;
		cin>>C;

		char stage[100][100];

		FOR(i,0,R){
			FOR(j,0,C){
				char tmp;
				cin>>tmp;
				stage[i][j]=tmp;
			}
		}

		int ct=0;
		int impossible=0;

		FOR(x,0,R){
			FOR(y,0,C){
				if(impossible)
					break;

				int here=0;
				int ok=0;

				if(stage[x][y]=='.')
					continue;
				if(stage[x][y]=='>')
					here=0;
				if(stage[x][y]=='<')
					here=2;
				if(stage[x][y]=='v')
					here=1;
				if(stage[x][y]=='^')
					here=3;

				int tx=x,ty=y;

				while(1){
					tx+=dx[here];
					ty+=dy[here];

					if(!inside(tx,ty,R,C))
						break;

					if(stage[tx][ty]!='.'){
						ok=1;
						break;
					}
				}

				if(ok)
					continue;

				FOR(ve,0,4){
					tx=x;ty=y;
					if(ve==here)
						continue;

					while(1){
						tx+=dx[ve];
						ty+=dy[ve];

						if(!inside(tx,ty,R,C))
							break;

						if(stage[tx][ty]!='.'){
							ok=1;
							break;
						}
					}
					if(ok)
						break;
				}

				if(ok){
					ct++;
				}else{
					impossible=1;
				}

			}
		}

		if(impossible){
			cout<<"IMPOSSIBLE";
		}else{
			cout<<ct;
		}



		cout<<endl;
	}

}
