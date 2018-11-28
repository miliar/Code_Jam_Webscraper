#define DEBUG

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <stdarg.h>
#include <climits>

using namespace std;

typedef unsigned int uint;
typedef unsigned long long uint64;
#define SIZE(A) ((int)A.size())
#define LENGTH(A) ((int)A.length())
#define MP(A,B) make_pair(A,B)
#define POW2(X) (((uint)1)<<(X))
typedef vector<int> VI;
typedef pair<int,int> ipair;

int main(){
	int T,N;
	cin >> T;
	int t = 0;
	while(t < T){
		t++;
		long result = 0;
		long sum = 0;
		cin >> N;
		string s;
		cin >> s;
		for(int i = 0; i < s.size(); i ++){
			int num = s[i] - '0';
			if(num == 0)	continue;
			if(i == 0){
				sum += num;
				continue;
			}
			if(sum < i){
				result += i - sum;
				sum = i + num;
			}else{
				sum += num;
			}
		}
		cout << "Case #"<< t <<": " << result << endl;
	}
}


