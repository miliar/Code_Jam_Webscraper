#include <iostream>
#include <math.h>
#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

bool isvalid(int x,int y,int fi[100][100],int N,int M){
	
	bool is_h=true,is_v=true;

	//check the horizontal field path
	int fieldheight = fi[x][y];
	for (int i = 0; i < M; ++i){
		if(fi[x][i] > fieldheight) is_h = false;
	}
	//check the vertial field path
	for (int i = 0; i < N; ++i){
		if(fi[i][y] > fieldheight) is_v = false;
	}
	if(!is_h && !is_v) return false;
	return true;
}


int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	int caseno;
	scanf("%d",&caseno);
	int field[100][100] = {0};
	bool ispossible;
	for(int case_id=0;case_id<caseno;case_id++){
		ispossible = true;
		int N,M;
		cin >> N >> M;
		for(int i=0;i<N;i++){
			for(int j=0;j<M;j++){
				int d;
				cin >> d;
				field[i][j] = d;
			}
		}

		for(int i=0;i<N;i++){
			for(int j=0;j<M;j++){
				if(field[i][j] < 100){ //the lawn has mowed the field in this square
					ispossible = isvalid(i,j,field,N,M);
					if(!ispossible) break;						
				}
			}
			if(!ispossible) break;
		}
		if(ispossible) cout << "Case #" << case_id+1 << ": " << "YES" << endl;
		else cout << "Case #" << case_id+1 << ": " << "NO" << endl;
	}
	return 0;
}