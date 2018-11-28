
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <utility>
#include <math.h>
#include <fstream>

using namespace std;
typedef long double ld;

const ld EPS = 10e-14;
const ld pi = 3.14159265358979323846264338327950288;

void solve1();

int cnt = 1;

ofstream ofs("result.txt");

int main( void ) {

	//FILE *fpin = freopen("data.txt","r",stdin);

	int N;
	cin >> N;

	for( int i = 0; i < N; i++ )
		solve1();

	ofs.close();

	return 0;
}

void solve1() {

	//貪欲
	ofs << "Case #" << cnt << ":";

	int T;
	cin >> T;
	vector< int > p(T);
	int sum = 0;

	for( int i = 0; i < T; i++ ) {
		cin >> p[i];
		sum += p[i];
	}

	while( sum > 0 ) {

		//最大党
		vector< int > v(p);
		int m[2] = { -1, -1 };
		int count = 0;
		int restp = T;
		int maxm[2] = { -1, -1 };

		//ふたり除く
		for( int i = 0; i < 2; i++ ) {
			for( int j = 0; j < T; j++ ) {
				if( maxm[i] < v[j] ) {
					maxm[i] = v[j];
					m[i] = j;
				}
			}
			if( m[i] >= 0 ) {
				v[m[i]] --;
				count ++;
			}
		}

		bool flg = true;
		if( count == 2 ) {
			for( int i = 0; i < T; i++ ) {
				flg &= ( (sum-2) >= 2*v[i] );
			}
		} else 
			flg = false;

		if( flg == false ) {
			for( int i = 0; i < 2; i++ ) {
				m[i] = -1;
				maxm[i] = -1;
			}
			count = 0;
			//ひとりのぞく
			v = p;
			for( int i = 0; i < T; i++ ) {
				if( maxm[0] < v[i] ) {
					maxm[0] = v[i];
					m[0] = i;
				}
			}
			count ++;
		}

		ofs << " ";
		for( int i = 0; i < count; i++ ) {
			p[m[i]]--;
			sum--;
			char ch = m[i]+'A';
			ofs << ch;
		}


	}



	ofs << endl;

	cnt ++;

}