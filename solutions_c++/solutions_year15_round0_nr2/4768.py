#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <queue>
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
#include <cstring> 

using namespace std; 

#define MAXM 1100000

char p[MAXM];  
int pos[MAXM];  
int m, k;

long long solveMaxHeight(int height, vector<int> plates){
	long long res = 0;
	for(int i = 0; i < plates.size(); ++i){
		res += plates[i]/height - 1;
		if(plates[i]%height > 0){
			++res;
		}
	}
	return res;
}

int main() {
	int t;
	cin>>t;
	for(int c = 1; c <= t; ++c){
		vector<int> plates;
		int n;
		cin>>n;
		while(n--){
			int a;
			cin>>a;
			plates.push_back(a);
		}

		long long best_sol = 1<<10;
		for (int i = 1; i <= 1000; ++i){
			long long special_days = solveMaxHeight(i, plates);
			best_sol = min(best_sol, special_days + i);
		}

		cout<<"Case #"<<c<<": "<<best_sol<<endl;
	}
}