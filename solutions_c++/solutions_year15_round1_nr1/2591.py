// by Naciraa
#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <stack>
#include <queue>
#include <cstring>
#include <sstream>


using namespace std;

int in(){int r=0,c;for(c=getchar();c<=32;c=getchar());if(c=='-') return -in();for(;c>32;r=(r<<1)+(r<<3)+c-'0',c=getchar());return r;}


int main(){
	int cases;
	cin >> cases;
	int  y,z;
	
	for(int caso=1; caso<= cases; ++caso){
		int n;
		cin >> n;
		int m[n];
		z = 0;
		int max_diff=0;
		for(int i=0; i<n; ++i){
			cin >> m[i];
			if(i == 0){
				y = 0;
			}else{
				if(m[i] < m[i-1]){
					y += (m[i-1] - m[i]);
					
					if ((m[i-1] - m[i]) > max_diff){
						max_diff = (m[i-1] - m[i]);
					}
				}
			}
		}
		//~ cerr << "max:diff " << max_diff <<endl;
		for(int j=0; j<(n-1); ++j){
			if(m[j]<=max_diff){
				z += m[j];
			}else{
				z += max_diff;
			}
			//~ cerr << j << " " << z << endl;
		}
		
		
		cout << "Case #" << caso <<": " << y << " " << z << endl;
	}
	
	
return 0;
}

