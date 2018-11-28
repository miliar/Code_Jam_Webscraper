#include <iostream>
#include <fstream>

using namespace std;

ifstream fin( "A1.in" );
ofstream fout( "A1.out" );
#define cin fin
#define cout fout

int G[2], arr[2][4][4];
int T;

int main()
{
	cin >> T;
	for( int tt = 1; tt <= T; tt++ ){
		
		for( int i = 0; i < 2; i++ ){
			cin >> G[i];
			G[i]--;
			for( int j = 0; j < 4; j++ )
				for( int k = 0; k < 4; k++ )
					cin >> arr[i][j][k];
		}
		cout << "Case #" << tt << ": ";
		int cnt = 0, any = 0;
		for( int c1 = 0; c1 < 4; c1++ )
			for( int c2 = 0; c2 < 4; c2++ ){
				if( arr[0][G[0]][c1] == arr[1][G[1]][c2] ){
					cnt++;
					any = arr[0][G[0]][c1];
				}
			}
		if( cnt == 1 )
			cout << any << endl;
		else if( cnt == 0 )
			cout << "Volunteer cheated!" << endl;
		else cout << "Bad magician!" << endl;
		
	}

	return 0;
}