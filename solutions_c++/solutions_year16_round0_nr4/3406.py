#include<bits/stdtr1c++.h>
using namespace std;
typedef long long LL;
int n;
int j;
vector<int> v;
int c;
LL MX;
LL MN;
typedef pair<LL,LL> pr;
set<pr> ans;
bool check(LL &a) {
  return (a && MN);
}
void solve(int ind, LL a, LL lst) {
  if((int)ans.size() >= j)
    return;
  if(a > MX)
    return;
  if( (a & MN)  == MN) {
    ans.insert(pr(a,lst));
  }
  if(ind == -1)
    return ;
  solve(ind-1,a*v[ind],v[ind]);
  solve(ind-1,a,lst);
}
string BI(LL a) {
  string ret ="";
  while(a) {
    ret += (a%2) +'0';
    a /=2;
  }
  reverse(ret.begin(),ret.end());
  return ret;
}
int main()
{
    #ifndef ONLINE_JUDGE
        freopen("2.in","r",stdin);
        freopen("2.out","w",stdout);
    #endif // ONLINE_JUDGE
    
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int T;
    cin>>T;
    LL k,c,s;
    for(int ic = 1;ic<=T;ic++) {
      cin>>k>>c>>s;
      cout<<"Case #"<<ic<<": ";
      unsigned long long last = 0;
      LL p = 1;
      for(int j=1;j<c;j++) p*=k;

      for(int i=0;i<k;i++){
        if(i) cout<<" ";
        cout<<last+1;
          last +=p;
      }
      cout<<endl;
    }
    return 0;
    
}
