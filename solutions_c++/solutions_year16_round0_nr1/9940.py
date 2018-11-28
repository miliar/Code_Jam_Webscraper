/*
 *
 */
#include<bits/stdc++.h>
using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef unsigned int uint;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
#define ft first
#define sd second
#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define ms0(X) memset((X), 0, sizeof((X)))
#define ms1(X) memset((X), -1, sizeof((X)))
#define len(X) strlen(X)
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define mrg(a, b) a##b
#define gt(a) #a
#define rep(i,n) for(i=0;i<n;i++)
const int MOD = 1e9+7;
const int SIZE = 1e6+10;

bitset<10> l;
int digits(int n){
  while(n){
    int i = n%10;
    l.set(i,0);
    n/=10;
  }
}

int solve(int n){
  l.set();
  int i=1,t;
  while(l.any()){
    t=i*n;
    digits(t);
    i++;
  }
  return t;
}

int main()
{
  int t,n;
  cin>>t;
  for(int i=1;i<=t;i++){
    cin>>n;
    if(n==0)
       cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
    else
      cout<<"Case #"<<i<<": "<<solve(n)<<endl;
  }
  return 0;
}
