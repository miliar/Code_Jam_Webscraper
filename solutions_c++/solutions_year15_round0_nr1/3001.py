#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <fstream>
#include <queue>
#include <complex>

#define INF 1145141919
#define INF_INT_MAX 2147483647
#define INF_LL_MAX 9223372036854775807
#define EPS 1e-10
#define Pi acos(-1)
#define LL long long
#define ULL unsigned long long

using namespace std;

#define MAX_N 1005

string currentPass = "C:\\C\\pra\\Debug\\";

int main(){

	ifstream ifs(currentPass + "input.in");
	ofstream ofs(currentPass + "output.out");

	int T;
	ifs >> T;

	for (int testCase = 1; testCase <= T; testCase++){

		int N;
		char str[MAX_N];
		ifs >> N;
		for (int i = 0; i <= N; i++){
			ifs >> str[i];
		}

		int preCnt = 0;
		int ans = 0;

		for (int i = 0; i <= N; i++){

			if (str[i] == '0')
				continue;

			if (preCnt >= i){
				preCnt += str[i] - '0';
			}

			else{
				int tmpCnt = i - preCnt;
				ans += tmpCnt;
				preCnt += tmpCnt + str[i] - '0';
			}

		}

		ofs << "Case #" << testCase << ": " << ans;
		if (testCase <= T - 1)
			ofs << endl;

	}

	ifs.close();
	ofs.close();

	return 0;

}