#include<bits/stdc++.h>
 
using namespace std;
 
#define ll long long int
#define ull unsigned long long int
#define maxN 100005
#define logN 18
#define maxW 1005
#define MOD 1000000007
#define pb push_back
#define mp make_pair
#define INF (((ll)1000000000) * ((ll)1000000000))
#define e 2.7182818284590452353602874
#define maxT 100000

int main() {

cin.sync_with_stdio(0);
cin.tie(0);

int T;
cin>>T;

for(int tc=1;tc<=T;tc++) {

int N;
cin>>N;

int l=N+1;
string s;
cin>>s;

vector<int> V;
V.clear();
for(int i=0;i<s.size();i++)
 for(int j=0;j<s[i]-'0';j++)
  V.pb(i);

sort(V.begin(),V.end());

int req=0;
int cnt=0;

for(int i=0;i<V.size();i++)
if(V[i]>cnt) {
req+=V[i]-cnt;
cnt=V[i]+1;
}
else 
cnt++;
 
cout<<"Case #"<<tc<<": "<<req<<"\n";

}

return 0;
}
