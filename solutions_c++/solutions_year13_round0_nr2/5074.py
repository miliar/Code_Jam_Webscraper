#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
using namespace std;

int lawn[100][100];
bool covered[100][100];

int main () {
	
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int T;
    int n, m;
    cin >> T;
    for (int t = 1; t <= T; t++) {
    	cin >> n >> m;
    	for (int i=0; i<n; i++) {
	    	for (int j=0; j<m; j++) {
	    		scanf("%d", &lawn[i][j]);
	    		covered[i][j] = false;
	    	}
	    }
	    if (n==1 || m==1) {
	    	printf("Case #%d: YES\n", t);
	    	continue;
	    }
	    // check the biggest of each row/col
	    for (int i=0; i<n; i++) {
	    	vector<int> bigjiji;
	    	int max = -1;
	    	for (int j=0; j<m; j++) {
	    		if (lawn[i][j] > max) {
	    			max = lawn[i][j];
	    			bigjiji.clear();
	    			bigjiji.push_back(j);
	    		}else if (lawn[i][j] == max){
	    			bigjiji.push_back(j);
	    		}
	    	}
	    	// bigjiji has all the maximum in row i
	    	for (int k=0; k<bigjiji.size(); k++) {
	    		covered[i][bigjiji[k]] = true;
	    		//printf("XD %d %d\n", i, bigjiji[k]);
	    	}
	    }
	    // col 
	    for (int j=0; j<m; j++) {
	    	vector<int> bigjiji;
	    	int max = -1;
	    	for (int i=0; i<n; i++) {
	    		if (lawn[i][j] > max) {
	    			max = lawn[i][j];
	    			bigjiji.clear();
	    			bigjiji.push_back(i);
	    		}else if (lawn[i][j] == max){
	    			bigjiji.push_back(i);
	    		}
	    	}
	    	// bigjiji has all the maximum in row i
	    	for (int k=0; k<bigjiji.size(); k++) {
	    		covered[bigjiji[k]][j] = true;
	    		//printf("XD %d %d\n", bigjiji[k], j);
	    	}
	    }
	    bool okk = true;
	    for (int i=0; i<n; i++) {
	    	for (int j=0; j<m; j++) {
	    		if (!covered[i][j]) {
	    			okk = false;
	    			break;
	    		}
	    	}
	    	if (!okk) break;
	    }
	    if (okk) {
	    	printf("Case #%d: YES\n", t);
	    }else {
	    	printf("Case #%d: NO\n", t);
	    }
	}   
}