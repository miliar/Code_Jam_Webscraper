#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cctype>
#include <climits>
#include <string>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define INF	(int)1e9
#define EPS 1e-9

int main(){
	int casenum;
	cin >> casenum;

	for(int i = 0; i < casenum; i++){
		double c, f, x, ans, curr;
		cin >> c >> f >> x;

		ans = x / 2;
		int j = 1;
		while(true){
			curr = 0;
			for(int k = 0; k < j; k++){
				curr += c/(2+k*f);
			}
			curr += x/(2+j*f);
			if(curr <= ans){
				ans = curr;
				j++;
			} else{
				break;
			}
		}

		printf("Case #%d: %.7f\n", i+1, ans);
	}
}