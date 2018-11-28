#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <sstream>
#include <functional>
#include <map>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <list>
using namespace std;
const double PI = 3.14159265358979323846;

int g[100][100];
int N,M;

bool check(int a, int b){
	bool fr = true,fc = true;
	for(int i = 0; i < N; i++){
		if(g[i][b] > g[a][b])fc = false;
	}
	for(int j = 0; j < M; j++){
		if(g[a][j] > g[a][b])fr = false;
	}
	
	return fr || fc;
}

int main(){
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		cin>>N>>M;
		for(int i = 0; i < N; i++){
			for(int j = 0; j < M; j++){
				scanf("%d",g[i]+j);
			}
		}
		
		bool flag = true;
		
		for(int i = 0; i < N; i++){
			for(int j = 0; j < M; j++){
				if(!check(i,j))flag = false;
			}
		}
		printf("Case #%d: ",Case);
		if(flag){
			cout<<"YES"<<endl;
		}else {
			cout<<"NO"<<endl;
		}
	}
	return 0;
}
