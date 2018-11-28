//C++ Template

#include <bits/stdc++.h>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;
typedef map<int,int>::iterator ITmii;

#define EPS 1e-9
#define FOR1(x,y,z) for(int x = y; x < z ; ++x)
#define FOR(x,y) FOR1(x,0,y)
#define FOR2(x,y) for(int x = y; x >= 0; --x)
#define PB push_back
#define ALL(X) (X).begin(), (X).end()
#define SORT(X) sort(ALL(X))
#define SIZE(X) ((int)(X).size())

//------------------------------------------------------------------

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.txt","w",stdout);
	int a;
	cin >> a;
	FOR(i,a){
		string s;
		cin >> s;
		vector<int> v(26,0);
		vector<int> ans(10,0);
		FOR(j,SIZE(s)){
			++v[s[j]-'A'];
		}
		while(v[25] != 0){ //0
			++ans[0];
			--v[25]; //z
			--v[4]; //e
			--v[17]; //r
			--v[14]; //o
		}
		while(v[6] != 0){ //8
			++ans[8];
			--v[4]; //e
			--v[8]; //i
			--v[6]; //g
			--v[7]; //h
			--v[19];//t
		}
		while(v[7] != 0){ //3
			++ans[3];
			--v[19];
			--v[7];
			--v[17];
			--v[4]; --v[4];
		}
		while(v[23] != 0){ //6
			++ans[6];
			--v[18]; //s
			--v[8]; //i
			--v[23]; //x
		}
		while(v[22] != 0){ //2
			++ans[2];
			--v[19];//t
			--v[22];//w
			--v[14];//o
		}
		while(v[18] != 0){ //7
			++ans[7];
			--v[18];//s
			--v[4];//e
			--v[21];//v
			--v[4];//e
			--v[13];//n
		}
		while(v[21] != 0){ //5
			++ans[5];
			--v[5];//f
			--v[8];//i
			--v[21];//v
			--v[4];//e
		}
		while (v[5] != 0){ //4
			++ans[4];
			--v[5];//f
			--v[14];//o
			--v[20];//u
			--v[17];//r
		}
		while(v[8] != 0){ //9
			++ans[9];
			--v[13]; --v[13];
			--v[8];
			--v[4];
		}
		ans[1] += v[14];
		cout << "Case #" << i+1 <<": ";
		FOR(j,10){
			FOR(k,ans[j]){
				cout << j;
			}
		}
		cout << '\n';
		}
}
