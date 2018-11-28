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
#include <ctime>
#define ll long long int 
using namespace std;
int main() {
	//freopen("in.txt","r", stdin);
	//freopen("out.txt","w", stdout);
	int t;
	int c2 = 1;
	scanf("%d", &t);
	while(t--)
	{
		int r, c, w;
		scanf("%d %d %d", &r, &c, &w);
		int res = 0;
		for(int i = 1; i < r; i++) res += c / w;
		if(c % w == 0) res += c / w + w - 1;
		else res += c / w + w;
		printf("Case #%d: %d\n", c2, res);
		c2++;
	}
	return 0;
}
