#include <iostream>
#include <string>
#define forn(i, n) for(int i = 0; i < int(n); i++)
using namespace std;
#define sz(s) (int)(s).size()
bool is_pal(long long a){
	string s = "";
	do{
		s.push_back(a%10 + '0');
		a/=10;
	}while(a > 0);
	forn(i, sz(s))
		if(s[i] != s[sz(s) - i - 1])
			return false;
	return true;
}
long long get_pal(long long a){
	string s = "";
	do{
		s.push_back(a%10 + '0');
		a/=10;
	}while(a > 0);
	int cnt = sz(s);
	forn(i, cnt)
		s.push_back(s[cnt-i-1]);
	long long res = 0;
	forn(i, sz(s))
		res = 10 * res + s[i]-'0';
	return res;
}
int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int tests;
	cin >> tests;
	forn(test, tests){
		printf("Case #%d: ", test + 1);
		long long A, B;
		cin >> A >> B;
		long long cnt = 0;
		for(int c = 0; c <= 9; c++){
			long long pal = c;
			long long mul = pal * pal;
			if(mul > B)
				break;
			if(is_pal(mul) && A <= mul && mul <= B) {
				cnt++;
				cerr <<  pal << " " << mul << endl;
			}
		
		}
		for(int c = 1; ; c++){
			long long pal = get_pal(c);
			long long mul = pal * pal;
			if(mul > B)
				break;
			if(is_pal(mul) && A <= mul && mul <= B) {
				cnt++;
				cerr <<  pal << " " << mul << endl;
			}
		}
		cout << cnt << endl;
	}
	return 0;
}