/*
 * B.cpp
 *
 *  Created on: 2013-4-13
 *      Author: chen
 */

#include<iostream>
using namespace std;
#define max(a,b) (a>b?a:b)
int grid[124][124];
int col[124],row[124];
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int cases,cas;
	cin >> cases;
	int n,m;
	for(int cas = 1; cas <= cases; cas++){
		cin >> n >> m;
		memset(col,0,sizeof(col));
		memset(row,0,sizeof(row));
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				cin >> grid[i][j];
				row[i] = max(row[i],grid[i][j]);
			}
		}
		for(int j=0;j<m;j++){
			for(int i=0;i<n;i++){
				col[j] = max(col[j],grid[i][j]);
			}
		}
		bool result = true;
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				if(grid[i][j] != col[j] && grid[i][j] != row[i]){
					result = false;
					break;
				}
			}
			if(!result)break;
		}
		printf("Case #%d: %s\n",cas,result ? "YES" : "NO");
	}
	return 0;
}

