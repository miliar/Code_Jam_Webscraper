#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <sstream>
#include <functional>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <list>
#include <numeric>
using namespace std;
const double PI = 3.14159265358979323846;
const double EPS = 1e-12;
const int INF = 1<<25;
typedef pair<int,int> P;
typedef long long ll;
typedef unsigned long long ull;


int main(){
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		int L;
		string s;
		cin>>L>>s;
		int sum = 0, res = 0;
		for(int i = 0; i <= L; i++){
			int num = s[i]-'0';
			if(sum < i){
				res += i-sum;
				sum = i;
			}
			sum += num;
		}
		printf("Case #%d: %d\n", Case, res);
	}
	return 0;
}

