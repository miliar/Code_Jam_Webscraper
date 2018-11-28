// Standard I/O
#include <iostream>
#include <sstream>
#include <cstdio>
// Standard Library
#include <cstdlib>
#include <ctime>
#include <cmath>
// Template Class
#include <string>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <stack>
// Container Control
#include <algorithm>

using namespace std;

#define rep( i, n ) for( int i = 0; i < n; ++i )
#define reep( i, s, n ) for ( int i = s; i < n; ++i )

typedef vector<int>::iterator vi_itr;
typedef list<int>::iterator li_itr;

typedef pair<int, int> pii;
typedef list<int> li;
typedef vector<int> vi;
typedef vector< vector<int> > vii;

int main()
{
	int N;
	int field[4][4][2];

	cin >> N;
	rep(n, N){
		int row[2];

		rep(i, 2){
			cin >> row[i];
			--row[i];
			rep(j, 4){
				rep(k, 4){
					cin >> field[j][k][i];
				}
			}
		}

		bool exist[20][2] = { false };
		rep(i, 2){
			rep(j, 4){
				exist[field[row[i]][j][i]][i] = true;
			}
		}

		vi choose;
		rep(i, 20){
			if( exist[i][0] && exist[i][1] ){
				choose.push_back( i );
			}
		}

		cout << "Case #" << n+1 << ": ";
		if( choose.size() == 0 ){
			cout << "Volunteer cheated!" << endl;
		}
		else if( choose.size() == 1 ){
			cout << choose[0] << endl;
		}
		else{
			cout << "Bad magician!" << endl;
		}
	}
}
