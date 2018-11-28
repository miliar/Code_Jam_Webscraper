#include <bits/stdc++.h>
 
using namespace std;
 
#define INF 1000000007
#define MAX 100010
#define ROOT 100
#define BIG 1010
#define EPS 1e-6
const double pi = 2*acos(0) ;
 
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi; 
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef pair<ii,ii> pii;
 
#define set0(a) memset(a,0,sizeof(a));
#define setminus1(a) memset(a,-1,sizeof(a)); 
#define all(x) x.begin(), x.end()
#define tr(x,it) for(auto it = x.begin(); it!=x.end(); ++it)
#define rtr(x,it) for(auto it = x.rbegin(); it!=x.rend(); ++it)
#define sz(a) int((a).size()) 
#define pb push_back 
#define mp make_pair
#define F first
#define S second
#define FOR(i,a,b) for(int i = a; i<=b; ++i)
#define NFOR(i,a,b) for(int i = a; i>=b; --i)
#define fast ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)
int A[100];
int B[100];
void solve(){
  string s;
  cin>>s;
  set0(A);
  set0(B);
  int n=sz(s);
  FOR(i,0,n-1){
    A[s[i]-'A']++;
  }
  int temp;
  temp=A['z'-'a'];
  FOR(i,1,temp){
    B[0]++;
    A['z'-'a']--;
    A['e'-'a']--;
    A['r'-'a']--;
    A['o'-'a']--;
  }temp=A['w'-'a'];
  FOR(i,1,temp){
    B[2]++;
    A['w'-'a']--;
    A['t'-'a']--;
    A['o'-'a']--;
  }temp=A['g'-'a'];
  FOR(i,1,temp){
    A['g'-'a']--;
    B[8]++;
    A['e'-'a']--;
    A['i'-'a']--;
    A['h'-'a']--;
    A['t'-'a']--;
  }temp=A['h'-'a'];
  FOR(i,1,temp){
    A['h'-'a']--;
    B[3]++;
    A['t'-'a']--;
    A['r'-'a']--;
    A['e'-'a']-=2;
  }temp=A['u'-'a'];
  FOR(i,1,temp){
    A['u'-'a']--;
    B[4]++;
    A['f'-'a']--;
    A['o'-'a']--;
    A['r'-'a']-=2;
  }temp=A['f'-'a'];
  FOR(i,1,temp){
    A['f'-'a']--;
    B[5]++;
    A['i'-'a']--;
    A['v'-'a']--;
    A['e'-'a']--;
  }temp=A['x'-'a'];
  FOR(i,1,temp){
    A['x'-'a']--;
    B[6]++;
    A['s'-'a']--;
    A['i'-'a']--;
  }temp=A['v'-'a'];
  FOR(i,1,temp){
    A['v'-'a']--;
    B[7]++;
    A['s'-'a']--;
    A['e'-'a']-=2;
    A['n'-'a']--;
  }temp=A['i'-'a'];
  FOR(i,1,temp){
    A['i'-'a']--;
    B[9]++;
    A['n'-'a']-=2;
    A['e'-'a']--;
  }temp=A['o'-'a'];
  FOR(i,1,temp){
    A['o'-'a']--;
    B[1]++;
    A['n'-'a']-=2;
    A['e'-'a']--;
  }
  FOR(i,0,9){
    while(B[i]--){
      cout<<i;
    }
  }
  cout<<"\n";


}

int main(){
  clock_t tm=clock();
  fast;
  int t=1;
  cin>>t;
  FOR(_t,1,t){
  	cout<<"Case #"<<_t<<": ";
    solve();
  }	
  tm=clock()-tm;
  cerr<<(float)(tm)/CLOCKS_PER_SEC<<"\n";
  return 0;
} 