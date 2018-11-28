#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <string>
#include <algorithm>
#include <functional>
#include <math.h>
#include <iomanip>
#include <time.h>
#include <utility>


using namespace std;

typedef long long int lli;
typedef pair <int, int> pii;
typedef pair <long long int, long long int> pll;

//global
lli slen;
string s;
lli ans;

void GetAll(){
	cin >> slen;
	cin >> s;
	ans = 0;
}

void Run(){
	lli now = 0;
	for (int i = 0; i < slen + 1; i++){
		if (s[i] == '0'){
			continue;
		}
		if (now >= i){
			now += s[i] - '0';
		}
		else{
			lli buf = i - now;
			ans += buf;
			now += buf;
			now += s[i] - '0';
		}
	}
	cout << ans;
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int n = 0;
	cin >> n;
	for (int i = 0; i < n; i++){
		cout << "Case #" << i + 1 << ": ";
		GetAll();
		Run();
		cout << "\n";
	}

	return 0;
}