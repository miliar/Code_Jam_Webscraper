# include <iostream>
# include <math.h>
# include <stdio.h>
# include <string.h>
# include <algorithm>
# include <vector>
# include <fstream>
# include <limits.h>

using namespace std;

//ifstream INPUT_FORMAT ("");
ofstream fout ("file.out");

int T,q1,vis[100],a;

int main(){
	
	cin >> T;
	for ( int i=0; i<T; i++ ){
		cin >> q1;
		for ( int j=0; j<4; j++ ){
			for ( int h=0; h<4; h++ ){
				cin >> a;
				if( q1-1 == j )
					vis[a]++;
			}
		}
		
		cin >> q1;
		for ( int j=0; j<4; j++ ){
			for ( int h=0; h<4; h++ ){
				cin >> a;
				if( q1-1 == j )
					vis[a]++;
			}
		}
		
		int ans=0,indx=0;
		for ( int j=1; j<=16; j++ )
			if( vis[j] == 2 )
				ans++,indx=j;
		
		if( ans == 1 )	fout << "Case #" << i+1 << ": " << indx << endl;
		else if( ans > 1 )	fout << "Case #" << i+1 << ": " << "Bad magician!\n";
		else fout << "Case #" << i+1 << ": " << "Volunteer cheated!\n";
		
		for ( int j=1; j<=16; j++ )	vis[j]=0;
	}
	
	return 0;
}
