//------------------------------------------------------------------------------
//  Problem : 
//  User    : 
//  Date    : 
//------------------------------------------------------------------------------


#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

bool check(int a, int r, int c) {
	if(r > c) {
		swap(r, c);
	}
	if(r*c%a != 0) {
		return false;
	}
	switch(a) {
		case 1:
			return true;
		case 2:
			return (r>=1)&&(c>=2);
		case 3:
			return (r>=2)&&(c>=3);
		case 4:
			return (r>=3)&&(c>=4);
		case 5:
			return (r>=3)&&(c>=5);
		case 6:
			return (r>=4)&&(c>=6);
	}
	return false;
}

void solu(int x) {
	printf("Case #%d: GABRIEL\n", x);
}

void nosl(int x) {
	printf("Case #%d: RICHARD\n", x);
}

void work(int x) {
	int a, r, c;
	scanf("%d%d%d", &a, &r, &c);
	if(check(a, r, c)) {
		solu(x);
	} else {
		nosl(x);
	}
}

int main( int argc , char *argv[] )
{
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i) {
		work(i);
	}
	return 0;
}
