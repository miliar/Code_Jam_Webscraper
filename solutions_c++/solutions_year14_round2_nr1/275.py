#include<iostream>
#include<cstring>
#include<map>
#include<vector>
#include<string>
#include<set>
#include<queue>
#include<algorithm>
#include<cmath>

using namespace std;
vector<pair<char,int> > process ( string s ){
	vector<pair<char,int> > ret;
	char prev = '-' ; int cnt = 0 ;
	for ( int i=0 ; i<s.size() ; i++ ){
		if ( s[i] == prev ){
			cnt ++ ;
		}
		else {
			ret.push_back(make_pair(prev,cnt));
			cnt = 1;
			prev = s[i];
		}
	}
	ret.push_back(make_pair(prev,cnt));
	return ret;
}
int solve(vector< vector<pair<char,int> > >v ){
	for ( int i=0 ; i<v.size() ; i++ ){
		if ( v[i].size() != v[0].size() )
			return -1;
		for ( int j=0 ; j<v[0].size() ; j++ )
			if ( v[i][j].first != v[0][j].first )
				return -1;
	}
	int ret = 0 ;
	for ( int j=0 ; j<v[0].size() ; j++ ){
		int min_value = 10000 , max_value = -1;
		for ( int i=0 ; i<v.size() ; i++ ) {
			min_value = min ( min_value , v[i][j].second ) ;
			max_value = max ( max_value , v[i][j].second ) ;
		}
		int best_cost = 100000000 ;
		for ( int a = min_value ; a<=max_value ; a++ ){
			int cost = 0 ;
			for ( int i=0 ; i<v.size() ; i++ )
				cost += abs(v[i][j].second-a);
			best_cost = min ( best_cost , cost ) ;
		}
		ret += best_cost; 
	}
	return ret;
}
int main(){
	int tc;
	cin >> tc;
	for ( int test_case=1 ; test_case<=tc ; test_case++ ){
		cerr << test_case << " " << tc << endl;
		int n;string a , b;
		vector<vector<pair<char, int> > > v;
		cin >> n;
		for ( int i=0 ; i<n ; i++ ){
			string s;
			cin >> s;
			v.push_back(process(s));
		}
		int ret = solve(v);		
		cout << "Case #" << test_case << ": ";
		if ( ret == -1 ) cout << "Fegla Won" << endl;
		else cout << ret << endl;
	}
}
