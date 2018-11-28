#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fore(i,n) for(int i = 0; i< n ; i++ )
#define lop(i,n) for(int i = 1 ; i<=n ; i++ )
#define ops(i,n) for(int  i = n-1 ; i>=0 ; i-- )
#define	forall( it,g )	for( typeof(g.begin()) it=g.begin();it!=g.end();it++ )
#define PI  3.141592653589793
#define mod  1000000007
#define inf 1000000000000
#define INF -1000000000
#define modulo 1073741824
#define MH 1234533333333337
//ios_base::sync_with_stdio(0);cin.tie(0); cout.tie(0);
using namespace std;
typedef vector <int > vi;
typedef vector <vector <int> > vv;
typedef vector <pair <int,int > >vp;
typedef vector <vector <pair <int ,int > > > vvp;
typedef vector <pair <int ,pair <int ,int > > > vpp;
typedef pair<int,int> pp;
typedef long long ll;
pp pre[10010],suf[10010];
pp comput(int cur,char s,int neg){
    if(s == 'i' && cur == 1)cur = 0 ,neg*=-1;
    else if(s == 'j' && cur == 2)cur = 0,neg*=-1;
    else if(s == 'k' && cur == 3)cur = 0,neg*=-1;
    else if(s == 'j' && cur == 1)cur = 3 ;
    else if(s == 'k' && cur == 2)cur = 1 ;
    else if(s == 'i' && cur == 3)cur = 2 ;
    else if(s == 'i' && cur == 2)cur = 3 ,neg*=-1;
    else if(s == 'j' && cur == 3)cur = 1 ,neg*=-1;
    else if(s == 'k' && cur == 1)cur = 2 ,neg*=-1;
    else if(cur == 0 && s == 'i')cur = 1;
    else if(cur == 0 && s == 'j')cur = 2;
    else if(cur == 0 && s == 'k')cur = 3;
    return mp(cur,neg);
}
int main()
{
  ios_base::sync_with_stdio(0);cin.tie(0); cout.tie(0);
  freopen("out.txt","w",stdout);
  freopen("C-small-attempt7.in","r",stdin);
  int test,g = 0;
  cin >> test ;
  while(test--){
    g++;
    string s,str;
    int l,x;
    cin >> l >> x;
    cin >> s ;
    str = s;
    fore(i , x-1)
      s+=str;

    int cur = 0 , neg = 1;
    fore(i , s.size()){
      pp a = comput(cur,s[i],neg);
      pre[i] = (mp(a.first,a.second));
      cur = a.first , neg = a.second;
    }

    cur = 0 , neg = 1;
    ops(i , s.size()){
      pp a = comput(cur,s[i],neg);
      suf[i] = (mp(a.first,a.second));
      cur = a.first , neg = a.second;
    }

    bool done = false;
    fore(i , x*l){
      if(pre[i].first == 1 && pre[i].second == 1 && suf[i+1].first == 1){
        cur = 0 , neg = 1;
        bool flag = false,diff = false;
        for(int j = i+1 ;j<x*l ;j++){
          if(j!=x*l-1 && s[j]!=s[j+1])
            diff = true;
          pp a = comput(cur,s[j],neg);
          cur = a.first , neg = a.second;
          if(cur == 2 && neg == 1)
            flag = true;
        }
        if(diff && flag && neg == 1){
          done = true;
          break;
        }
      }
      if(done)break;
    }
    if(done)cout << "Case #" << g <<": YES"<<endl;
    else cout << "Case #" << g <<": NO"<<endl;
    fill_n(pre,10001,mp(-1,0)),fill_n(suf,10001,mp(-1,0));
    s.clear(),str.clear();
  }
  return 0;
}
/*
1
2 6
ji
*/
