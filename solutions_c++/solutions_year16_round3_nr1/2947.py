/*
* @Author: onkar
* @Date:   2016-05-08 14:23:03
* @Last Modified by:   onkar
* @Last Modified time: 2016-05-08 15:28:55
*/
#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define REP(i, n) FOR(i, 0, n)
#define BACK(i, n) ROF(i, 0, n)
#define FOR(i, a, b) for (ll i = (a); i < (b); i++)
#define ROF(i, a, b) for (ll i = (b); --i >= (a); )
#define REP1(i, n) FOR(i, 1, n+1)
typedef pair<int, int> pii;
typedef pair<string, int> psi;

double rd(){
  double x;
  scanf("%lf", &x);
  return x;
}

ll rl(){
  ll x;
  scanf("%lld", &x);
  return x;
}

string rs(){
 	string x;
  cin >> x;
  return x;
}

int compare (const void *a , const void *b){   //decreasing order  
  return ( *(ll*)b - *(ll*)a );
}

bool sortFunc( const vector<ll>& p1,
               const vector<ll>& p2 ) {
 return p1[0] > p2[0];
}

char a(ll x){

}

int main(){
	ll cases = rl();
	REP1(cc , cases){
		ll n = rl();
		bool hash = false;
		// ll arr[n];
		// ll sum = 0, maxi = 0;
		// REP(i,n){
		// 	arr[i] = rl();
		// 	sum += arr[i];
		// 	maxi = max(maxi,arr[i])
		// }
		ll temp1, temp2 = 'A';
    	vector< vector<ll> > vec;
	    REP(i,n){
      		vector < ll > tmpvec;
    	  	temp1 = rl();
      		tmpvec.push_back(temp1);
      		tmpvec.push_back(temp2);
      		temp2++;
      		vec.push_back(tmpvec);
    	}
    	// for (ll i = 0; i < vec.size(); ++i){
    	// 	cout << vec[i][0] << " "<< vec[i][1]<<"\t";
    	// }
    	printf("Case #%lld: ", cc);
    	while(vec.size() != 0){
    		sort(vec.begin(), vec.end(), sortFunc);
    		// for (ll i = 0; i < vec.size(); ++i){
    		// 	cout << vec[i][0] << " "<< vec[i][1]<<"\t";
    		// }
    		if(vec.size() == 3 && vec[0][0] == 1){
    			cout << (char)vec[0][1] << " ";
    			vec.erase(vec.begin());
    		}
    		else{
    			hash = false;
    			cout << (char)vec[0][1]<<(char)vec[1][1] << " ";
    			vec[0][0]--;
    			vec[1][0]--;
    			if(vec[0][0] == 0){
    				break;
    			}
    			if(vec[1][0] == 0)
    				vec.erase(vec.begin() + 1);
    		}
    	}
    	cout << endl;
	}
}
	 