#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
string s;
ll a[1005];
int main(){
  freopen("asd.txt","r",stdin);
   freopen("qw.txt","w",stdout);
ll n,t;
cin >> t;
ll j = 1;

while(t--){

    //cin >> n >> s;
  //  FILE *myfile,*t;

    cin >> n >> s;

    ll cnt = 0;
    ll cnt1=0;
    for(ll i=0; i<s.length(); i++){

        cnt += (s[i]-'0');
        if(i+1>cnt && s[i+1] != '0'){
            cnt1 += i+1-cnt;
            cnt += i+1-cnt;
        }
    }

    cout << "Case #";
    cout << j << ":";
    cout <<" " << cnt1 << "\n";

    j++;
  //  fclose(stdout);

}
    return 0;

}
