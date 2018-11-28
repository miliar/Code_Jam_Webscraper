#include <bits/stdc++.h>

using namespace std ; 

class obj {
	public:
		int val ; 
		char label ; 
};

bool operator < ( obj a , obj b ) {
	if( a.val != b.val ) {
		return a.val < b.val ; 
	}
	return false ; 
}

void printResult( vector<string> res , int cas ) {
	cout << "Case #" << cas << ":" ; 
	
	for( int i = 0 ; i < res.size() ; i ++ ) {
		cout << " " << res[ i ] ;
	}
	cout << endl ; 
}

void solve( vector<int> &v , int cas ) {
	priority_queue<obj> q ; 
	
	int rem = 0 ; 
	for( int i = 0 ; i < v.size() ; i ++ ) {
		obj tmp ; 
		tmp.val = v[ i ] ;
		rem += v[ i ] ; 
		tmp.label = 'A' + i ; 
		q.push( tmp ) ; 
	}
	
	vector<string> res ;
	
	while( !q.empty() ) {
		obj cur = q.top() ; q.pop() ; 
		
		string curRes = "" ; 
		curRes += cur.label ; 
		
		cur.val -- ; 
		rem -- ; 
		
		if( cur.val != 0 ) q.push( cur ) ; 
		
		if( q.empty() ) {
			res.push_back( curRes ) ; 
			break ; 
		}
		
		obj snd = q.top() ;
		
		//cerr << "snd " << snd.val << endl ; 
		if( snd.val > ( rem / 2 ) ) {
			q.pop() ; 
			curRes += snd.label ; 
			snd.val -- ; 
			rem -- ; 
			if( snd.val != 0 ) q.push( snd ) ; 
		}
		
		res.push_back( curRes ) ; 
		
	}
	
	printResult( res , cas ) ; 
}

int main() {
	
	int T ; 
	
	cin >> T ; 
	
	for( int i = 0 ; i < T ; i ++ ) {
		int N ; 
		cin >> N ; 
		vector<int> v ; 
		for( int j = 0 ; j < N ; j ++ ) {
			int p ; 
			cin >> p ; 
			v.push_back( p ) ; 
		}
		solve( v , i + 1 ) ; 
	}
	return 0 ;
}
