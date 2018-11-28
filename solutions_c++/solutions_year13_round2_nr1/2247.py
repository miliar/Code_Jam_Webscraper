#include <iostream>
#include <algorithm>
#include <cmath>
#include <math.h>
#include <stdio.h>
#include <cstring>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <sstream>
#include <iomanip>

#define S               second
#define pi  		2 * acos(0.0)
#define sz(a)   	int((a).size()) 
#define pb 		push_back 
#define tr(c,i) 	for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) 	(find(all(c),x) != (c).end()) 

using namespace std;

int main(){
	int t, cs = 0;string s = "";
	cin >> t;
	while(t--){cs++;//cout << "Case #" <<cs <<": Draw" << endl;
		int ar[11];
		for(int i = 0; i < 11; i++){ar[i] = 0;}
		int a, n;
		cin >> a >> n;
		int br[n];
		for(int i = 0; i < n; i++){cin >>br[i];}
		sort(br,br+n);
		int ans = 0;
		int b = 0, c = 0, d = 0;
		while(true){c++;if(c == 1000)break;if(d == n)break;
			if(br[d] < a ) {a += br[d];d++;continue;}
			int e = n-d;
			int f = 0,g = a,h=0;bool flag = false;
			while(true){h++;if(h==1000)break;
				g += (g-1);
				f++;
				if(br[d] < g){flag = true;break;}
			}
			if(flag == false){ans += e;break;}
			if(flag == true &&f >= e){ans += e;break;}
			a = g;
			if(br[d] >= a)break;
			 if(br[d] < a ) {ans += f;a += br[d];d++;continue;}

		}
		cout << "Case #" <<cs <<": " <<ans << endl;
	}
        
	return 0;
}

