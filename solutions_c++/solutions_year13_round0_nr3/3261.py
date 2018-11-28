#include <cstdio>
#include <iostream>
#include <cstring>
#include <sstream>
#include <string>
#include <cmath>
using namespace std;

#define MAXN 1000
int ans[MAXN + 1];

bool ispalindromes(int n){
	bool flag = false;
	ostringstream oss;
	oss << n;
	string str = oss.str();
	for(int i = 0; i < str.size() / 2; i++){
		if(str[i] != str[str.size() - i - 1])
			return false;
	}
	return true;
}

void ini(){
	memset(ans, 0, sizeof(ans));
	for(int i = 1; i <= sqrt(MAXN)+1; i++){
		if(ispalindromes(i) && ispalindromes(i*i))
			ans[i*i]++;
	}
	/*for(int i = 1; i < 100; i++){
        cout << i << ": " << ans[i] << endl;
    }*/

	for(int i = 2; i <= MAXN; i++)
		ans[i] += ans[i-1];
}

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	ini();
	for(int cases = 1; cases <= t; cases++){
        cout << "Case #" << cases << ": ";

        int st,end;
        cin >> st >> end;
        cout << ans[end] - ans[st-1];

        cout << endl;
	}
	return 0;
}
