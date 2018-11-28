

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>
#include <iostream>
#include <vector>
#include <utility>
#include <set>
#include <map>
#include <string>
#include <complex>
#include <functional>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <fstream>
using namespace std;

struct node{
	int val;
	int x, y;
};

node stage[10001];

int table[102][102];

bool cmp(const node &a, const node &b){
	if(a.val >= b.val)return true;
	else return false;
	//return false;
}

int main() {



	//freopen("D:/GCJ2013/B-small-attempt1.in","r", stdin);
	//freopen("D:/GCJ2013/B-small-attempt2.out", "w", stdout);
	freopen("D:/GCJ2013/B-large.in","r", stdin);
	freopen("D:/GCJ2013/B-large.out", "w", stdout);
	//
	//
	int t;
	int count;
	while(scanf("%d", &t) != EOF && t != 0){
		for(int num = 1; num <= t; num++){
			int n,m;
			int i, j;
			scanf("%d%d", &n, &m);
			count = 0;
			for(i = 0; i< (n * m + 1); i++){
				stage[i].val = 0;
				stage[i].x = stage[i].y = -1;
			}
			for(i = 0;i < n;i++)
				for(j = 0;j < m; j++){
					scanf("%d", &table[i][j]);
					stage[count].val = table[i][j];
					stage[count].x = i;
					stage[count++].y = j;
				}
			if(n == 1 || m == 1){
				printf("Case #%d: YES\n", num);
				continue;
			}
			//cout<<count<<endl;continue;
			//sort(stage, stage, cmp);
			//
			//node tmp;	
			//printf("count %d\n", count);
			//for(i = 0; i < count; i++) 	
			//	for(j = 0; j < count; j++)
			//		if(stage[i].val > stage[j].val){
			//			tmp = stage[i];
			//			stage[i] = stage[j];
			//			stage[j] = tmp;
			//		}
			////
			//
			//for(int k = 0; k < count; k++)
			//	printf("%d", stage[k].val);
			//printf("\n");
			//
		 	for(i = 0;i < count; i++){
				//if(i == count - 1)break;
				bool raw, col;
				raw = col = false;
				int x = stage[i].x;
				int y = stage[i].y;
				for(int tt = 0; tt < m; tt++){
					if(table[x][tt] > stage[i].val)break;
					if(tt == m - 1)col = true;
				}
				for(int tt = 0; tt < n; tt++){
					if(table[tt][y] > stage[i].val)break;
					if(tt == n - 1)raw = true;
				}
				if(raw || col){
					raw = col = false;
					continue;
				}
				else break;
			}	
			if(i == count)
				printf("Case #%d: YES\n", num);
			else 
				printf("Case #%d: NO\n", num);
		}
	}
	

    return 0;
}






