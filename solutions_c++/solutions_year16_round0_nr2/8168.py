#include <bits/stdc++.h>
using namespace std;

int main(){

	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	int ans2= 0,ans1= 0;
	scanf("%d", &t);
	while(t--){
		string s;
		cin >> s;
		ans1= 0,ans2= 0;
		int i= 0;
		while(s[i] == '-'){
			i++;
			ans1= 1;
		}
		for(;i < s.length();i++){
			if(s[i] == '-' && s[i - 1] != '-')
				ans1+= 2;
		}
		reverse(s.begin(),s.end());
		ans2= 1;
		i= 0;
		while(s[i] == '+'){
			i++;
			ans2= 1;
		}
		for(;i < s.length();i++){
			if(s[i] == '+' && s[i - 1] != '+')
				ans2+= 2;
		}
		static int x =1;
		printf("Case #%d: %d\n", x++, min (ans1, ans2));
	}

	return 0;
}
