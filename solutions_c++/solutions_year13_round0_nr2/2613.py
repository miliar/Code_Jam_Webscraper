#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <deque>

#define REP(i,n) for(int i=0;i<(n);i++)
#define REPA(i,a,n) for(int i=(a);i<((a)+(n));i++)
#define INITW(var,value,width) for(int whslkfje=0;whslkfje<(width);whslkfje++) var[whslkfje]=(value)
#define INITHW(var,value,height,width) for(int hwesaft=0;hwesaft<(height);hwesaft++) \
		 for(int whslkfje=0;whslkfje<(width);whslkfje++) var[hwesaft][whslkfje]=(value)

typedef long long lint;
using namespace std;
void solve();
void init();

int main(){
	init();

	int T;
	cin>>T;
	string str;
	getline(cin, str);
	
	for(int t=1;t<=T;t++){
		cout<<"Case #"<<t<<": ";
		solve();
		cout<<"\n";
	}
}

void init(){
	
}
int n,m;
int field[105][105];

bool rowreach(int i,int j){
	REP(k,m)if(field[i][k]>field[i][j])return false;
	return true;
}
bool colreach(int i,int j){
	REP(k,n)if(field[k][j]>field[i][j])return false;
	return true;
}

bool reach(int i,int j){
	if(rowreach(i,j))return true;
	if(colreach(i,j))return true;
	return false;
}

bool reachable(){
	REP(i,n)REP(j,m){
		if(!reach(i,j))return false;
	}
	return true;
}

void solve(){
	cin>>n>>m;
	REP(i,n)REP(j,m)cin>>field[i][j];
	if(reachable())cout<<"YES";
	else cout<<"NO";
}
