#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility> //Pair
#include <algorithm>
#include <sstream> 
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <functional>
#include <ctime>

using namespace std;
  
typedef long long ll;
typedef vector <int> vi;
typedef pair< int ,int > pii;

#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define sz size()
#define ln length()
#define rep(i,n) for(int i=0;i<n;i++)
#define all(a) a.begin(),a.end()
#define ESP (1e-4)
#define INF (1e9) 
#define fill(space,a) memset(space,a,sizeof(space))

int main(){
	//freopen("B-large.in","r",stdin);
	//freopen("outbl.txt","w",stdout);

	ios::sync_with_stdio(false);

	int t;cin >> t;
	int itr = 1;
	while(t--){
		string s;
		cin >> s;
		int ans = 0;
		
		for(int i=0;i<s.length()-1;i++) if(s[i] != s[i+1]) ans++;
//if(ans == 1 && s[0] == '+') ans++;
		if(ans == 0 && s[0] == '-') ans++;
		else if(ans >= 1 && s[s.length() - 1] == '-') ans++;
		cout << "Case #" << itr << ": " << ans << endl;
		itr++;
	}
	return 0;
}