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
#include <iterator>
#include <tuple>
#include <regex>
#include <array>
#include <valarray>
#include <fstream>
#define all(v)begin(v),end(v)
#define dump(v)copy(all(v),ostream_iterator<decltype(*begin(v))>(cout,"\n"))
#define rg(i,a,b)for(int i=a,i##e=b;i<i##e;++i)
#define fr(i,n)for(int i=0,i##e=n;i<i##e;++i)
#define rf(i,n)for(int i=n-1;i>=0;--i)
#define ei(a,m)for(auto&a:m)if(int a##i=&a-&*begin(m)+1)if(--a##i,1)
#define ec(i,m)for(int i=0,i##e=m.size();i<i##e;++i)
#define sz(v)int(v.size())
#define sr(v)sort(all(v))
#define rs(v)sort(all(v),greater<int>())
#define rev(v)reverse(all(v))
#define eb emplace_back
#define big numeric_limits<int>::max()
#define g(t,i)get<i>(t)
#define cb(v,w)copy(all(v),back_inserter(w))
#define uni(v)sort(all(v));v.erase(unique(all(v)),end(v))
#define vt(...)vector<tuple<__VA_ARGS__>>
#define smx(a,b)a=max(a,b)
#define smn(a,b)a=min(a,b)
typedef long long ll;
using namespace std;

int main() {
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int T;
	cin >> T;
	cout << fixed << setprecision(9);
	for (int i = 1; i <= T; ++i) {
		cout << "Case #" << i << ": ";
		double C, F, X, mnT = 1e30;
		cin >> C >> F >> X;
		double T = 0, S = 2;
		for (int j = 0; ; ++j) {
			if (T + X / S < mnT){
				mnT = T + X / S;
			} else {
				break;
			}
			T += C / S, S += F;
		}
		cout << mnT << endl;
	}
}