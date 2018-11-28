#include <iostream>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>
#include <string>
#include <list>

using namespace std;



int main(){
	//run. ./main < in.txt > out.txt
	//long long int l= (100/2)+3;
	//long long int r = (2*(long long int)std::pow(100,8)) + l;
	//cout << r << endl;
	int TC;
	cin >> TC;
	for(int tc=1;tc<=TC;tc++){
		printf("Case #%d: ", tc);
		int k, c, s;
		cin >> k >> c >> s;
		if(c==1 && s< k )
			cout << "IMPOSSIBLE" << endl;
		else if(c!=1 && s < ceil(k/2))
			cout << "IMPOSSIBLE" << endl;
		else if (c==1){
			for(int j=1;j<=k;j++){
				if (j==k)
					cout << j;
				else
					cout << j << " ";
			}
			cout << endl;
		}
		else{
			for(int j=0;j<(k+1)/2;j++){
				long long int r = j*(long long int)pow(k,c-1)+ ((long long int)(k/2+1+j));
				if(j==(k+1)/2-1)
					cout << r;
				else
					cout << r << " ";
			}
			cout << endl;
		}
	}
	return 0;
}