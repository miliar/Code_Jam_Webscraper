/*
	In the Name Of GOD
*/
#include <vector>
#include <map>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <complex>
#include <queue>
#include <stack>
#include <map>
#include <bitset>
#include <iomanip>
#include <set>
#include <stack>
#include <stdio.h>

using namespace std;
#define N 10020
#define MAXN 60
#define X first
#define Y second
#define CLR(x,a) memset(x,a,sizeof(x))
#define FOR(i,b) for(ll i=0;i<(b);i++)
#define FOR1(i,b) for(ll i=1;i<=(b);i++)
#define FORA(i,a,b) for(ll i=(a);i<=(b);i++)
#define FORB(i,b,a) for(ll i=(b);i>=(a);i--)
#define sh(x) cerr<<(#x)<<" = "<<(x)<<endl
#define EPS 0.00001
#define ull unsigned long long int
#define ll long long 
#define MP make_pair
#define PB push_back
#define ALL(v) (v).begin(),(v).end()
#define sz size()
#define EXIST(a,b) find(ALL(a),(b))!=(a).end()
#define Sort(x) sort(ALL(x))
#define UNIQUE(v) Sort(v); (v).resize(unique(ALL(v)) - (v).begin())
#define timestamp(x) printf("Time : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC)
//const double PI = acos(-1);
typedef complex<double> point;
typedef pair<int,int> pii;
typedef pair<int, pii> piii;
typedef vector<int> vi;
typedef vector<vi > vii;
typedef vector<pii> vpii;
typedef vector<piii> vpiii;
int b,m;
int mat[6][6];
int tmpmat[6][6];
int mulmat[6][6];

void make(int x){
	for(int i=0;i<b;i++){
		for(int j=i+1;j<b;j++){
			mat[i][j] = tmpmat[i][j] = x%2;
			x/=2;
		}
	}
}


void mult(){
	FOR(i,b){
		FOR(j,b){
			mulmat[i][j] = 0;
			FOR(l,b){
				mulmat[i][j] += mat[i][l]*tmpmat[l][j];
			}
		}
	}
	FOR(i,b){
		FOR(j,b){
			mat[i][j] = mulmat[i][j];
		}
	}
}

int main()
{
	ios::sync_with_stdio(false);
	int T; cin>>T;
	int test = 0 ;
	while(T--)
	{
		test++;
		cout<<"Case #"<<test<<":";
		cin>>b>>m;
		bool win = 0;
		int last = (b-1)*b/2;
		for(int i=0;i<(1<<last);i++){
			make(i);
			int sum = 0;
			for(int i=0;i<b;i++){
				sum+=mat[0][b-1];
				mult();
			}
			if(sum==m){
				win = 1;
				cout<<" POSSIBLE"<<endl;
				FOR(i,b){
					FOR(j,b){
						cout<<tmpmat[i][j];
					}
					cout<<endl;
				}
				break;
			}
		}
		if(!win){
			cout<<" IMPOSSIBLE"<<endl;
		}
	}
}
