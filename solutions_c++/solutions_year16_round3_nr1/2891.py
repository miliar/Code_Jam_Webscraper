#include <bits/stdc++.h>
 
using namespace std;
 
#define INF 1000000007
#define MAX 1000010
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
int P[30];
void solve(){
	 int n;
   int sum=0;
   cin>>n;
   FOR(i,0,n-1){cin>>P[i];sum+=P[i];}
   while(sum!=0){
      FOR(i,0,n-1){
        FOR(j,i,n-1){
          if(!sum)break;
          P[i]--;
          P[j]--;
          if(P[i]<0&&P[j]<0&&i!=j){
            P[i]++;
            P[j]++;
            continue;
          }
          if(P[i]<0){
            sum--;
            int maxi=0;
            FOR(k,0,n-1)maxi=max(maxi,P[k]);
            if(maxi>(sum)/2){
              P[i]++;
              P[j]++;
              sum++;continue;
            }
            else{
              P[i]++;
              cout<<(char)(j+'A')<<" ";
              continue;
            }
          }
          if(P[j]<0&&i!=j){
              sum--;
            int maxi=0;
            FOR(k,0,n-1)maxi=max(maxi,P[k]);
            if(maxi>(sum)/2){
              P[i]++;
              P[j]++;
              sum++;continue;
            }
            else{
              P[j]++;
              cout<<(char)(i+'A')<<" ";continue;
            }
          }
          sum-=2;
          int maxi=0;
          FOR(k,0,n-1)maxi=max(maxi,P[k]);
          if(maxi>(sum)/2){
            P[i]++;
            P[j]++;
            sum+=2;continue;
          }
          else{
            cout<<(char)(i+'A')<<(char)(j+'A')<<" ";
          }
        }
      }
   }
    cout<<"\n";
    //cout<<P[0]<<" "<<P[1]<<" "<<P[2]<<"\n";
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
