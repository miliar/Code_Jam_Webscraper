#include <iostream>
#include <algorithm>
using namespace std;

const int MAX_NM = 100;
const int ROW = 0;
const int COL = 1;
int d_lawn[MAX_NM][MAX_NM];
int lawn[MAX_NM][MAX_NM];
bool visit[2][MAX_NM];

int N, M, T;
//
//int isPossibleToMow(int idx, int TYPE){
//	int h1 = 0;
//	int h2 = 0;
//	int h = 0;
//	if(TYPE == ROW){
//		for(int j = 0; j < M; j++){
//			h1 = max(h1, d_lawn[idx][j]);
//			h2 = min(h2, lawn[idx][j]);
//		}
//		h = h2 - h1;
//		if(h <= 0) return -1;
//		
//		return h;
//	}else{
//		for(int i = 0; i < N; i++){
//			h1 = max(h1, d_lawn[i][idx]);
//			h2 = min(h2, lawn[i][idx]);
//		}
//		h = h2 - h1;
//		if(h <= 0) return -1;
//		
//		return h;
//	}
//	return -1;
//}
//
//void Mowing(int idx, int TYPE, int h){
//	if(TYPE == ROW){
//		for(int j = 0; j < M; j++)
//			lawn[idx][j] = h;
//	}else{
//		for(int i = 0; i < N; i++)
//			lawn[i][idx] = h;
//	}
//}
//void Pasting(int idx, int TYPE, int h){
//	if(TYPE == ROW){
//		for(int j = 0; j < M; j++)
//			lawn[idx][j] = h;
//	}else{
//		for(int i = 0; i < N; i++)
//			lawn[i][idx] = h;
//	}
//}
//
//bool checkLawn(){
//	for(int i = 0; i < N; i++){
//		for(int j = 0; j < M; j++){
//			if(d_lawn[i][j] != lawn[i][j]) return false;
//		}
//	}
//	return true;
//}
//
////bool dfs()
////{
////	if(checkLawn()) return true;
////	int h = 0;
////	//spreading from rows
////	for(int i = 0; i < N; i++){		
////		if(isPossible(i, ROW, 1)){
////			Mowing(i, ROW, 1);
////			if(dfs()) return true;
////			Pasting(i, ROW, 1);
////		}
////	}
////
////	//spreading from columns
////	for(int j = 0; j < M; j++){
////		if(isPossible(j, COL, 1)){
////			Mowing(j, COL, 1);
////			if(dfs()) return true;
////			Pasting(j, COL, 1);
////		}
////	}
////
////	return false;
////}
////
////bool dfs(int row, int col){
////	if(checkLawn())				return true;
////	if(row >= N || col >= M) 	return checkLawn();
////	int h = 0;
////	if((h = isPossibleToMow(row, ROW)) != -1){
////		Mowing(row, ROW, h);
////		if(dfs(row+1, col)) return true;
////		Pasting(row, ROW, h);
////	}
////	if(dfs(row+1, col)) return true;
////
////	if((h = isPossibleToMow(col, COL)) != -1){
////		Mowing(col, COL, h);
////		if(dfs(row, col+1)) return true;
////		Pasting(col, COL, h);
////	}
////	if(dfs(row, col+1)) return true;
////
////	return false;
////}
//
//bool isPossible(int idx, int TYPE, int &max_height){
//	max_height = 0;
//	if(TYPE == ROW){
//		for(int j = 0; j < M; j++)
//			max_height = max(max_height, d_lawn[idx][j]);
//
//		int cnt = 0;
//		for(int j = 0; j < M; j++){
//			if(lawn[idx][j] < max_height) return false;
//			if(lawn[idx][j] == max_height) cnt++;
//		}
//		if(cnt == M) return false;
//		return true;
//	}else{
//		for(int i = 0; i < N; i++)
//			max_height = max(max_height, d_lawn[i][idx]);
//		int cnt = 0;
//		for(int i = 0; i < N; i++){
//			if(lawn[i][idx] < max_height) return false;
//			if(lawn[i][idx] == max_height) cnt++;
//		}
//		if(cnt == N) return false;
//		return true;
//	}
//	return false;
//}
//
//bool dfs(){
//	if(checkLawn()) return true;
//	//row
//	for(int i = 0; i < N; i++){
//		int max_height = 0;
//		if(!visit[ROW][i] && isPossible(i, ROW, max_height)){
//			visit[ROW][i] = true;
//			int trow[MAX_NM];
//			for(int j = 0; j < M; j++){
//				trow[j] = lawn[i][j];
//				lawn[i][j] = max_height;
//			}
//
//			if(dfs()) return true;
//			
//			for(int j = 0; j < M; j++)
//				lawn[i][j] = trow[j];
//			visit[ROW][i] = false;
//		}
//	}
//
//	//column
//	for(int j = 0; j < M; j++){
//		int max_height = 0;
//		if(!visit[COL][j] && isPossible(j, COL, max_height)){
//			visit[COL][j] = true;
//			int tcol[MAX_NM];
//			for(int i = 0; i < N; i++){
//				tcol[i] = lawn[i][j];
//				lawn[i][j] = max_height;
//			}
//
//			if(dfs()) return true;
//			
//			for(int i = 0; i < N; i++)
//				lawn[i][j] = tcol[i];
//			visit[COL][j] = false;
//		}
//	}
//
//	return false;
//}

int cnt[MAX_NM];
int main()
{
	int num = 1;
	cin>>T;
	while(T--){
		cin>>N>>M;
		int max_height = 0;
		memset(cnt, 0, sizeof(cnt));
		for(int i = 0; i < N; i++){
			for(int j = 0; j < M; j++){
				cin>>d_lawn[i][j];
				cnt[ d_lawn[i][j] ]++;
				max_height = max(max_height, d_lawn[i][j]);
			}
		}
		int width = M;
		int height = N;
		
		for(int h = 1; h <= max_height; h++){
			//가로로 지울 수 있는 것은 다 지운다.			
			for(int i = 0; i < N; i++){
				int k = 0;
				for(int j = 0; j < M; j++)	
					if(d_lawn[i][j] == h) k++;

				if(k == width){
					for(int j = 0; j < M; j++)	d_lawn[i][j] = -1;
					cnt[h] -= k;
					height--;
				}
			}
			//세로로 지울 수 있는 것은 다 지운다.
			for(int j = 0; j < M; j++){
				int k = 0;
				for(int i = 0; i < N; i++)
					if(d_lawn[i][j] == h) k++;
				if(k == height){
					for(int i = 0; i < N; i++) d_lawn[i][j] = -1;
					cnt[h] -= k;
					width--;
				}
			}
		}

		
		cout<<"Case #"<<num++<<": ";
		
		//남은 것을 세본다.
		bool flag = true;
		for(int h = 1; h <= max_height; h++){
			if(cnt[h] != 0) {
				flag = false;
				break;
			}
		}
		if(flag) cout<<"YES"<<endl;
		else	 cout<<"NO"<<endl;
	}
	return 0;
}