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

int n;
int f[1<<20],g[1<<20],a[1<<20];

void main2(){
	cin >> n;
	for (int i=0; i<n; i++)
		cin >> a[i];
	int ans = 0;
	while(n){
		int pos = 0;
		for (int j=1; j<n; j++) if (a[j]<a[pos])
			pos = j;
		if (pos<=n-1-pos){
			while (pos>0){
				swap(a[pos], a[pos-1]);
				pos--, ans++;
			}
			for (int j=1; j<n; j++)
				a[j-1] = a[j];
		}else{
			while (pos<n-1){
				swap(a[pos], a[pos+1]);
				pos++, ans++;
			}
		}
		n--;
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
