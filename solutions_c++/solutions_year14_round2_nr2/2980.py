#include <vector>
#include <list>
#include <map>
#include <set>
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

using namespace std;

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int T,count,A, B,C;
	unsigned int i,j,k,x,y, sum, carry;
	scanf("%d", &T);
	//cerr << "at " << km << endl;
	for(i=0;i<T;i++){
		scanf("%d", &A);
		scanf("%d", &B);
		scanf("%d", &C);
		count = 0;
		//cerr << "at " << A <<" " <<B << endl;
		for(k=0;k<A;k++){
			for(j=0;j<B;j++){
				sum = k&j;
				if((sum<C)){// && (k <=C)){
					count++;
				}
				//cerr << "Numbers " << k <<" " <<j <<" " <<sum << endl;
			}
		}
		//cerr << "at " << A <<" " <<B << endl;
		printf("Case #%d: %d\n",i+1,count);
	}
	
	return 0;
}
/*
5
3 4 2
4 5 2
7 8 5
45 56 35
103 143 88
*/
