#include <bits/stdc++.h>
using namespace std;
 
typedef pair<int,int> pii;
typedef long long ll;

void fastStream(){cin.tie(0);std::ios_base::sync_with_stdio(0);}

char S[2000];
int len;

int main(){
  fastStream();
  int T;
  cin>>T;
  for(int t=1;t<=T;t++){
    cout<<"Case #"<<t<<": ";
    cin>>len;
    cin>>S;
    int tot = 0;
    int res = 0;
    for(int i = 0; i <= len; i++){
      if(tot>=i){}
      else{
        res+=i-tot;
        tot+=i-tot;
      }
      tot += S[i] - '0';
    }
    cout<<res<<endl;
  }
  
  return 0;
}
