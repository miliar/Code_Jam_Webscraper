#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#define maxn 1010
#define maxm 1010
using namespace std; 

char ch[] = "PRS";


int f[3][13][3];
string str[3][13];

void init(){
	for(int i = 0; i < 3; ++i){
		for(int j = 0; j < 3; ++j) f[i][0][j] = 0;
		f[i][0][i] = 1;
		str[i][0] = ch[i];
	}
	for(int i = 1; i < 13; ++i)
		for(int j = 0; j < 3; ++j) {
			for(int k = 0; k < 3; ++k) f[j][i][k] = f[j][i-1][k] + f[(j+1)%3][i-1][k];
			str[j][i] = min(str[j][i-1]+str[(j+1)%3][i-1], str[(j+1)%3][i-1]+str[j][i-1]);
		}
}

void solve()
{
	int result[3];
	int n;
	cin >> n;
	cin >> result[1] >> result[0] >> result[2];
	string best = "";
	for(int w = 0; w < 3; ++w){
		bool match = true;
		for(int i = 0; i < 3; ++i) if (f[w][n][i] != result[i]) match = false;
		if(match && (best == "" || str[w][n] < best)) best = str[w][n];
	}
	if (best == "") best = "IMPOSSIBLE";
	cout << best << endl;
}

int main() 
{
	init();
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i){
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
