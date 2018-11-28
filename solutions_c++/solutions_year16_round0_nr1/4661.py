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
		ll a;
		cin>>a;
		cout<<"Case #"<<Case<<": ";
		if(a==0){
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		set<int> st;
		ll b = 0;
		while(st.size()<10){
			b += a;
			ll c = b;
			while(c){
				st.insert(c%10);
				c /= 10;
			}
		}
		cout<<b<<endl;
	}
	return 0;
}

