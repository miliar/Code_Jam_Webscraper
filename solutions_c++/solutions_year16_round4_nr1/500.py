#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <string>
#include <cstring>
#include <cmath>
using namespace std;
string str[3][15];
int main(){
	str[0][0] = "R";
	str[1][0] = "S";
	str[2][0] = "P";
	for(int i = 1;i<=12;i++)
		for(int j=0;j<3;j++){
		int len = 1 << (i-1);
		int u, v;
		if(j==0) u = 0, v = 1;
		if(j==1) u = 1, v = 2;
		if(j==2) u = 0, v = 2;
		str[j][i] = min(str[u][i-1] + str[v][i-1], str[v][i-1] + str[u][i-1]);
	}
	int t;
	cin >> t;
	for(int ca = 1; ca <=t ; ca++){
		int n, r,s,p;
		cin >> n >> r >> p >> s;
		string ans = "";
		for(int i=0;i<3;i++){
			int cr=0,cs=0,cp=0;
			for(int j=0;j<(1<<n);j++){
				if(str[i][n][j] == 'R') cr++;
				if(str[i][n][j] == 'P') cp++;
				if(str[i][n][j] == 'S') cs++;
			}
			if(cr == r && cp == p && cs == s){
				if(ans == "" || ans > str[i][n])
					ans = str[i][n];
			}
		}
		if(ans == "") ans = "IMPOSSIBLE";
		printf("Case #%d: ", ca);
		cout << ans << endl;
	}
}