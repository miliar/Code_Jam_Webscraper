#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)


int a[2][200];

int main(){

    int t;
    cin>>t;
    rep(k,t){
        memset(a,0,sizeof a);
        string st;
        cin>>st;
        if(st[0]=='+')a[1][0]=1;
        else a[0][0]=1;
        for(int i=1;i<st.size();i++){
            a[0][i]=(st[i]=='+'?a[0][i-1]:a[1][i-1]+1);
            a[1][i]=(st[i]=='-'?a[1][i-1]:a[0][i-1]+1);
        }
        int  ans=a[0][st.size()-1];
      cout<<"Case #"<<k+1<<": "<<ans<<endl;
    }

    return 0;
}