#include <iostream>
#include <string>
#include <algorithm>
#include <stdio.h>
#include <vector>
using namespace std;

const int N = 105;

int main(){
	//freopen("1.txt","r",stdin);
	//freopen("2.txt","w",stdout);
	int numcase;
	cin >> numcase;
	for(int cnt = 1; cnt <= numcase; ++cnt){
	  int map[N][N];
	  for(int i = 0; i < N; ++i){
	     for(int j = 0; j < N; ++j)
			 map[i][j] = 0;
	  }
	  int row,col;
	  cin >> row >> col;
	  for(int i = 1; i <= row; ++i){
	     for(int j = 1; j <= col; ++j)
			 cin >> map[i][j];
	  }
	  bool flag = true;
	  for(int i = 1; i <= row; ++i){
		  for(int j = 1; j <= col; ++j){
		     int tmp = map[i][j];
			 bool flag1 = true, flag2 = true;
			 for(int k = 0;k <= col ; ++k){
				 if(map[i][k] > tmp){
				   flag1 = false;
				   break;
				 }
			 }
			 for(int k = 0; k <= row ; ++k){
				 if(map[k][j] > tmp){
				    flag2 = false;
					break;
				 }
			 }
			 if(!flag1 && !flag2){
				 flag = false;
				 break;
			 }
		  }
	  }
	  printf("Case #%d: ",cnt);
	  if(flag)
		  printf("YES\n");
	  else
		  printf("NO\n");
	}
	return 0;
}