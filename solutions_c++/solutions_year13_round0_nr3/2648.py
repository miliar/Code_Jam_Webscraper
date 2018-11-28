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
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
__int64 ten[20];
vector<__int64> data;

__int64 geta(__int64 s)
{	
	int digit[100];
	int n = 0;
	__int64 t = s;
	while(s > 0) {
		digit[n++] = s % 10;
		s /= 10;
	}
	if(digit[0] == 0) return -1;

	__int64 ans = t;
	for (int i = 0;i < n;++i) {
		ans += digit[i] * ten[2 * n - i - 1];
	}
	return ans;
}
__int64 getb(__int64 s)
{
	int digit[100];
	int n = 0;
	__int64 t = s;
	while(s > 0) {
		digit[n++] = s % 10;
		s /= 10;
	}
	if(digit[0] == 0) return -1;

	__int64 ans = t;
	for (int i = 0;i < n - 1;++i) {
		ans += digit[i] * ten[2 * n - i - 2];
	}
	return ans;
}
bool isp(__int64 s) 
{
	int digit[100];
	int n = 0;
	__int64 t = s;
	while(s > 0) {
		digit[n++] = s % 10;
		s /= 10;
	}
	for (int i = 0;i < n;++i) {
		if(digit[i] == digit[n - i - 1]) continue;
		return false;
	}
	return true;
}
bool iss(__int64 a)
{
	__int64 b = floor(sqrt((double)a));

	if(b * b == a) {
		if(isp(b)) {
			return true;
		} else {
			return false;
		}
	}
	return false;
}
void init()
{
	ten[0] = 1;
	for (int i = 1;i < 17;++i) {
		ten[i] = ten[i - 1] * 10;
	}
	for(__int64 i = 1;i <= 1e7;++i ) {
		__int64 a = geta(i);
		__int64 b = getb(i);

		if(iss(a)) {
			data.push_back(a);
		} 
		if(iss(b)){
			data.push_back(b);
		}
	}
	sort(data.begin(), data.end());
	//for(int i = 0;i < data.size();++i) {
	//	cout<<data[i]<<endl;
	//}
}
int count(__int64 a) 
{
	for (int i = 0;i < data.size();++i) {
		if(data[i] > a)return i - 1;
	}
	return data.size();
}
void solve()
{
	__int64 A, B;
	cin>>A>>B;
	cout<<count(B) - count(A - 1)<<endl;
}
int main()
{
	//freopen("data.txt", "r", stdin);

	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);
	init();
	int n;
	scanf("%d", &n);
	for (int i = 1;i <= n;++i) {
		cout<<"Case #"<<i<<": ";
		solve();
	}
	return 0;
}