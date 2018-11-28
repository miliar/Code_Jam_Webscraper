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

string flip(string s){

  string r="";
  for(int i=0; i<s.length(); i++){
    if(s[i]=='0')
      r= "1" + r;
    else
      r = "0" + r;
  }
  return r;
}

int shortest_bfs(string s, string f){
  map< string, int>D;
  queue<string>Q;
  D[s]=0;
  Q.push(s);
  while(!Q.empty()){
    string curr = Q.front();
    Q.pop();

    int clen = D[curr];
    if(curr.compare(f)==0)
      return D[curr];

    string i;
    for(int j=1;j<=s.length();j++){
      if(j!=s.length()){
      string pile = curr.substr(0,j);
      i = flip(pile) + curr.substr(j);
    }
    else{
      i = flip(curr);
    }
      if(!present(D,i)){
        D[i] = clen+1;
        Q.push(i);
      }
    }
  }
  return -1;
}

int main()
{
  int t;
  string s;
  cin>>t;
  for(int i=1;i<=t;i++){
    cin>>s;

    string r="",e="";
    for(int j = 0;j<s.length();j++){
      if(s[j]=='+')
        r=r+"1";
      else
        r=r+"0";
      e=e+"1";
    }
    cout<<"Case #"<<i<<": "<<shortest_bfs(r,e) <<endl;
  }
  return 0;
}
