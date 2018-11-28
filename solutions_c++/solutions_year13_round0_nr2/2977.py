#include <iostream>
#define HEI 100
#define WID 100
using namespace std;

bool executeloop();
void inputlawn(int[HEI][WID], int, int);
bool islegal(int[HEI][WID], int, int, int, int);
bool rowOK(int[HEI][WID], int, int, int, int);
bool colOK(int[HEI][WID], int, int, int, int);

int main(){
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		cout << "Case #" << i+1 << ": " << (executeloop() ? "YES" : "NO") << endl;
	}
}

bool executeloop(){
	int h, w;
	cin >> h >> w;
	int lawn[HEI][WID];
	inputlawn(lawn, h, w);
	for(int i = 0; i < h; i++){
		for(int j = 0; j < w; j++){
			if(!islegal(lawn,h,w,i,j)){
				return false;
			}
		}
	}
	return true;
}

void inputlawn(int lawn[HEI][WID], int h, int w){
	for(int i = 0; i < h; i++){
		for(int j = 0; j < w; j++){
			cin >> lawn[i][j];
		}
	}
}

bool islegal(int lawn[HEI][WID], int h, int w, int x, int y){
	return rowOK(lawn,h,w,x,y) || colOK(lawn,h,w,x,y);
}

bool rowOK(int lawn[HEI][WID], int h, int w, int x, int y){
	for(int i = 0; i < w; i++){
		if(lawn[x][i] > lawn[x][y]){
			return false;
		}
	}
	return true;
}

bool colOK(int lawn[HEI][WID], int h, int w, int x, int y){
	for(int i = 0; i < h; i++){
		if(lawn[i][y] > lawn[x][y]){
			return false;
		}
	}
	return true;
}