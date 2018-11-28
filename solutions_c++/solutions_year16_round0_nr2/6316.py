#include<cstring>
#include<iostream>
#include<bitset>
#include<cstdlib>
#include<set>
#include<map>
#include<vector>
#include<string>
#include<queue>
#include<stack>
#include<cstdio>
#include<cmath>
#include<utility>
#include<algorithm>
#include<iomanip>
#define BUFF ios::sync_with_stdio(false);
#define mp make_pair
#define pb push_back
#define imprime(v) for(int X=0;X<v.size();X++) cout<<v[X]<<" "; cout<<endl;
#define grid(v) for(int X=0;X<v.size();X++){for(int Y=0;Y<v[X].size();Y++) cout<<v[X][Y]<<" "; cout<<endl;}
#define endl "\n"
using namespace std;
const int INF= 0x3f3f3f3f;
const long double pi= acos(-1);
typedef long long int ll;
typedef long double ld;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector< vector< int > > vii;
const int MOD=1e9+7;
set<int> dig;
void pega_digito(ll x){
  while(x!=0){
    int last=x%10;
    dig.insert(last);
    x/=10;
  }
}
int main()
{
  BUFF;
  int t;
  cin>>t;
  int cu=t;
  while(t--){
    ll n;
    dig.clear();
    cin>>n;
    ll i=0;
    while(dig.size()<10 and n!=0){
      i++;
      ll number=i*n;
      pega_digito(number);
    }
    ll resp=i*n;
    if(resp!=0)
    cout<<"Case #"<<cu-t<<": "<<resp<<endl;
    else cout<<"Case #"<<cu-t<<": INSOMNIA"<<endl;
  }
  return 0;
}
