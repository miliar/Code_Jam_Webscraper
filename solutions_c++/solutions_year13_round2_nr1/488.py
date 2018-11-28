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

int d[128];

int main(){
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		int A,N;
		cin>>A>>N;
		for(int i = 0; i < N; i++) cin>>d[i];

		sort(d,d+N);

		int ans = N,C = 0;
		for(int i = 0; i < N && C < ans; i++){
			if(A>d[i]){
				A += d[i];
				continue;
			}
			ans = min(ans,N-i+C);
			while(A<=d[i] && C < ans){
				A = A*2-1;
				C++;
			}
			A += d[i];
		}
		ans = min(ans,C);
		
		printf("Case #%d: %d\n",Case,ans);

	}
	return 0;
}
