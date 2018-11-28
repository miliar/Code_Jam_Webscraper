#include <string>
#include <iostream>
#include <cmath>

using namespace std;

int n, m, a[105][105], tgt[105][105];

string solve(){
	cin >> n >> m;
	for(int i = 0; i < n; ++i)
		for(int j = 0; j < m; ++j)
			cin >> tgt[i][j];
	
	for(int i = 0; i < n; ++i)
		for(int j = 0; j < m; ++j)
			a[i][j] = 100;
			
	// for each line cut the grass to the maximum from that line
	for(int i = 0; i < n; ++i){
		int largest = 0;
		for(int j = 0; j < m; ++j)
			largest = max(largest, tgt[i][j]);
				
		for(int j = 0; j < m; ++j)
			a[i][j] = largest;
	}
	
	// for each column cut the grass to the minimum from that column
	for(int j = 0; j < m; ++j){
		bool change = false;
		for(int i = 0; i < n; ++i)
			if(a[i][j] != tgt[i][j])
				change = true;
		
		if(!change)
			continue;
		
		int smallest = 101;
		for(int i = 0; i < n; ++i)
			smallest = min(smallest, tgt[i][j]);
				
		for(int i = 0; i < n; ++i)
			a[i][j] = smallest;
	}
	
	for(int i = 0; i < n; ++i)
		for(int j = 0; j < m; ++j)
			if(a[i][j] != tgt[i][j])
				return "NO";
	
	return "YES";
}

int main()
{
	int t;
	cin >> t;
	
	for(int testNo = 0; testNo < t; ++testNo)
		cout << "Case #" << (testNo+1) << ": " << solve() << endl;
	return 0;
}
