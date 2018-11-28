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
	for(int caso=1; caso<=cases; ++caso){
		int smax;
		cin >> smax;
		string k;
		cin >> k;
		int c = 0;
		char aux = '0';
		c = k[0] - aux;
		int res = 0;
		for(int j=0; j<smax+1; ++j){
			if((j == 0) && (c == 0)){
				res += 1;
				c += 1;
			}
			int p_aux = k[j] - aux;
			//cout << "k[" << j << "]: " << k[j] << "   " << "p_aux: " << p_aux << " c: "<< c << "  j: " << j << endl;
			if((c < j) && (p_aux != 0)){
				res += (j - c);
				c += (j - c);
				//cout << "res " << res << "   " << "p_aux: " << p_aux << " c: "<< c << "  j: " << j << endl;
			}
			
			if( j != 0 ){
				c += p_aux;
			}
		}
		cout << "Case #" << caso <<": " << res << endl;	
	}

return 0;
}

