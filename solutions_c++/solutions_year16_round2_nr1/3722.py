#include <bits/stdc++.h>

using namespace std ;
typedef long long ll;

int main() {
	
	freopen("in.txt","r",stdin) ;
	freopen("out.txt","w",stdout) ;
	
	int t ;
	cin >> t ;
	
	for( int k = 1 ; k <= t ; k++ ) {
				
		cout << "Case #" << k << ": " ;
		string str ;
		cin >> str ;
		
		int arr[ 30 ] ;
		for( int i = 0 ; i < 30 ; i++ ) arr[i] = 0 ;
		
		int i = 0 ; 
		while( str[i] ) {
			arr[ str[i] -65 ]++ ;
			i++ ;
		}
		
	//	cout << str << endl ;
		
		string ans ;
		int counter , uniCounter = 0 ;
		
		while( 1 ) {
			
			//cout << endl << ans << endl ;
			//for( int i = 0 ; i < 30 ; i++ ) cout << " (" << (char)(i+65) << " , " << arr[i] << ")  " ;
			
			if( uniCounter > 300000 ) {
				for( int i = 0 ; i < 30 ; i++ ) arr[i] = 0 ;
		
				int i = 0 ; 
				while( str[i] ) {
					arr[ str[i] -65 ]++ ;
					i++ ;
				}
				ans.clear() ;
				uniCounter = 0 ;
			}
			
			counter = 0 ;
			for( int i = 0 ; i < 30 ; i++ ) if( arr[i] ) counter++ ;
			if( !counter ) break ;
			
		int num = rand()%10 ;
		uniCounter++ ;
		
		//cout << num << endl ;
		char ch = num+48 ;
		//cout << " char : " << ch << endl ;
		switch( ch ) {
			
			
			case '7' :
			
				//cout << " inside case : " << ch << endl ;
				if( arr['S'-65] ) {
				if( arr['E'-65] ) {
					if( arr['V'-65] ) {
						if( arr['E'-65] > 1 ) {
							if( arr['N'-65] ) {
								arr[ 'S'-65 ]-- ;
								arr[ 'E'-65 ]-- ;
								arr[ 'V'-65 ]-- ;
								arr[ 'E'-65 ]-- ;
								arr[ 'N'-65 ]-- ;
								ans.push_back('7') ;
								continue ;
							}
						}
					}
				}
			} 			
			break ;
			
			case '3' : 
			if( arr['T'-65] ) {
				if( arr['H'-65] ) {
					if( arr['R'-65] ) {
						if( arr['E'-65] ) {
							if( arr['E'-65] > 1 ) {
								arr[ 'T'-65 ]-- ;
								arr[ 'H'-65 ]-- ;
								arr[ 'R'-65 ]-- ;
								arr[ 'E'-65 ]-- ;
								arr[ 'E'-65 ]-- ;
								ans.push_back('3') ;
								continue ;
							}
						}
					}
				}
			}
			break ;
			
			case '0' :
			if( arr['Z'-65] ) {
				if( arr['E'-65] ) {
					if( arr['R'-65] ) {
						if( arr['O'-65] ) {
							arr[ 'Z'-65 ]-- ;
							arr[ 'E'-65 ]-- ;
							arr[ 'R'-65 ]-- ;
							arr[ 'O'-65 ]-- ;
							ans.push_back('0') ;
							continue ;
						}
					}
				}
			}
			break ;
			
			case '4' : 
			if( arr['F'-65] ) {
				if( arr['O'-65] ) {
					if( arr['U'-65] ) {
						if( arr['R'-65] ) {
							arr[ 'F'-65 ]-- ;
							arr[ 'O'-65 ]-- ;
							arr[ 'U'-65 ]-- ;
							arr[ 'R'-65 ]-- ;
							ans.push_back('4') ;
							continue ;
						}
					}
				}
			}
			break ;
			
			case '5' :
			if( arr['F'-65] ) {
				if( arr['I'-65] ) {
					if( arr['V'-65] ) {
						if( arr['E'-65] ) {
							arr[ 'F'-65 ]-- ;
							arr[ 'I'-65 ]-- ;
							arr[ 'V'-65 ]-- ;
							arr[ 'E'-65 ]-- ;
							ans.push_back('5') ;
							continue ;
						}
					}
				}
			}
			break ;
			
			case '8' :
			if( arr['E'-65] ) {
				if( arr['I'-65] ) {
					if( arr['G'-65] ) {
						if( arr['H'-65] ) {
							if( arr['T'-65] ) {
								arr[ 'E'-65 ]-- ;
								arr[ 'I'-65 ]-- ;
								arr[ 'G'-65 ]-- ;
								arr[ 'H'-65 ]-- ;
								arr[ 'T'-65 ]-- ;
								ans.push_back('8') ;
								continue ;
							}
						}
					}
				}
			}
			break ;
			
			case '9' :
			if( arr['N'-65] ) {
				if( arr['I'-65] ) {
					if( arr['N'-65] > 1 ) {
						if( arr['E'-65] ) {
							arr[ 'N'-65 ]-- ;
							arr[ 'I'-65 ]-- ;
							arr[ 'N'-65 ]-- ;
							arr[ 'E'-65 ]-- ;
							ans.push_back('9') ;
							continue ;
						}
					}
				}
			} 
			break ;
			
			case '1' : 
			if( arr['O'-65] ) {
				if( arr['N'-65] ) {
					if( arr['E'-65] ) {
						arr[ 'O'-65 ]-- ;
						arr[ 'N'-65 ]-- ;
						arr[ 'E'-65 ]-- ;
						ans.push_back('1') ;
						continue ;
					}
				}
			} 
			break ;
			
			case '2' :
			if( arr['T'-65] ) {
				if( arr['W'-65] ) {
					if( arr['O'-65] ) {
						arr[ 'T'-65 ]-- ;
						arr[ 'W'-65 ]-- ;
						arr[ 'O'-65 ]-- ;
						ans.push_back('2') ;
						continue ;
					}
				}
			} 
			break ; 
			
			case '6' :
			if( arr['S'-65] ) {
				if( arr['I'-65] ) {
					if( arr['X'-65] ) {
						arr[ 'S'-65 ]-- ;
						arr[ 'I'-65 ]-- ;
						arr[ 'X'-65 ]-- ;
						ans.push_back('6') ;
						continue ;
					}
				}
			}
			break ;
			
			
			
			
			
		}
			
			
		}
		
		sort(ans.begin(),ans.end()) ;
		cout << ans << endl ;
	}
	
	return 0 ;
}
