#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <limits>
using namespace std;

int main(){
	freopen("C:\\in.txt", "r", stdin); //输入重定向，输入数据将从in.txt文件中读取 
	freopen("C:\\out.txt", "w", stdout); //输出重定向，输出数据将保存在out.txt文件

	int map[102][102];
	int maxRow[102], maxCol[102]; 
	int T, cnt = 0;
	scanf("%d", &T);
	while(T--){
		int N, M;
		scanf("%d%d", &N, &M);
		for(int i = 0; i < N; ++i)
			for(int j = 0; j < M; ++j)
				scanf("%d", &map[i][j]);
		
		for(int i = 0; i < N; ++i){
			maxRow[i] = map[i][0];
			for(int j = 1; j < M; ++j){
				if(map[i][j] > maxRow[i])
					maxRow[i] = map[i][j];
			}
		}

		for(int i = 0; i < M; ++i){
			maxCol[i] = map[0][i];
			for(int j = 1; j < N; ++j){
				if(map[j][i] > maxCol[i])
					maxCol[i] = map[j][i];
			}
		}

		bool ans = true;
		for(int i = 0; i < N; ++i){
			for(int j = 0; j < M; ++j)
				if(map[i][j] < maxRow[i] && map[i][j] < maxCol[j]){
					ans = false;
					break;
				}
			if(ans == false)
				break;
		}

		for(int i = 0; i < M; ++i){
			for(int j = 0; j < N; ++j)
				if(map[j][i] < maxCol[i] && map[j][i] < maxRow[j]){
					ans = false;
					break;
				}
				if(ans == false)
					break;
		}
		printf("Case #%d: %s\n", ++cnt, ans?"YES":"NO");
	}
}