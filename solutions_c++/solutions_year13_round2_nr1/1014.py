#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <fstream>
#include <memory.h>
using namespace std;

long long arr[105], N;

long long rec(long long A, int idx){
	if(idx == N) return 0;
	if(A > arr[idx])
		return rec(A+arr[idx], idx+1);
	long long ret =  N - idx;
	if(A > 1)
		ret = min(ret, rec(A+A-1,idx)+1);
	return ret;
}

int main(){

	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int T, A, c = 0;
	cin >> T;

	while(T--){
		cin >> A >> N;
		for(int i=0; i<N; i++)
			cin >> arr[i];
		sort(arr,arr+N);
		cout << "Case #" <<++c << ": " << rec(A,0) << endl;
	}

}

