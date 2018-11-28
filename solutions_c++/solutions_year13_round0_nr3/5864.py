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

bool palindrome(int x){
    int t = x, m = 0;
    do m = m*10 + t%10;
    while(t /= 10);
    return m == x;
}

int main(){

	freopen("C.in", "rt", stdin);
	freopen("C.out", "wt", stdout);

	int r,N,i;
	long count;
	long long X,Y,x,y;
	bool result = true;
	
   	cin >> N;

   	for(r=0;r<N;r++){
   		cout << "Case #" << r+1 << ": ";
		cerr << "Case #" << r+1 << ": ";

		cin >> X >> Y;
		
		x = ceil(sqrt(X));
		y = floor(sqrt(Y));
		count = 0;

		//cerr << "[" << X << "," << Y << "],{" << x << "," << y << "}" << endl;

		for(i=x;i<=y;i++){
			if(palindrome(i)){
				if(palindrome(i*i)) count ++;
			}
		}
	
		cout << count << endl;
		cerr << count << endl;
	}
}

