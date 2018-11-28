#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

set<int> st;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int j=1; j<=t; j++){
        int z;
        cin>>z;
        cout<<"Case #"<<j<<": ";
        for(int i=1; i<1000; i++){
           int d=z*i;

        while(d>0){
           st.insert(d%10);
           d/=10;
        }
        if(st.size()==10){cout<<z*i<<endl; break; }
        }
      if(st.size()<10)cout<<"INSOMNIA\n";

      st.clear();
    }

    return 0;
}
