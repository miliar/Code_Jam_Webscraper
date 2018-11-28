#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>

using namespace std;

int main(){
	//freopen("C:\Documents and Settings\Administrator\×ÀÃæ\in.txt", "r", stdin);
	//freopen("C:\Documents and Settings\Administrator\×ÀÃæ\out.txt", "w", stdout);
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int a[5][5], T;
	int tmp[16], f, l;
	cin >> T;
	int times = 0;
	while(T--){
		cin >> f;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				cin >> a[i][j];
			}
			if(i == f - 1){
				for(int j = 0; j < 4; j++){
					tmp[j] = a[i][j];
				}
			}
		}
		cin >> l;
		int cnt = 0, res;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				cin >> a[i][j];
			}
			
			if(i == l - 1){
				for(int j = 0; j < 4; j++){
					//cout << tmp[j] << " ";
					for(int k = 0; k < 4; k++){
						if(tmp[j] == a[i][k]){
							cnt++;
							res = tmp[j];
						}
					}
				}
			}
		}
		if(cnt == 1){
			printf("Case #%d: %d\n", ++times, res);
		}else if(cnt == 0){
			printf("Case #%d: Volunteer cheated!\n", ++times);
		}else{
			printf("Case #%d: Bad magician!\n", ++times);
		}
	}

	return 0;
}