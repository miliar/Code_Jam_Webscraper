#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
typedef vector<string> vs;

#define st          first
#define se          second
#define all(x)      (x).begin(), (x).end()
#define ini(a, v)   memset(a, v, sizeof(a))
#define re(i,s,n)  	for(int i=s;i<(n);++i)
#define fr(i,n)     re(i,0,n)
#define tr(i,x)     for(typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define pu          push_back
#define mp          make_pair
#define sz(x)       (int)(x.size())
int row1[5][5];
int row2[5][5];
int main() {
	int t,x,y;
	cin >> t;
	for(int test=1; test<=t; test++) {
		cin >> x;
		for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) {
				cin >> row1[i][j];
			}
		}
		cin >> y;
		for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) {
				cin >> row2[i][j];
			}
		}
		int cnt =0;
		int ans =0;
		for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) {
				if(row1[x-1][i] == row2[y-1][j]) {
					cnt++;
					ans = row1[x-1][i];
				}
			}
		}
		cout << "Case #"<< test <<": ";
		if(cnt==0) cout << "Volunteer cheated!";
		else if(cnt==1) cout << ans;
		else cout << "Bad magician!";
		cout << endl;
	}
	return 0;
}
