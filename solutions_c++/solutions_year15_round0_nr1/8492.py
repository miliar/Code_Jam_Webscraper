#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <sstream>
#include <fstream>
#include <queue>
#include <math.h>
#include <set>

#define For(i,a,b) for(int i=(a);i<(b);++i)
#define rep(i,n)  For(i,0,n)

//clear memory
#define CLR(a) memset((a), 0 ,sizeof(a))
#define check(a) rep(i, a.size()) cout << a[i] << endl
#define SORT(c) sort((c).begin(),(c).end())
using namespace std;

int main(int argc, char* argv[]){
	int n;
	cin >> n;
	rep(i, n){
		int t;
		string str;
		cin >> t >> str;
		int result = 0;
		int goukei = 0;
		rep(k, str.length()){
			if (str[k] != 0 && goukei >= k){
				goukei += (str[k] - '0');
			}
			else if (goukei < k){
				result += (k - goukei);
				goukei = goukei + (k - goukei) + (str[k] - '0');
			}
		}
		cout << "Case #" << i + 1 << ": " << result << endl;
	}
	return 0;
}