/* 
 * in the name of god 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 */ 

#include <iostream> 
#include <fstream> 
#include <sstream> 
#include <cstdio> 
#include <cstring> 
#include <cstdlib> 
#include <cmath> 
#include <ctime> 
#include <algorithm> 
#include <vector> 
#include <queue> 
#include <deque> 
#include <stack> 
#include <set> 
#include <map> 
#include <complex> 
#include <bitset> 
#include <iomanip> 
#include <utility> 

using namespace std; 

typedef long long LL; 
typedef pair<int,int> pii; 
typedef complex<double> point; 

const double eps = 1e-9;

int main(){
	int T; cin >> T;
	for (int i=1; i<=T; i++){
		cout << "Case #" << i << ": "; 
		double C,F,X; cin >> C >> F >> X;
		double ret = 0.0;
		double cur = 2.0;
		while (X/(cur+F) + C/cur < X/cur - eps){
			ret+= C/cur;
			cur+= F;
		}
		ret+= X/cur;
		cout << fixed << setprecision(10) << ret << endl;
	}
	return 0;
}
