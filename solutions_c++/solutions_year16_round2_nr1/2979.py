#include <iostream>
#include <sstream>
#include <string>
#include <math.h>
#include <string.h>
#include <bitset>
#include <functional>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <iostream>
#include <iomanip>
#define mp(a, b) make_pair(a, b)
typedef long long ll;
using namespace std;




int main(){
	int T;// Z () W () U () X () G ()
	//char suji[10][20] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
	char suji2[10][20] = { "ZERO", "WTO", "UFOR", "XSI", "GHEIT", "ONE", "THREE", "FIVE", "SEVEN", "INNE" };
	int out[10] = {0,5,1,6,2,7,3,8,4,9};
	vector<int> ret;
	cin >> T;
	for (int t = 0; t < T; t++){
		char in[3000];
		int tmpnum[50];
		memset(tmpnum, 0, sizeof(tmpnum));
		cin >> in;
		cerr << in;
		for (int i = 0; i < strlen(in); i++){
			tmpnum[in[i]-'A']++;
		}
		for (int i = 0; i < 27; i++){
			cerr << tmpnum[i];
		}
		int tmp[10] ;
		memset(tmp, 0, sizeof(tmp));

		for (int i = 0; i < 10; i ++){// 0 2 4 6 8 
			tmp[i] = tmpnum[suji2[i][0]-'A'];
			for (int j = 0; j <  strlen(suji2[i]); j++){
				tmpnum[suji2[i][j]-'A'] -= tmp[i];
			}
		}


		cout << "Case #" << t + 1 << ": ";
		for (int i = 0; i < 10; i++){
			for (int j = 0; j < tmp[out[i]]; j++){
				cout << i;
			}
			
		}
		cout << endl;
		cerr << endl;
		//cout << "Case #" << i + 1 << ": "<<maxct<<endl;
	}


	return 0;
}