#include<iostream>
#include<fstream>
#include<string>
using namespace std;
#define LL long long
LL ans[20];
LL get(string s){
	LL r = ans[s.length()];
	LL k = 1;
	int rot = 0;
	if(s.length() > 1 && s[0] - '0' > 1)
		rot = 1;
	for(int i = 0; 2 * i < s.length(); i++){
		if(i && i < s.length() / 2 && s[i] - '0' > 0)
			rot = 1;
		r += (s[i] - '0') * k;
		int j = s.length() - 1 - i;
		if(j != i)
			r += (s[j] - '0') * k;
		k *= 10ll;
	}
	r--;
	r += rot;
	return r;
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	ans[1] = 1;
	string x = "1";
	for(int i = 2; i <= 15; i++){
		ans[i] = get(x) + 9ll;
		x = "9" + x;
	}
	int n;
	cin >> n;
	for(int i = 0; i < n; i++){
		string s;
		LL x;
		cin >> x;
		LL ans = 0;
		if((x % 10) == 0){
			x--;
			ans = 1;
		}
		while(x){
			s = (char)((x % 10) + '0') + s;
			x /= 10;
		}
		ans += get(s);
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
	return 0;
}
			