#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
#define ll long long
#define ld long double
#define vi vector<int>
#define pb push_back
#define pii pair<int,int>
#define mp make_pair
#define st first
#define nd second
#define mini(a,b) a=min(a,(b))
#define maxi(a,b) a=max(a,(b))
#define RE(i,n) for(int i=0,_n=(n);i<_n;++i)
#define RI(i,n) for(int i=1,_n=(n);i<=_n;++i)
const int inf=1e9+5, nax=1e6+5;

int licz[20];
int t[6][6];

int main()
{
	ios_base::sync_with_stdio(0);
	
	int z;
	cin >> z;
	RI(test, z) {
		RE(i, 20) licz[i] = 0;
		RE(_, 2) {
			int k;
			cin >> k;
			RI(row, 4) RI(col, 4) cin >> t[row][col];
			RI(col, 4) licz[ t[k][col] ]++;
		}
		int ile2 = 0;
		RE(i, 20) if(licz[i] == 2) ile2++;
		cout << "Case #" << test << ": ";
		if(ile2 == 0) cout << "Volunteer cheated!" << "\n";
		else if(ile2 > 1) cout << "Bad magician!" << "\n";
		else {
			int best = 0;
			RE(i, 20) if(licz[i] == 2) best = i;
			cout << best << "\n";
		}
	}
	return 0;
}
