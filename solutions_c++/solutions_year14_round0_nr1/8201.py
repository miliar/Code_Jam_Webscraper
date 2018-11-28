
#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;


typedef pair<int, int> ii;
#define REP(i, a, b)  for (int i = int(a); i <= int(b); i++) 


int main(){
	
	int test_count;
	cin >> test_count;
	
	REP( test_index , 1 , test_count )
	{
		int  choice_1;
		cin >> choice_1;
		
		int row1[4];
		
		
		REP( i , 0 , 3 )
		{
			REP( j , 0 , 3 )
			{
				if ( i == choice_1-1){
					cin >> row1[j];
				}
				else{
					int garbage;
					cin >> garbage;
				}			
			}
		}
		
		
		int  choice_2;
		cin >> choice_2;
		
		int row2[4];
		
		
		REP( i , 0 , 3 )
		{
			REP( j , 0 , 3 )
			{
				if ( i == choice_2-1){
					cin >> row2[j];
				}
				else{
					int garbage;
					cin >> garbage;
				}			
			}
		}
		//cout << row1[0]<< " " << row1[1] << " " << row1[2] << " " << row1[3]<<"  ";
		//cout << row2[0]<< " " << row2[1] << " " << row2[2] << " " << row2[3]<<"  ";

		std::sort( row1 , row1 + 4 );
		std::sort( row2 , row2 + 4 );
		
		//cout << row1[0]<< " " << row1[1] << " " << row1[2] << " " << row1[3]<<"  ";
		//cout << row2[0]<< " " << row2[1] << " " << row2[2] << " " << row2[3]<<"  ";
		int interestion[4];
		
		int count = ( std::set_intersection (row1, row1+4, row2, row2+4, interestion) - interestion ) ;

			
		cout <<"Case #" << test_index<<": ";
		
		if( count == 0 ){
		     cout << "Volunteer cheated!";
		}
		else if (count == 1  )
		{
		     cout << interestion[0];
		}
		else
		{
		     cout << "Bad magician!";
		}			
		cout <<"\n";
	}
	
	
	return 0;
}