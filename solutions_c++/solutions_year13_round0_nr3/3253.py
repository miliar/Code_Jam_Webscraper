#include <iostream>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <iterator>
using namespace std;

#define PW2(n) (n)*(n)
#define RPT(var, n) for(int var = 0; var < (n); var++)
#define RVT(var, n) for(int var = (n - 1); var >= 0; var--)
#define PRN(var) cout << #var << "=" << (var) << endl
#define vint vector<int>

#define MAX 11000

int lst[1000];

bool r(int n){
	int t[10];
	int s = -1;
	
	for(int i = 0; n > 0; i++){
		t[i] = n%10;
		n /= 10;
		s++;
	}
	
	int a = 0;
	
	while(a < s){
		if(t[a] != t[s]){
			return false;
		}
		a++;
		s--;
	}
	return true;
}

int main(){
	int T, A, B, m = 0;
	cin >> T;
	
	for(int i = 1; PW2(i) <= MAX; i++){
		if(r(i) && r(PW2(i))){
			lst[m] = PW2(i);
			m++;
		}
	}
	
	RPT(cnt, T){
		cin >> A >> B;
		
		int rslt = 0;
		for(int i = 0; lst[i] <= B; i++){
			if(lst[i] >= A){
				rslt++;
			}
		}
		cout << "Case #" << cnt+1 << ": " << rslt << endl;
	}
} 
