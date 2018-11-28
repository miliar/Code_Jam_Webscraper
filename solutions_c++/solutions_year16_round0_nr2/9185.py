#include <string>
#include <cstring>
#include <iostream>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<queue>
using namespace std;
typedef long long ll;
int T;
string s;
char rev(char c){
	if (c == '+'){
		return '-';
	}
	else{
		return '+';
	}
}

void solve(string s, int t){
	char pre = s[0];
	int res = 0;
	int pos = 1;
	int f = 0;
	while (pos < s.size()){
		if (s[pos] != pre){
			res++;
			f++;
		}
		pre = s[pos];
		pos++;
	}
	char c;
	if (f % 2 == 0){
		c = s[0];
	}
	else{
		c = rev(s[0]);
	}
	if (c != '+'){
		res++;
	}
	printf("Case #%d: %d\n", t, res);
}

int main(){
	freopen("B.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		cin >> s;
		solve(s, i);
	}
}