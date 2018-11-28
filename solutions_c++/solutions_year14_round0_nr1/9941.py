// googleJam.cpp : Defines the entry point for the console application.
//
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <iostream>

using namespace std;
int arr[4][4];
int main()
{
	freopen("A-small-attempt2.in", "r", stdin);
    freopen("A-small-attempt2.out", "w", stdout);
	int n;
	cin >> n;
	for(int i = 0; i < n; i++){
		bool b[16];
		int x;
		cin >> x;
		x--;
		for(int j = 0; j < 4; j++){
			for(int z = 0; z < 4; z++){
				cin >> arr[j][z];
				arr[j][z]--;
			}
		}
		for(int j = 0; j < 4; j++){
			b[arr[x][j]] = false;
		}
		cin >> x;
		x--;
		for(int j = 0; j < 4; j++){
			for(int z = 0; z < 4; z++){
				cin >> arr[j][z];
				arr[j][z]--;
			}
		}
		int c = 0;
		int index;
		for(int j = 0; j < 4; j++){
			if(!b[arr[x][j]]){
				c++;
				index = arr[x][j] + 1;
			}
		}
		if(c == 1){
			printf("Case #%d: %d\n",i+1,index);
		} else if(c == 0){
			printf("Case #%d: Volunteer cheated!\n",i+1);
		} else {
			printf("Case #%d: Bad magician!\n",i+1);
		}
		for(int j = 0; j < 16; j++){
			b[j] = true;
		}
	}
	return 0;
}

