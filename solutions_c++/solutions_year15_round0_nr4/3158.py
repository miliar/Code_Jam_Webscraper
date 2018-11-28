#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std; 

int main(){

	freopen("D-small-attempt4.in", "rt", stdin);
	freopen("D-small-attempt4.out", "wt", stdout);

	int r,N;
	int X,R,C;
	bool winRichards;
	
   	cin >> N;

   	for(r=0;r<N;r++){
   		cout << "Case #" << r+1 << ": ";
		
		cin >> X >> R >> C;
		bool winRichards = true;

        if((R*C)%X != 0){
           winRichards = true;
        }else if(X >= 7){
           winRichards = true;
        }else if(X <= 2){
           winRichards = false;
        }else if(X >= 2*min(R, C)){
            winRichards = true;
        }else{
            winRichards = false;
        }


		if(winRichards){
			cout << "RICHARD" << endl;
		}else{
			cout << "GABRIEL" << endl;
		}
		
	}
}

