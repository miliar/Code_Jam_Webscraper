#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
#include <valarray>

using namespace std;

#define ALL(v) (v).begin(),(v).end()
typedef pair<int,int> pii;

int grid[128][128];

int main(){
	int nteste,teste;
	scanf("%d",&nteste);
	
	for(teste = 1; teste <= nteste; teste++){
		int n,m;
		scanf("%d %d",&n,&m);
		
		vector<int> maxl(n,-1);
		int i,j;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				scanf(" %d",&grid[i][j]);
		for(i=0;i<n;i++)
			maxl[i] = *max_element(&grid[i][0],&grid[i][m]);		
		
		for(j=0;j<m;j++){
			int mxeq=-1,mneq=200,up=-1;
			
			for(i=0;i<n;i++){
				if(grid[i][j] == maxl[i]){
					up = max(up,grid[i][j]);
				}else{
					mxeq = max(mxeq,grid[i][j]);
					mneq = min(mneq,grid[i][j]);
				}
			}
			if(mxeq != -1 && ( (mxeq != mneq) || (mxeq < up) ))
				break;			
		}
		printf("Case #%d: ",teste);
		if(j<m) printf("NO\n");
		else printf("YES\n");
	}
}
