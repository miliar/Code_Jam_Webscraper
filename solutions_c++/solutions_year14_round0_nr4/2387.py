#include "iostream"
#include "cstring"
#include "cstdio"
#include "cmath"
#include "algorithm"
#include "vector"
#include "set"
using namespace std;
const int N = 1010;
vector<double> a, b;
bool cmp(double x, double y)
{
	return x > y;
}
set<double> st;
int main(void)
{
	int T;
	freopen("D-large.in","r", stdin);
	freopen("D.out","w", stdout);
	int g = 0;
	scanf("%d", &T);
	int n;
	while(T --){
		printf("Case #%d: ",++ g);
		scanf("%d", &n);
		double x;
		a.clear();
		b.clear();
		for(int i = 0; i < n; ++ i){
			cin >> x;
			a.push_back(x);
		}
		for(int i = 0; i < n; ++ i){
			cin >> x;
			b.push_back(x);
		}
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		int ans0 = 0, ans1 = 0;
		int l = 0, r = n - 1;
		for(int i = 0; i < n; ++ i){
			double x = a[i];
			if(x > b[l]){
				ans0 ++;
				l ++;
			}else{
				r --;
			}
		}
		st.clear();
		for(int i = 0; i < n; ++ i){
			st.insert(b[i]);
		}
		for(int i = 0; i < n; ++ i){
			set<double>::iterator it;
			it = st.lower_bound(a[i]);
			if(it == st.end()){
				ans1 ++;
			}else{
				st.erase(it);
			}
		}
		printf("%d %d\n", ans0, ans1);
	}
	return 0;
}
