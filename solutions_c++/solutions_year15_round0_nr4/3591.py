#include <bits/stdc++.h>
using namespace std;
//ios_base::sync_with_stdio(false);
#ifdef CORLEONE
  #define d(b) cerr<< #b << " " << b << endl
  #else
  #define d(b)
#endif

int main()
{
  freopen("input4.in","r",stdin);
  freopen("output4.txt","w",stdout);
  int t;
  cin>>t;
 for(int rr=1;rr<=t;rr++)
  {
    int x,c,r;
    cin>>x>>c>>r;
    int area = c*r;
    if(x==1) cout<<"Case #"<<rr<<": GABRIEL"<<endl;
    else if(x==2 && area%x == 0) cout<<"Case #"<<rr<<": GABRIEL"<<endl;
    else if(x==3 && area==3) cout<<"Case #"<<rr<<": RICHARD"<<endl;
    else if(x==3 && area%x==0) cout<<"Case #"<<rr<<": GABRIEL"<<endl;
    else if(x==4 && area/x>=3 && area%x==0)cout<<"Case #"<<rr<<": GABRIEL"<<endl;
    else cout<<"Case #"<<rr<<": RICHARD"<<endl;
  }
}