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
	
	//freopen("D-small-attempt0.in","r",stdin);
	//freopen("input_a.txt","r",stdin);
//	freopen("outds.txt","w",stdout);

	int t;cin >> t;
	int itr = 1;
	while(t--){
		int k,c,s;cin >> k >> c >> s;
		cout << "Case #" << itr << ": " ;
		for(int i=1;i<=k;i++) cout << i << ' ';
		cout << endl;
		itr++;
	}
	return 0;
}