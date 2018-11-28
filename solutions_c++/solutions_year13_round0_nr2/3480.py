#include<iostream>
#include<algorithm>
#include<fstream>
#include<vector>
#include<stack>
#include<queue>
#include<cmath>
#include<set>
#include<string>
#include<stdio.h>
#include<stdlib.h>
#include<sstream>
#include <stdio.h>

using namespace std;
const int maxn = 101;
int m,n,test;
int board[maxn][maxn];

bool check(int x , int y) {
	bool checkrow = true;
	bool checkcol = true;
	for(int j = 0 ; j < n ; j++) {
		if (board[x][y] < board[x][j]) {
			checkrow = false;
			break;
		}
	}
	
	for(int i = 0 ; i < m; i++) {
		if (board[x][y] < board[i][y]) {
			checkcol = false;
			break;
		}
	}
	return checkrow || checkcol;
}

string solve() {
	for(int i = 0 ; i < m ; i++) {
		for(int j = 0 ; j < n ; j++) {
			if (!check(i, j)) {
				return "NO";
			}
		}
	}
	return "YES";
}

int main(){
    cin>>test;
    string a;
    for(int t = 1;t<=test;t++){
        cin>>m>>n;
        for(int i = 0 ; i < m ; i++) {
        	for(int j = 0 ; j < n ; j++) {
        		cin>>board[i][j];
        	}
        }
        cout<<"Case #"<<t<<": ";
        cout<<solve();
        if (t < test) {
        	cout<<endl;
        }
    }               
}
