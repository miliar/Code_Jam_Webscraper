#include <cstdio>
#include <iostream>
#include <string>
using namespace std;
FILE *fi = freopen("A-large.in", "r", stdin);
FILE *fo = freopen("ALout.txt", "w", stdout);

string str, ans;

int test, lev;

int main(){
	scanf("%d", &test);
	while (test--){
		++lev;
		cin >> str;
		ans.clear();
		ans.push_back(str[0]);
		for (int i = 1; i < str.size(); i++){
			if (ans.front() <= str[i])ans = str[i] + ans;
			else ans.push_back(str[i]);
		}
		printf("Case #%d: ", lev); cout << ans << endl;
	}
}