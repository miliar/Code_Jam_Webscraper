#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef pair<ii, int> iii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<int, int> mii;
typedef map<string, int> msi;

#define FOR(i, a, b) \
for (int i = int(a); i <= int(b); i++) // a to b, and variable i is local!
#define FORD(i, a, b) \
for (int i = int(a); i >= int(b); i--) // a to b, and variable i is local!
#define TRvi(c, it) \
for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) \
for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it) \
for (msi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmii(c, it) \
for (mii::iterator it = (c).begin(); it != (c).end(); it++)
#define INF 2000000000
#define MEMSET_INF 127
#define MEMSET_HALF_INF 63
#define zero(arr) memset((arr), 0, sizeof (arr))
#define init(arr) memset((arr), -1, sizeof (arr))
#define ff first
#define ss second
#define pb push_back
#define LSOne(S) (S & (-S))

bool bit[104];

int main()
{

	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	
	int n;
	string s;
	
	cin>>n;
	
	FOR(i, 1, n) {
		cin>>s;
		FOR(j, 0, s.length()-1) {
			if(s[j]=='+')
				bit[j] = 1;
			else
				bit[j] = 0;
		}
		
		int cnt = 0;
		
		while(1) {
			int sum = 0;
			if(bit[0]) {
				int mark = -1;
				FOR(j, 1, s.length()-1) {	
					if(!bit[j]) {
						mark = j-1;
						break;
					}
				}
				if(mark != -1) {
					cnt++;
					FOR(j, 0, mark) {
						bit[j] = 0;
					}
				}
				else
					break;
			}
			else {
				
				int mark = -1;
				FORD(j, s.length()-1, 0){
					if(bit[j] == 0) {
						mark = j;
						break;
					}
				}
				cnt++;
				FOR(j, 0, mark) {
					bit[j] ^= 1;
				}
			}
			
		}
		
		cout<<"Case #"<<i<<": "<<cnt<<endl;
	}
 return 0;
}



