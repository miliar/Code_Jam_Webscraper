#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
using namespace std;

int main() {
	int T, D, m, m1, temp;
	cin >> T;
	vector<int> v;
 	for(int i=1; i<=T; i++){
		v.clear();
		cin >> D;
		m =0 ;
		for(int j=0; j<D; j++){
			cin >> temp;
			v.push_back(temp);
			m = max(m, temp);
		}
		int count =0 ;
		m1 = m;
		for (int j = 2; j<m; j++){
		
			count = 0;
			for(int k =0; k<D; k++){
				count = count + ceil(v[k]*1.0/j) -1 ;
			}
			
			m1 = min(m1, count+j);
 		}
 		cout <<"Case #" << i <<  ": " << m1 <<endl ;
	}



	return 0;
}