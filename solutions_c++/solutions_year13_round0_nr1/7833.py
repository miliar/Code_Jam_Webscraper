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
char b[4][4];
int temp = 0;
char solve() {

	for(int i = 0; i < 4; i ++){
		if(((b[i][0] == b[i][1] || b[i][1] == 'T' || b[i][0] == 'T') &&( b[i][0] != '.' && b[i][1] != '.')) && ((b[i][0] == b[i][2] || b[i][2] == 'T'  )&& b[i][2] != '.') && ((b[i][0] == b[i][3] || b[i][3] == 'T' ) && b[i][3] != '.' ))
		{
			if(b[i][0] == 'T')
				return b[i][1];
			else
				return b[i][0];
		}
		if(((b[0][i] == b[1][i] || b[1][i] == 'T' || b[0][i] == 'T') && (b[0][i] != '.' && b[1][i] != '.') ) && ((b[1][i] == b[2][i] || b[2][i] == 'T' )&& b[2][i] != '.' ) && ((b[2][i] == b[3][i] || b[3][i] == 'T') && b[3][i] != '.'))
		{
			if(b[0][i] == 'T')
				return b[1][1];
			else
				return b[0][i];
		}
	}
	int count = 0,count2= 0;
	for(int i = 0; i < 3; i ++){
		if(b[i][i] == b[i + 1][i + 1] || b[i][i] == 'T')
			count ++;
	}
	if(count == 3){
		if(b[0][0] == 'T')
			return b[1][1];
		else
			return b[0][0];
	}
	if(((b[0][3] == b[1][2] || b[0][3] == 'T' || b[1][2] == 'T') && b[0][3] != '.') && ((b[0][3] == b[2][1] || b[2][1] == 'T') && b[2][1] != '.') && ((b[0][3] == b[3][0] || b[3][0] == 'T') && b[3][0] != '.') ){
		if(b[0][3] == 'T')
			return b[1][2];
		else
			return b[0][3];
	}
	for (int j = 0; j < 4; j++)
		for (int k = 0; k < 4; k++)
			if(b[j][k] == '.')
				return '.';
	return 'N';	

}
int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	cin >> test;
	for (int i = 0; i < test; i++)
	{
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				cin >> b[j][k];
		cout << "Case #" << i + 1 <<": ";
		char s = solve();
		if(s == 'X')
			cout << "X won"<<endl;
		else if(s == 'O')
			cout << "O won" <<endl;
		else if(s == 'N')
			cout << "Draw" <<endl;
		else if(s == '.')
			cout << "Game has not completed" <<endl;
	}
}