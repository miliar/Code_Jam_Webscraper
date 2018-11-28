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
#define fi first
#define se second

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

int main(){
	ll cases = rl();
	REP1(cc , cases){
    string s = rs();
    ll arr[26];
    ll length = s.length();
    REP(i,26)arr[i] = 0;
    for (ll i = 0; i < length; ++i){
      arr[s.at(i) - 65]++; 
    }
      // for (ll i = 0; i < 26; ++i){
      //   cout << arr[i] << endl; 
      // }
    string ans = "";
    ll count = arr[25];
    for (ll i = 0; i < count; ++i){   //Z for zero
      ans = ans + "0";
      arr[25]--;
      arr[4]--;
      arr[17]--;
      arr[14]--;
    }
    //cout << ans<<endl;
    count = arr[22];
    for (ll i = 0; i < count; ++i){   //W for two
      ans = ans + "2";
      arr[22]--;
      arr[19]--;
      arr[14]--;
    }
    //cout << ans<<endl;
    count = arr[23];
    for (ll i = 0; i < count; ++i){   //X for six
      ans = ans + "6";
      arr[23]--;
      arr[8]--;
      arr[18]--;
    }
    //cout << ans<<endl;
    count = arr[20];
    for (ll i = 0; i < count; ++i){   //u for four
      ans = ans + "4";
      arr[5]--;
      arr[14]--;
      arr[20]--;
      arr[17]--;
    }
    //cout << ans<<endl;
    count = arr[14];
    for (ll i = 0; i < count; ++i){   //o for one
      ans = ans + "1";
      arr[14]--;
      arr[13]--;
      arr[4]--;
    }
    //cout << ans<<endl;
    count = arr[5];
    for (ll i = 0; i < count; ++i){   //f for five
      ans = ans + "5";
      arr[5]--;
      arr[8]--;
      arr[21]--;
      arr[4]--;
    }
    //cout << ans<<endl;
    count = arr[21];
    for (ll i = 0; i < count; ++i){   //v for seven
      ans = ans + "7";
      arr[21]--;
      arr[4] = arr[4] - 2;
      arr[18]--;
      arr[13]--;
    }
    //cout << ans<<endl;
    count = arr[17];
    for (ll i = 0; i < count; ++i){   //r for three
      ans = ans + "3";
      arr[19]--;
      arr[4] = arr[4] - 2;
      arr[7]--;
      arr[17]--;
    }
    //cout << ans<<endl;
    count = arr[19];
    for (ll i = 0; i < count; ++i){   //t for eight
      ans = ans + "8";
      arr[8]--;
      arr[4]--;
      arr[6]--;
      arr[7]--;
      arr[19]--;
    }
    //cout << ans<<endl;
    count = arr[8];
    for (ll i = 0; i < count; ++i){   //i for nine
      ans = ans + "9";
      arr[8]--;
      arr[13] = arr[13] - 2;
      arr[4]--;
    }
    printf("Case #%lld: ", cc);
    sort(ans.begin(), ans.end());
    cout << ans<<endl;
	}
}
