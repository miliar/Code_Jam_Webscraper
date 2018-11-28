#include <iostream>
#include <string>
#include <vector>
#include <thread>
#include <algorithm>
#include <string>
using namespace std;

typedef unsigned long long int ull;

ull ans[100]={0};

	bool check( const vector<string> & arr, const vector<int> & );

	void Solve( int idx, vector<string> arr ) {
		ans[idx] = 0;

		sort( arr.begin(), arr.end() );
		vector<int> order( arr.size() );
		iota( order.begin(), order.end(), 0 );

		do{
			
			bool ok = check(arr, order);
			//cout << " " << boolalpha << ok << "\n";
			if( ok ){
				ans[idx]++;
				if( ans[idx] >  1000000007 ){
					ans[idx] %= 1000000007;
				}
			}
		}while( next_permutation(order.begin(), order.end() ) );
	}

	bool check( const vector<string> & arr, const vector<int> & ord){
		string temp ;
		int occ[26] = {0};
		for( int i=0; i<ord.size(); i++) temp += arr[ ord[i] ];

		//cout << temp << ": ";

		for( int i=0; i<temp.size(); i++){
			int c=temp[i] - 'a';
			if( occ[c] == 0 ){
				occ[c] = 1;
				continue;
			}else{
				if( temp[i-1] != temp[i] ) return false;
			}
		}
		return true;
	}

int main(){
	int Case; 
	cin >> Case;
	vector<thread> tid;

	for( int t=1; t<=Case; t++){
		int n;
		vector<string> arr;
		cin >> n ;

		string temp;

		arr.reserve(n);

		while( n-- ){
			cin >> temp;
			arr.push_back(temp);
		}

		tid.emplace_back( Solve, t-1, arr );
	}
	for( int i=0; i<tid.size(); i++){
		tid[i].join();
		cout << "Case #" << i+1 << ": " << ans[i] << "\n";
	}
}
