//Esteban Foronda Sierra
using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

template <class T> string toStr(const T &x)
{ stringstream s; s << x; return s.str(); }
template <class T> int toInt(const T &x)
{ stringstream s; s << x; int r; s >> r; return r;}

#define D(x) cout << #x " is " << x << endl
#define MAXN 1005


int main(){
	int n;
	cin >> n;
	int cases = 1;
	while(n--){
		int d;
		cin >> d;
		int numbers[d];
		int maxi = -1;
		for(int i = 0; i < d; ++i){
			cin >> numbers[i];
			maxi = max(maxi, numbers[i]);
		}
		int ans = maxi;
		for(int x = 1; x < maxi; ++x){
			int aux = 0;
			for(int i = 0; i < d; ++i) {
				if(numbers[i] > x) aux += ((numbers[i] - 1)/x);
			}
			aux += x;
			ans = min(ans, aux);
		}
		printf("Case #%d: %d\n", cases++, ans); 
	}
	return 0;
}




