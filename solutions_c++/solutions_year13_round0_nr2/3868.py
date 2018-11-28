#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

int caseNum;
int list[105][105];

int main(){
	int print_num;
	cin >> caseNum;

	int row,col;
	int next;
	bool fail = false;
	int temp;
	for(int i = 1; i <= caseNum; ++i){
		next = 105;
		fail = false;

		scanf("%d %d", &row, &col);
		for(int y = 0; y < row; ++y){
			for(int x = 0; x < col; ++x){
				scanf("%d", &list[y][x]);
			}
		}
		
		int k = 1;
		while(1){
			for(int y = 0; y < row; ++y){
				for(int x = 0; x < col; ++x){
					temp = list[y][x];
					if(k == temp){
						for(int xx = 0; xx < col; ++xx){
							if(list[y][xx] > temp){
								fail = true;
								break;
							}
						}
						if(fail){
							fail = false;
							for(int yy = 0; yy < row; ++yy){
								if(list[yy][x] > temp){
									fail = true;
									break;
								}
							}
							if(fail){
								break;
							}else{
								for(int yy = 0; yy < row; ++yy){
									if(list[yy][x] == temp){
										list[yy][x]--;
									}
								}
							}
						}else{
							for(int xx = 0; xx < col; ++xx){
								if(list[y][xx] == temp){
									list[y][xx]--;
								}
							}
						}
					}else if(k < temp){
						if(next > temp){
							next = temp;
						}
					}
				}
				if(fail) break;
			}
			if(next == 105) break;
			else{
				k = next;
				next = 105;
			}
			if(fail) break;
		}
		printf("Case #%d: %s\n", i, fail ? "NO" : "YES");
	}


	return 0;
}