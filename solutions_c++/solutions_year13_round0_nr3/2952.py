#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
#include <bitset>
#include <climits>
#include <stack>
#include <cctype>
#include <sstream>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;

int lessThan(int x) {
    if(x <= 1)  return 0;
    else if(x <= 4) return 1;
    else if(x <= 9) return 2;
    else if(x <= 121) return 3;
    else if(x <= 484) return 4;
    else return 5;
}

int lessThanEqualTo(int x) {
    if(x < 1)  return 0;
    else if(x < 4) return 1;
    else if(x < 9) return 2;
    else if(x < 121) return 3;
    else if(x < 484) return 4;
    else return 5;
}

int main()	{
    int T, A, B, i;

	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small.txt", "w", stdout);

	scanf("%d", &T);
	for(i=1; i<=T; i++) {
        scanf("%d %d", &A, &B);
        printf("Case #%d: %d\n", i, lessThanEqualTo(B) - lessThan(A));
	}

	return 0;
}
