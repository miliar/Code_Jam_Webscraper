#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <valarray>
#include <vector>

#define EPS 1e-9
#define INF 1070000000LL
#define MOD 1000000007LL
#define fir first
#define foreach(it,X) for(__typeof((X).begin()) it=(X).begin();it!=(X).end();it++)
#define ite iterator
#define mp make_pair
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<(n);i++)
#define pb push_back
#define sec second
#define sz(x) ((int)(x).size())

using namespace std;

struct timer{
	time_t start;
	timer(){start=clock();}
	~timer(){cerr<<1.*(clock()-start)/CLOCKS_PER_SEC<<" secs"<<endl;}
};

typedef istringstream iss;
typedef long long ll;
typedef pair<int,int> pi;
typedef stringstream sst;
typedef vector<int> vi;

int N,M,P;
ll U[2010],V[2010],A[2010],B[2010];
int p[510];
ll way[1010][1010];
ll dist[1010][1010];

void main2(){
	cin>>N>>M>>P;
	rep(i,M){
		cin>>U[i]>>V[i]>>A[i]>>B[i];
		U[i]--,V[i]--;
	}
	rep(i,P){
		cin>>p[i];
		p[i]--;
	}
	
	int done=0;
	rep(ii,P){
		int ng=1;
		
		rep(mask,1<<M){
			
			rep(i,N)rep(j,N){
				way[i][j]=i==j?0:INF*INF;
			}
			rep(i,M){
				if(mask>>i &1){
					way[U[i]][V[i]] = min(way[U[i]][V[i]],A[i]);
				}
				else{
					way[U[i]][V[i]] = min(way[U[i]][V[i]],B[i]);
				}
			}
			rep(i,N)rep(j,N){
				dist[i][j]=way[i][j];
			}
			rep(k,N)rep(i,N)rep(j,N)dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j]);
			
			ll sug=0;
			int city=0;
			rep(i,ii+1){
				if(mask>>p[i] &1)sug += A[p[i]];
				else sug += B[p[i]];
				city = V[p[i]];
			}
			sug += dist[city][1];
			if(sug == dist[0][1]){
				ng=0;
				break;
			}
		}
		
		if(ng){
			cout<<p[ii]+1<<endl;
			done=1;
			break;
		}
	}
	
	if(!done)cout<<"Looks Good To Me"<<endl;
}

int main(){
	int T;
	cin>>T;
	time_t start=clock(),pre=start;
	rep(tc,T){
		cout<<"Case #"<<tc+1<<": ";
		main2();
		time_t now=clock();
		cerr<<tc+1<<"/"<<T<<": "<<(double)(now-pre)/CLOCKS_PER_SEC<<endl;
		if(tc==T-1){
			cerr<<"Total: "<<(double)(now-start)/CLOCKS_PER_SEC<<endl;
			cerr<<"  Ave: "<<(double)(now-start)/CLOCKS_PER_SEC/T<<endl;
		}
		pre=now;
	}
}
