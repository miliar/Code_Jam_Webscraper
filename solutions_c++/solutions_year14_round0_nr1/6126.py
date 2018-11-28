#include <iostream>
#include <fstream>

using namespace std;

int A[5][5];
int B[5][5];
int a , b;


int Magic () {

	bool flg[17];
	for ( int i = 0 ; i < 17 ; i++ ) 
		flg[i] = false;

	a--;
	for ( int i = 0 ; i < 4 ; i++ ) 
		flg[A[a][i]]=true;
	
	int count = 0; 
	int ans;
	b--;
	for ( int i = 0 ; i < 4 ; i++ )
		if ( flg[B[b][i]]  )  {
			count++;
			ans=B[b][i];
		}

	if ( count == 1 ) return ans;
	if ( count > 1 ) return -1;
	//if ( count == 0 ) return 0;
	return 0;
		
}
void Readata() {

	int T;
	cin >> T;
	for ( int i = 0 ; i < T ; i++ ) {
	
		cin >> a;
		for ( int j = 0 ; j < 4 ; j++ ) 
			for ( int k = 0 ; k < 4 ; k++ ) 
				cin >> A[j][k];
		cin >> b;
		for ( int j = 0 ; j < 4 ; j++ ) 
			for ( int k = 0 ; k < 4; k++ )
				cin >> B[j][k];

		int ans = Magic();
		if ( ans > 0 ) cout << "Case #" << i+1 << ": " << ans << endl;
		if ( ans == 0 ) cout <<"Case #" << i+1 << ": " <<"Volunteer cheated!" << endl;
		if ( ans < 0 ) cout <<"Case #" << i+1 << ": " << "Bad magician!" << endl;
	}
}
int main()
{
	Readata();
	return 0;
}
