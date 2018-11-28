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


int main() {
	freopen("A-large.in", "r", stdin);
	freopen("answer.out", "w", stdout);
	int T;
	cin>>T;
	for(int t = 1; t <= T; t++){
		int N,m[1000];
		cin>>N;
		for(int i = 0; i < N; i++)
			cin>>m[i];
		int res1=0,res2=0;
		int cr = 0;
		for(int i = 0; i < N-1; i++)
			if(m[i]>m[i+1])
				cr = max(cr, m[i] - m[i+1]);
		for(int i = 0; i < N-1; i++){
			if(m[i+1] < m[i])
				res1 += m[i] - m[i+1];
			res2 += min(cr,m[i]);
		}
		cout<<"Case #"<<t<<": "<<res1<<" "<<res2<<endl;
	}
	return 0;
}
