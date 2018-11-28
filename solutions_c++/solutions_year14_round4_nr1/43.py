/*
 * in the name of god
 *
 *
 *
 *
 *
 *
 *
 *
 */

#include <iostream> 
#include <fstream> 
#include <sstream> 
#include <cstdio> 
#include <cstring> 
#include <cstdlib> 
#include <cmath> 
#include <ctime> 
#include <algorithm> 
#include <vector> 
#include <queue> 
#include <deque> 
#include <stack> 
#include <set> 
#include <map> 
#include <complex> 
#include <bitset> 
#include <iomanip> 
#include <utility> 

using namespace std;

int a[1<<20],cnt[1000];

void main2(){
	int n; cin >> n;
	int X; cin >> X;
	for (int i=0; i<n; i++)
		cin >> a[i];
	sort(a, a+n);
	reverse(a, a+n);
	queue <int> Q;
	int ans = 0;
	memset(cnt, 0, sizeof cnt);
	for (int i=0; i<n; i++){
		bool flag = false;
		for (int j=X-a[i]; j>=a[i]; j--){
			if (cnt[j]){
				cnt[j]--;
				flag = true;
				break;
			}
		}
		if (!flag){
			cnt[a[i]]++;
			ans++;
		}
	}
	cout << ans << endl;
}

int main(){
	int testCase; cin >> testCase;
	for (int o=1; o<=testCase; o++){
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
