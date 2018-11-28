#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

int main(){
	freopen("A-large (1).in", "r", stdin);
	freopen("A-large (1).out", "w+", stdout);
	int t;
    cin >> t;

	int motes;
	int ops;
	int size;
	int curmote;
	int motelist[100];

	for(int ti = 0; ti < t; ti++){
		cout << "Case #" << (ti+1) << ": ";
		cin >> size;
		cin >> motes;
		int motesleft = motes;
		int status;
		int safetystep = 0;
		int safetyops = 0;
		ops = 0;

		for(int mi = 0; mi < motes; mi++){
			cin >> motelist[mi];
		}
		sort(&motelist[0],&motelist[motes]);

		for(int mi = 0; mi < motes; mi++){
			curmote = motelist[mi];
			status = 1;
			if(size > curmote){
				size = size + curmote;
				if(ops <= (mi + 1)){
					safetystep = mi + 1;
				}
				motesleft--;
			}
			else{
				int tempops = 0;
				while(1){
					tempops++;
					size = size + size - 1;
					if((ops + tempops) > (safetyops + motes-safetystep)){
						ops = safetyops + motes-safetystep;
						status = 0;
						break;
					}
					if(size > curmote){
						size = size + curmote;
						motesleft--;
						ops = ops + tempops;
						if(ops <= (mi + 1)){
							safetystep = mi + 1;
							safetyops = ops;
						}
						status = 1;
						break;
					}
					else{
					}

					
				}
			}
			if(status == 0){break;}
			
		}
		cout << ops << endl;
	}
}