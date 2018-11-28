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

	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);

	int T, c = 1;
	
   	cin >> T;

   	for(int c = 1; c <= T; c++){
   		cout << "Case #" << c << ": ";
		
	    int N;
	    cin >> N;
		vector<int> mushrooms(N);

		for (int i = 0; i < N; i++) cin >> mushrooms[i];

		int sol1 = 0;
		int sol2 = 0;
		int maxdiff = 0;
		int diff = 0;
	
		for(int i=1; i < N ; i++){
			diff = (mushrooms[i-1] - mushrooms[i]);
			sol1 += std::max(0,diff);
			maxdiff = std::max(maxdiff,diff);
		}

		for(int i=0; i < N-1 ; i++){
			sol2 += std::min(maxdiff, mushrooms[i]);
		}
		
		cout << sol1 << " " << sol2 << endl;
		
	}
}

