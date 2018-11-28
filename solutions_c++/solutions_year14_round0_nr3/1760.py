#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <vector>
#include <string>
#include <cassert>
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;

const int SZ = 50;
char a[SZ][SZ];

void fill_board(char ch){
	for(int i=0; i<SZ; i++){
		for(int j=0; j<SZ; j++){
			a[i][j] = ch;
		}
	}
}

void print_board(ostream& cout, int n, int m){
	for(int i=0; i<n; i++){
		for(int j=0; j<m; j++){
			cout<<a[i][j];
		}
		cout<<endl;
	}
}

void fill(int diag, int& put, int k, int n, int m){
	for(int i=0; i<n && put<k; i++){
		for(int j=0; j<m && put<k; j++){
			if(i+j==diag &&
				!(i==n-1 && j==m-1) &&
				!(i==n-1 && j==m-2) &&
				!(i==n-2 && j==m-1) &&
				!(i==n-2 && j==m-2)){
				a[i][j] = '*';
				put++;
			}
		}
	}
}

int dx[] = {1,1,0,-1,-1,-1,0,1};
int dy[] = {0,-1,-1,-1,0,1,1,1};
bool found;

void go(int remain, int x, int y, int n, int m){
	if(remain==0){
		found = true;
		return;
	}
	char orig[SZ][SZ];
	memcpy(orig,a,SZ*SZ*sizeof(char));
	bool changed = false;
	for(int k=0; k<8; k++){
		int xn = x+dx[k];
		int yn = y+dy[k];
		if(xn>=0 && xn<n && yn>=0 && yn<m && a[xn][yn]!='.'){
			a[xn][yn] = '.';
			remain--;
			changed = true;
		}
	}
	if(!changed) return;
	if(remain==0){
		found = true;
		return;
	}else if(remain<0){
		memcpy(a,orig,SZ*SZ*sizeof(char));
		return;
	}
	for(int k=0; k<8 && !found; k++){
		int xn = x+dx[k];
		int yn = y+dy[k];
		if(xn>=0 && xn<n && yn>=0 && yn<m && a[xn][yn]!=orig[xn][yn]){
			go(remain, xn, yn, n, m);
		}
	}
	if(!found){
		memcpy(a,orig,SZ*SZ*sizeof(char));
	}
}

int main(){
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int ntests;
	cin>>ntests;
	for(int testnum=0; testnum<ntests; testnum++){
		int n, m, k;
		cin>>n>>m>>k;
		cout<<"Case #"<<testnum+1<<":"<<endl;
		if(k==n*m){
			cout<<"Impossible"<<endl;
			continue;
		}
		if(k==n*m-1){
			for(int i=0; i<n; i++){
				for(int j=0; j<m; j++){
					a[i][j] = '*';
				}
			}
			a[n-1][m-1] = 'c';
			print_board(cout, n, m);
			continue;
		}
		if(k==0){
			fill_board('.');
			a[0][0] = 'c';
			print_board(cout,n,m);
			continue;
		}
		if(n==1){
			fill_board('.');
			for(int i=0; i<k; i++) a[0][i] = '*';
			a[0][m-1] = 'c';
			print_board(cout, n, m);
			continue;
		}
		if(m==1){
			fill_board('.');
			for(int i=0; i<k; i++) a[i][0] = '*';
			a[n-1][0] = 'c';
			print_board(cout, n, m);
			continue;
		}
		fill_board('*');
		found = false;
		for(int i=0; i<n && !found; i++){
			for(int j=0; j<m && !found; j++){
				a[i][j] = '.';
				go(n*m-k-1,i,j,n,m);
				if(found) a[i][j] = 'c';
				else a[i][j] = '*';
			}
		}
		if(!found) cout<<"Impossible"<<endl;
		else print_board(cout, n, m);
	}
	return 0;
}
