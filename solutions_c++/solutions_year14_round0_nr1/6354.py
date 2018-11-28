#include<iostream>
#include<vector>
#include<set>
using namespace std;


int main (){
	int tc;
	cin >> tc;
	for ( int C=1 ;C<=tc ; C++ ){
		set<int> s1[4] , s2[4];
		int first , second ;
		cin >> first;
		for ( int i=0 ; i<4 ; i++ )
			for ( int j=0 ; j<4 ; j++ ){
				int a;
				cin >> a;
				s1[i].insert(a);
			}
		cin >> second;
		for ( int i=0 ; i<4 ; i++ )
			for ( int j=0 ; j<4 ; j++ ){
				int a;
				cin >> a;
				s2[i].insert(a);
			}
		first -- , second -- ;
		int answer = -1 , answer_cnt = 0;
		for ( set<int>::iterator itr = s1[first].begin() ; itr != s1[first].end() ; itr ++ ){
			//cerr << "enumerating " << *itr << endl;
			if ( s2[second].find ( *itr ) != s2[second].end() ){
				answer_cnt ++ ;
				answer = *itr ;
			}
		}
		cout << "Case #" << C <<": " ;
		if ( answer_cnt > 1 ) cout << "Bad magician!" << endl;
		else if ( answer_cnt == 0 ) cout << "Volunteer cheated!" << endl;
		else cout << answer << endl;
		
	}
}
