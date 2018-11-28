#include <bits/stdc++.h>

#define x first
#define y second

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef pair<ll,ll> pll;

int N,R,P,S,T;
//bool dp[20][4097][4097][3];

string sol[13][3]; //numpeop,winner
int ct[13][3][3]; //numpeop,winner,what count is of

int subs[3][2]{ {0,1}, {1,2}, {0,2} };

int main() {
	cin >> T;
	sol[0][0]="P";
	sol[0][1]="R";
	sol[0][2]="S";
	for (int i=0;i<3;i++) for (int j=0;j<3;j++) ct[0][i][j]=(i==j);

	for (int l=1;l<=12;l++) for (int w=0;w<3;w++) {
		for (int j=0;j<3;j++) ct[l][w][j]=ct[l-1][subs[w][0]][j]+ct[l-1][subs[w][1]][j];
		string s1=sol[l-1][subs[w][0]],s2=sol[l-1][subs[w][1]];
		if (s1>s2) swap(s1,s2);
		s1.append(s2);
		sol[l][w]=s1;
	}

	for (int cas=1;cas<=T;cas++) {
		cin >> N >> R >> P >> S;
		int rcts[3]{P,R,S};
		bool fs=0;
		string bs;
		for (int w=0;w<3;w++) {
			bool succ=1;
			int ln=N;
			/*while (N%2==0) {
				ln++;
				N/=2;
			}*/
			for (int i=0;i<3;i++) if (ct[ln][w][i]!=rcts[i]) succ=0;
			if (succ) {
				string cs=sol[ln][w];
				if (fs) {
					if (cs<bs) bs=cs;
				}
				else {
					fs=1;
					bs=cs;
				}
			}
		}

		printf("Case #%d: ",cas);
		if (fs) cout << bs << endl;
		else cout << "IMPOSSIBLE\n";
	}
}
