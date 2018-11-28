#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
template <class T> inline string itos(T n) {return (n)<0?"-"+itos(-(n)):(n)<10?(string)("")+(char)('0'+(n)):itos((n)/10)+itos((n)%10);}

int case_number;
#define printg printf("Case #%d: ",case_number+1), printf
#define gout printf("Case #%d: ",case_number+1), cout


//////////////////////////////////////////////////////////////////////////////////////////////

void main2(void){

	// Logic 
	int ans1, ans2, i;
	std::vector<int> row1(4), row2(4), dummy(4);
	
	cin >> ans1;
	REP(i, 4)
	{
		if( i == (ans1-1) )
			cin >> row1[0] >> row1[1] >> row1[2] >> row1[3];
		else
			cin >> dummy[0] >> dummy[1] >> dummy[2] >> dummy[3];
	}

	cin >> ans2;
	REP(i, 4)
	{
		if( i == (ans2-1) )
			cin >> row2[0] >> row2[1] >> row2[2] >> row2[3];
		else
			cin >> dummy[0] >> dummy[1] >> dummy[2] >> dummy[3];
	}

	int card_match=0;
	int card_no = -1;
	REP( i, 4)
	{
		std::vector<int>::iterator it =
			std::find( row1.begin(), row1.end(), row2[i]);

		if( it != row1.end() )
		{
			card_no = *it;
			card_match++;
			row1.erase( it );
		}
		if( card_match > 1 )
			break;
	}

	// Answer print 
	if( card_match == 0 ) gout << "Volunteer cheated!" << endl;
	if( card_match == 1 ) gout << card_no << endl;
	if( card_match > 1 ) gout << "Bad magician!" << endl;
}

int main(void){
	int number_of_test_cases;
	cin >> number_of_test_cases;
	
	REP( case_number, number_of_test_cases) 
		main2();

	return 0;
}
