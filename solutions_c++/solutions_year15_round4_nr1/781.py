/*
	In the Name Of GOD
	TRIPLE NARENGIES:)
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

const int MAXn = 117;
int r,c;
char jadval[MAXn][MAXn];
int table[MAXn][MAXn];


bool hasdot(){
	FOR(i,r){
		FOR(j,c){
			if(jadval[i][j]=='.'){
				// sh(i);
				// sh(j);
				return 1;
			}
		}
	}
	return 0;
}



void findvalue(){
	int tedad = 0;
	// FOR(i,r){
	// 	FOR(j,c){
	// 		if(r==0 && j==0){
	// 			continue;
	// 		}
	// 		if(r==0 && j==c-1)
	// 			continue;
	// 		if(i==r-1 && j==0)
	// 			continue;
	// 		if(i==r-1 && j==c-1)
	// 			continue;
	// 		if(i==0 && jadval[i][j]=='^') tedad++;
	// 		if(i==r-1 && jadval[i][j]=='v') tedad++;
	// 		if(j==0 && jadval[i][j] == '<') tedad++;
	// 		if(j==c-1 && jadval[i][j]=='>') tedad++; 
	// 	}
	// }
	// if(jadval[0][0]=='<'|| jadval[0][0]=='^') tedad++;
	// if(jadval[0][c-1]=='^' || jadval[0][c-1]=='>') tedad++;
	// if(jadval[r-1][0]=='<' || jadval[r-1][0]=='v') tedad++;
	// if(jadval[r-1][c-1]=='>' || jadval[r-1][c-1]=='v') tedad++;
	FOR(i,r){
		FOR(j,c){
			table[i][j]=0;
		}
	}
	FOR(i,r){
		FOR(j,c){
			if(jadval[i][j]!='.'){
				if(jadval[i][j]=='<')
					tedad++;
					table[i][j]++;
				break;
			}
		}
		for(int j=c-1;j>=0;j--){
			if(jadval[i][j]!='.'){
				if(jadval[i][j]=='>')
					tedad++;
					table[i][j]++;
				break;
			}
		}
	}
	FOR(j,c){
		FOR(i,r){
			if(jadval[i][j]!='.'){
				if(jadval[i][j]=='^')
					tedad++;
				table[i][j]++;
				break;
			}
		}
		for(int i=r-1;i>=0;i--){
			if(jadval[i][j]!='.'){
				if(jadval[i][j]=='v')
					tedad++;
					table[i][j]++;
				break;
			}
		}
	}
	FOR(i,r){
		FOR(j,c){
			if(table[i][j]==4){
				cout<<"IMPOSSIBLE"<<endl;
				return ;
			}
			// if(table[i][j])
			// 	tedad++;
		}
	}
	cout<<tedad<<endl;
	//return tedad;
}



int main()
{
	ios::sync_with_stdio(false);
	int T; cin>>T;
	int test = 0;
	while(T--)
	{
		test++;
		cout<<"Case #"<<test<<": ";
		cin>>r>>c;
		FOR(i,r){
			FOR(j,c){
				cin>>jadval[i][j];
			}
		}
		// if(r==1 && c==1){

		// 	cout<<0<<endl;
		// 	continue;
		// }
		// // if(hasdot()){
		// // 	cout<<"IMPOSSIBLE"<<endl;
		// // 	continue;
		// // }
		// if(r==1){
		// 	int tedad = 0;
		// 	if(jadval[0][0]!='>') tedad++;
		// 	if(jadval[0][c-1]!='<')tedad++;
		// 	cout<<tedad<<endl;
		// 	continue;
		// }
		// if(c==1){
		// 	int tedad = 0;
		// 	if(jadval[0][0]!='v') tedad++;
		// 	if(jadval[r-1][0]!='^')tedad++;
		// 	cout<<tedad<<endl;
		// 	continue;
		// }
		//cout<<findvalue()<<endl;
		findvalue();
	}
}
