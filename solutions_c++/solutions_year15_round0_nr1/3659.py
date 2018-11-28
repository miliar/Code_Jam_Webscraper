#include <iostream>
#include <vector>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long long ll;

int t,smax;
string s;
vi shy;

int main(){
	cin >> t;
	for(int cass = 1; cass <= t; ++cass){
		cin >> smax >> s;
		shy = vi(smax+1);
		for(int i = 0; i <= smax; ++i) shy[i] = int(s[i]-'0');
		int cont = 0;
		int res = 0;
		for(int i = 0; i <= smax; ++i){
			if(cont < i){
				++cont;
				++res;
			}
			cont += shy[i];
		}
		cout << "Case #" << cass << ": " << res << endl;
	}
}
