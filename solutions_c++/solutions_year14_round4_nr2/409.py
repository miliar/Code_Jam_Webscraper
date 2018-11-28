#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;
int test;
int arr[2000], pos[2005];
int temp[2000];
bool mark[2000];
int n;
ifstream fin( "B2.in" );
ofstream fout( "B2.out" );
#define cin fin
#define cout fout



int main()
{
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		int res = 0;
		cin >> n;
		for( int i = 0; i < n; i++ ){
			cin >> arr[i];
			temp[i] = arr[i];
		}
		sort( temp, temp + n );
		for( int i = 0; i < n; i++ )
			for( int j = 0; j < n; j++ )
				if( arr[i] == temp[j] ){
					arr[i] = j;
					pos[j] = i;
					break;
				}
		int left = 0, right = n - 1;
		for( int i = 0; i < n; i++ ){
			int d1 = abs( pos[i] - left );
			int d2 = abs( pos[i] - right );
			//res += min( d1, d2 );
			//cout << i << ' ' << pos[i] << ' ' << d1 << ' ' << d2 << ' ' << left << ' ' << right << ' ' << res << endl;
			if( d1 < d2 ){
				//cout << "DSSDA " << left << ' ' << pos[i] << endl;
				while( pos[i] != left ){
					pos[arr[pos[i] - 1]]++;
					swap( arr[pos[i]], arr[pos[i] - 1] );
					res++;
					
					pos[i]--;
				}
				left++;
			}
			else{
				
				while( pos[i] != right ){
					//cout << "DSDS " << right << ' ' << pos[i] << endl;	
					pos[arr[pos[i] + 1]]--;
					swap( arr[pos[i]], arr[pos[i] + 1] );
					res++;
					pos[i]++;
				}
				right--;
			}
		}
		cout << "Case #" << T << ": " << res << endl;
	}

	return 0;
}