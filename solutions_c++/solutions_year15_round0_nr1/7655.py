#include <bits/stdc++.h>

using namespace std;

#define sz(x) ((int) (x).size())
#define all(v) (v).begin( ), (v).end( )
double pi = 3.1415926536;
const int oo = (int) 1e9;
const long long OO = numeric_limits<long long>::max();

int dx[] = { 0, 1, 0, -1 };
int dy[] = { 1, 0, -1, 0 };

int di[] = { 0, 0, 1, -1, 1, -1, 1, -1 };
int dj[] = { 1, -1, 0, 0, 1, -1, -1, 1 };

int f1[] = { 0, 0, 0, 1, 1, 1, -1, -1, -1 };
int f2[] = { -1, 0, 1, -1, 0, 1, -1, 0, 1 };

int main(){
	ios_base::sync_with_stdio(false);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t , testCases = 1;
	cin >> t;

	while(t--){
		int sMax;
		string str;
		cin >> sMax >> str;
		int cnt = 0 , people = 0;

		people += str[0] - '0';

		for(int i = 1 ; i < sz(str) ; i++){
			if(people < i){
				cnt += i - people;
				people += i - people;
			}
			people += str[i] - '0';
		}


		cout << "Case #" << testCases++ << ": " << cnt << endl;
	}

}
