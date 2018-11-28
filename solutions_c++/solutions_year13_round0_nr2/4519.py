#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <string>
#include <map>
#include <math.h>
#include <stack>
#include <bitset>

using namespace std;


#define ii pair<int,int>
#define iii pair<int,ii>
typedef long long ll;
typedef unsigned long long ull;

int peta[103][103];
int x_peta,y_peta;

bool cek_H(int x,int y){

	int cari=peta[x][y];

	for(int i=x-1;i>=0;i--){
		if(peta[i][y]>cari)return false;
	}

	for(int i=x+1;i<x_peta;i++){
		if(peta[i][y]>cari)return false;
	}

	return true;
}

bool cek_V(int x,int y){
	int cari=peta[x][y];

	for(int i=y-1;i>=0;i--){
		if(peta[x][i]>cari)return false;
	}

	for(int i=y+1;i<y_peta;i++){
		if(peta[x][i]>cari)return false;
	}

	return true;
}


int main (){

	//freopen("B-large.in","r",stdin);	freopen("iseng.txt","w",stdout);

	int t;

	scanf("%d",&t);

	for(int kasus=1;kasus<=t;kasus++){

		int hitung=0;

		scanf("%d %d",&x_peta,&y_peta);

		for(int i=0;i<x_peta;i++)for(int j=0;j<y_peta;j++){
			scanf("%d",&peta[i][j]);
		}

		for(int i=0;i<x_peta;i++)for(int j=0;j<y_peta;j++){
				if(cek_H(i,j)==true || cek_V(i,j)==true){
					hitung++;
				}
		}

		printf("Case #%d: ",kasus);


		if(hitung==(x_peta*y_peta)){
			printf("YES\n");
		}
		else printf("NO\n");

	}

}





