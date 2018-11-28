#include <algorithm>
#include <bitset>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <limits>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <valarray>
#include <vector>


#define ll long long


using namespace std;
int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	ios::sync_with_stdio(false);
	cin.tie(0);
	int T, iT;
	cin >> T;
	for (int iT = 1; iT <= T; iT++){
		int smax;
		string audience;
		cin >> smax >> audience;
		int invited = 0, standing=0;
		for (int Si = 0; Si < audience.length(); Si++){
			
			int d = Si - standing;
				invited += max( d,0);
			

			
				standing += audience.at(Si) - '0' + max(d, 0);
		}
		cout <<"Case #"<<iT<<": "<< invited << "\n";
	}

}