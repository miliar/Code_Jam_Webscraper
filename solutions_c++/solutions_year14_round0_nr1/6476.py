#include <iostream>
#include <utility> 
#include <vector>
#include <stdio.h>
#include <algorithm> 
#include <string.h>
#include <set>

using namespace std;

#define MAX 20

int main(){

	
	int m1[MAX][MAX], m2[MAX][MAX], opt1, opt2, t, y;
	int flag;
	
	scanf("%d", &t);
	for (int i = 0; i < t; i++){
		scanf("%d", &opt1);
		for (int k = 0; k < 4; k++){
			for (int j = 0; j < 4; j++){
				scanf("%d", &m1[k][j]);
			}
		}
		scanf("%d", &opt2);
		for (int k = 0; k < 4; k++){
			for (int j = 0; j < 4; j++){
				scanf("%d", &m2[k][j]);
			}
		}
		flag = 0;
		y = -1;
		for (int k = 0; k < 4; k++){
			for (int j = 0; j < 4; j++){
				if (m1[opt1-1][k] == m2[opt2-1][j]){
					flag++;
					y = m1[opt1-1][k];
				}
			}
		}
		if(!flag){
			cout << "Case" << " #" << i+1 << ":" << " Volunteer cheated!";
		}
		else{
			if(flag == 1){
				cout << "Case" << " #" << i+1 << ":" << " " << y;
			}
			else cout << "Case" << " #" << i+1 << ":" << " Bad magician!";
		}
		cout << endl;
	}	
	
	return 0;
}