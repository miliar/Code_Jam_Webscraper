#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
typedef vector<string> vs;
#define st          first
#define se          second
#define all(x)      (x).begin(), (x).end()
#define ini(a, v)   memset(a, v, sizeof(a))
#define re(i,s,n)  	for(int i=s;i<(n);++i)
#define fr(i,n)     re(i,0,n)
#define tr(i,x)     for(typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define pu          push_back
#define mp          make_pair
#define sz(x)       (int)(x.size())

int main(){
int t;
cin >> t;
for(int test=1;test <= t;test++){
     long int A,B,K;
     cin >> A >> B >> K;
     long cnt = 0;
     for(long int i=0;i<A;i++){
          for(long int j=0;j<B;j++){
               long int kk = i & j;
               if(kk < K ) cnt++;
          }
     }
     cout << "Case #" << test << ": " << cnt <<endl;
}
return 0;
}
