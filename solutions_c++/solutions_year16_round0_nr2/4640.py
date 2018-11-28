#include<bits/stdtr1c++.h>
using namespace std;
typedef long long LL;

int solve(LL a, vector<int> &vis) {
  while(a) {
    int c = a%10;
    vis[c] = 1;
    a /= 10;
  }
  int ret =0;
  for(int i=0;i<10;i++)
    ret += vis[i];
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
    for(int ic = 1;ic<=T;ic++) {
      string s;
      cin>>s;
      cout<<"Case #"<<ic<<": ";
      int ret = 0;
      char last = '-';
      if(s[0] == '-' ) ret = 1;
      for(int i=0;i<s.size();i++) {
        if(s[i] == '-' && last == '+')
          ret += 2;
        last = s[i];
      }
      cout<<ret<<endl;
    }
    return 0;
    
}
