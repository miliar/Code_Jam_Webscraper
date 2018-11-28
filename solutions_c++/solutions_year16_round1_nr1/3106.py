#include <cstdio>
#include <iostream>
using namespace std;

int T;
string in, ans;

int main(){
	scanf("%d", &T);
	for(int tt = 1; tt <= T; tt++){
		cin >> in;
		
		ans = "";
		ans += in[0];
		for(int i = 1; i < in.length(); i++){
			if(in[i] >= ans[0])ans = in[i] + ans;
			else ans += in[i];
		}

		cout << "Case #" << tt << ": " << ans << endl;
	}
}