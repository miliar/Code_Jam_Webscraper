#define _CRT_SECURE_NO_WARNINGS

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <queue>
#include <cstring>
#include <string>
#include <complex>

#define vi vector<int>
#define vpii vector< pair<int,int> >
#define pii pair<int,int>
#define mp(x,y) make_pair(x,y)
#define all(x) (x).begin(),(x).end()
#define FOREACH(it,x) for (auto it = (x).begin(); it!=(x).end(); ++it) 
#define sz(x) (int)(x).size()
#define FOR(i,n) for (ll i = 0; i < ll(n); i++)
#define REP(i,a,b) for (ll i = a; i < ll(b); i++)
#define READ(a) int a; scanf("%d", &a);
#define READV(v,n) vi v(n);FOR(i,n){scanf("%d", &v[i]);}
#define WRITE(v) FOR(i,sz(v))cout<<v[i]<<" ";
#define gmin(a,b) { if (b < a) a = b; }
#define gmax(a,b) { if (b > a) a = b; }
#define pb push_back
#define ff first
#define ss second
#define oo ((1LL<<62)+((1LL<<31)-1))
const double PI = std::atan(1.0)*4;

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

int r,c;
vector<string> board;
int dx[4] = {0,1,0,-1};
int dy[4] = {-1,0,1,0};
char dc[4] = {'^','>','v','<'};

bool onBoard(int rr, int cc){
	return rr>=0 && rr<r && cc>=0 && cc<c;
}

int main(){
    READ(T);
	FOR(t,T){
		cin>>r>>c;
		board = vector<string>(r);
		FOR(i,r){
			cin>>board[i];
		}
		int res = 0;
		FOR(rr,r){
			FOR(cc,c){
				if(board[rr][cc]=='.') continue;
				int numout = 0;
				FOR(d,4){
					int p = 1;
					bool out = false;
					while(true){
						if(!onBoard(rr+dy[d]*p, cc+dx[d]*p)){
							out = true; break;
						}
						if(board[rr+dy[d]*p][cc+dx[d]*p]!='.'){
							out = false; break;
						}
						p++;
					}
					if(out) numout++;
					if(out && dc[d]==board[rr][cc]){
						res++;
					}
				}
				if(numout==4) {goto bad;}
			}
		}


		cout<<"Case #"<<(t+1)<<": "<<res<<endl; 
		continue;
		bad:
		cout<<"Case #"<<(t+1)<<": "<<"IMPOSSIBLE"<<endl; 
	}

    return 0;
}
