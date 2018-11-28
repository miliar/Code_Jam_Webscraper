#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define INF (1<<29)
#define EPS (1e-10)
#define make_pair mp
#define pb push_back
#define FOR(i,a,b) for(int i=a; i<b; i++ )

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef pair<int,int> pii;

int dx[] = {0,1,0,-1}, dy[] = {1,0,-1,0};

int main(){
	int T;
	cin >> T;
	FOR(t,1,T+1){
		int n;
		int ans = 0;
		cin >> n;
		vector<string> word;
		FOR(i,0,n){
			string w;
			cin >> w;
			word.pb(w);
		}
		bool flag = true;
		string ww = "";
		vii sum(100,vi(100,0));
		vi temp(100,0);
		for(int i=0; i<word.size(); i++ ){
			string nw = "";
			int k = 0;
			for(int j=0; j<word[i].size(); j++){
				if( j == 0 ){
					nw += word[i][j];
					sum[i][k]++;
					temp[k]++;
				}else if( word[i][j] != word[i][j-1] ){
					nw += word[i][j];
					k++;
					sum[i][k]++;
					temp[k]++;
				}else{
					sum[i][k]++;
					temp[k]++;
				}
			}
			//cout << nw << endl;
			if( i != 0 && ww != nw ){
				flag = false;
				break;
			}else ww = nw;
		}

		for(int i=0; i<word.size(); i++ ){
			for(int j=0; j<ww.size(); j++ ){
				//cout << sum[i][j] ;
				//cout << sum[i][j] - (temp[j]/word.size());
				if( (sum[i][j] > temp[j]/word.size()) ) ans += sum[i][j] - (temp[j]/word.size());
				else ans += temp[j]/word.size() - sum[i][j];
			}
			//cout << endl;
		}

		if( flag ) cout << "Case #" << t << ": " << ans << endl;
		else cout << "Case #" << t << ": " << "Fegla Won" << endl;
	}
}
