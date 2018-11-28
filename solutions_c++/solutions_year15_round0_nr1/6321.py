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

char B[4][4];

int main(){

	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);

	int r,N,i,j;
	int max;
	int friends;
	int stand;
	std::string shyness;
	
   	cin >> N;

   	for(r=0;r<N;r++){
   		cout << "Case #" << r+1 << ": ";
		
		cin >> max;
		cin >> shyness;

		friends = 0;
		stand = 0; 
		
		for(i=0; i <= max ; i++){
			friends += std::max(0, i - stand - friends);
			stand += (int)(shyness[i] - '0'); 
		}

		cout << friends << endl;
		
	}
}

