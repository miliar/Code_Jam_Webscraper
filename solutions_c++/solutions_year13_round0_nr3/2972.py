#include <iostream>
#include <cstdio>
#include <sstream>
using namespace std;
typedef long long ll;
bool h[10000];
stringstream ss;
string str;

bool pali(ll x){
	ss.clear(); ss << x; ss >> str;
	int l = str.length();
	for(int i = 0; i <= l/2; i++){
		if(str[i] != str[l-1-i]) return false;
	}
	return true;
}


void init(){
	for(ll i = 1; i <= 100; i++)
		if(pali(i) && pali(i * i)) h[i * i] = true; 
}

int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int T; cin >> T;
	
	init();
	
	for(int cas = 1; cas <= T; cas++){
		int a, b;
		cin >> a >> b;
		cout << "Case #" << cas << ": ";
		int cnt = 0; 
		for(int i = a; i <= b; i++){
			if(h[i]) cnt++;
		}
		cout << cnt << endl;
	}
	
	fclose(stdin);
	fclose(stdout);
	return 0;
}