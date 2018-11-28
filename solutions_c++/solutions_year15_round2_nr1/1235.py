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
using namespace std;
template <typename T>
string _numtostr(T n)
{
    ostringstream ss;
    ss << n;
    return ss.str();
}
template <typename T>
T _strtonum(const string& str)
{
    T res;
    istringstream ss(str);
    return ss >> res ? res : 0;
}
int ar[1000010];
int main() {
	//freopen("in.txt","r", stdin);
	//freopen("out.txt","w", stdout);
	for(int i = 1; i <= 1000000; i++) ar[i] = 1000010;
	for(int i = 1; i <= 1000000; i++)
	{
		ar[i] = min(ar[i], ar[i-1] + 1);
		string s = _numtostr<int>(i);
		reverse(s.begin(), s.end());
		int a = _strtonum<int>(s);
		if(a <= 1000000) ar[a] = min(ar[a], ar[i] + 1);
	}
	int t;
	scanf("%d", &t);
	int c = 1;
	while(t--)
	{
		int n;
		scanf("%d", &n);
		printf("Case #%d: %d\n", c, ar[n]);
		c++;
	}
	return 0;
}

