#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include<string.h>
using namespace std;

//bool mat[10][10];
//int x[]= {1, -1, 0, 0};
//int y[]= {0, 0, 1, -1};
//int R,C,X;
//
//void dfs(int r, int c, int count) {
//	if(count == X){
//
//	}
//	else if(!mat[r][c]){
//		mat[r][c] = 1;
//	}
//}

int main(){
	freopen("out.txt","w",stdout);
	freopen("in.txt","r",stdin);
	int  t,x,r,c;
	cin>>t;
	for (int i = 0; i < t; i++) {
		cin>>x>>r>>c;
		cout <<"Case #"<<i+1<<": ";
		if(x == 2 && r*c %2 != 0){
			cout << "RICHARD\n";
		}
		else if(x == 3) {
			if((r*c == 3) || (r*c % 3) != 0)
				cout << "RICHARD\n";
			else 
				cout << "GABRIEL\n";
		}
		else if(x == 4){
			if((r*c <= 8) || (r*c % 4) !=  0)
				cout << "RICHARD\n";
			else 
				cout << "GABRIEL\n";
		}
		else 
			cout << "GABRIEL\n";
	}
}
