#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std ;

int mul[5][5] = {
0,0,0,0,0,
0,1,2,3,4,
0,2,-1,4,-3,
0,3,-4,-1,2,
0,4,3,-2,-1
};

int map[1000];

void init() {
	map['i'] = 2 ;
	map['j'] = 3 ;
	map['k'] = 4 ;
}
int sign( int x ) {
	return x > 0 ? 1 : -1 ;
}

vector<int> calc( vector<int> a ) {
	vector<int> res ;
	res.clear();
	
	int now = 1 ;
	for ( int i = 0 ; i < a.size() ; ++i ) {
		int next = mul[ abs(now)][ abs(a[i])];
		int flag = sign(now) * sign(a[i]);
		
		now = next * flag ;
	}
	res.push_back(now);
	return res ;
}
vector<int> calc2( vector<int>a, vector<int>b ) {
	vector<int> c = a;
	for ( int i = 0 ; i < b.size() ; ++i )
		c.push_back( b[i] ) ;
	return calc(c);
}
vector<int> calcPre( vector<int> a ) {
	vector<int> res ;
	res.clear();
	
	int now = 1 ;
	for ( int i = 0 ; i < a.size() ; ++i ) {
		int next = mul[ abs(now)][ abs(a[i])];
		int flag = sign(now) * sign(a[i]);
		
		now = next * flag ;
		res.push_back(now);
	}
	return res ;
}
vector<int> calcSuf( vector<int> a ) {
	vector<int> res ;
	res.clear();
	
	int now = 1 ;
	for ( int i = a.size()-1 ; i >= 0 ; --i ) {
		int next = mul[ abs(a[i])][ abs(now)];
		int flag = sign(now) * sign(a[i]);
		
		now = next * flag ;
		res.push_back(now);
	}
	reverse(res.begin(),res.end());
	return res ;
}

vector<int> final , single;
vector<int> pre , suf ;
vector<int> read ;
vector<int> J , ijk ;

int main() {
	int test = 1 ;
	init();
	
	J.clear();
	J.push_back( map['j'] ) ;
	
	ijk.clear();
	ijk.push_back( map['i'] ) ;
	ijk.push_back( map['j'] ) ;
	ijk.push_back( map['k'] ) ;
	
	int T ;
	cin >> T ;
	while ( T-- ) {
		int L , n ;
		
		cin >> L >> n; 
		read.clear();
		for ( int i = 0 ; i < L ; ++i ) {
			char ch ;
			cin >> ch ;
			read.push_back( map[ch] ) ;
		}
		
		single = calc( read ) ;
		pre = calcPre( read ) ;
		suf = calcSuf( read ) ;
		
		int tmp = single[0];
		final.clear();
		for ( int i = 0 ; i < n ; ++i ) {
			final.push_back(tmp);
		}
		final = calc(final);	//	get the final answer
		
		bool ans = false ;
		
		if ( calc(ijk)[0] == final[0] ) {
		
			for ( int st = 0 ; ans == false && st < L ; ++st ) {
				for ( int ed = 0 ; ans == false && ed < L ; ++ed ) {
					vector<int> S1 ;
					S1.clear();
					S1.push_back(1);
					
					int cnt1 = 0 ;
					for ( int i = 0 ; ans == false && i < n && i < 8 ; ++i ) {
						
						vector<int> S2 ;
						S2.clear();
						S2.push_back(1);
						
						vector<int> ans1 = calc2(S1,vector<int>(1,pre[st]));
						
						if ( ans1[0] == map['i'] )
						for ( int j = 0 ; ans == false && j < n && j < 8 && i*L+st +j*L+L-ed < L*n ; ++j ) {
							
							vector<int> ans2 = calc2(vector<int>(1,suf[ed]),S2);
							
							if ( ans2[0] == map['k'] ) 
								ans = true ;
							
							
							S2.push_back(single[0]);
							S2 = calc(S2);
						}
						
						S1.push_back(single[0]);
						S1 = calc(S1);
					}
				}
			}
		}
		cout << "Case #" << test++ << ": " ;
		cout << (ans?"YES":"NO") << endl ;
	}
	
	return 0;
}