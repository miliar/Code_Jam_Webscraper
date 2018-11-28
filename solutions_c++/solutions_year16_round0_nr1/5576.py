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

bool mark[10];
	
bool check(){
	for(int i=0;i<10;i++) {
		if(!mark[i]) return true;
	}
	return false;
}

int main(){
	
	//freopen("A-large.in","r",stdin);
	//freopen("outal.txt","w",stdout);
	ios::sync_with_stdio(false);
	
	int t,itr=1;
	cin >> t;
	
	while(t--){
		ll n;cin >> n;
		if(n == 0) {
			cout << "Case #" << itr << ": " << "INSOMNIA" << endl;
			itr++;
		}
		else{
			fill(mark,false);
			ll curr = 0;

			while(check()){
				curr = curr + n;
				ll temp  = curr;
				while(temp != 0){
					mark[temp % 10] = true;
					temp = temp / 10;
				}
			}
			cout << "Case #" << itr << ": " <<curr<< endl;
			itr++;
		}
		
	}
	
	return 0;
}