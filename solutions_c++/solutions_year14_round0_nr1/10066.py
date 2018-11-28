#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
#define all(x) x.begin() , x.end()


#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
int TestCases  , First , Second ,FirstGrid[4][4] , SecondGrid[4][4] , tmp ;
int main()
{
READ("A-small-attempt4.in");
WRITE("A-Smallout.out");

cin>>TestCases ;

for(int x=1;x<=TestCases;x++){
	cin>>First ;

	for(int i =0 ;i<4 ;i++)
		for(int j =0 ;j<4;j++)
			cin>>FirstGrid[i][j];

	cin>>Second ;

	for(int i =0 ;i<4 ;i++)
			for(int j =0 ;j<4;j++)
				cin>>SecondGrid[i][j];

	int c = 0 ;

	for(int i =0 ;i<4;i++)
		for(int j =0 ;j<4;j++)
		if(FirstGrid[First-1][i] == SecondGrid[Second-1][j])
			c++ , tmp = FirstGrid[First-1][i];

	cout<<"Case #"<<x<<": ";

	if(c>1)
		cout<<"Bad magician!"<<endl;
	else if (c == 0 )
		cout<<"Volunteer cheated!"<<endl;
		else cout<<tmp<<endl;

}
return 0;
}
