#include <bits/stdc++.h>
using namespace std;
int test;
vector <string> s;
int n;

bool can(int B){
    vector <string> c=s;
    for (int i=0;i<n;i++)
    for (int j=0;j<n;j++)
    if (B&(1<<(i*n+j))) c[i][j]='1';
    //cout<<"B"<<B<<endl;
    for (int i=0;i<n;i++){
        vector <int> a;
        for (int j=0;j<n;j++) if (i!=j) a.push_back(j);
        do {
      //  cout<<"@@";
            vector <int> b;
            for (int j=0;j<n;j++)
            if (c[i][j]=='1') b.push_back(j);
        //    cout<<a.size()<<" "<<b.size()<<endl;
            if (b.size()<=a.size())
            do {
            //    cout<<"a";for (int i=0;i<a.size();i++) cout<<a[i];cout<<endl;
             //   cout<<"b";for (int i=0;i<b.size();i++) cout<<b[i];cout<<endl;
                bool cc=1;
                for (int j=0;cc && j<b.size();j++)
                cc&=(c[a[j]][b[j]]=='1');
          //      cout<<"cc"<<cc<<endl;
                if (cc) return 0;
            } while (next_permutation(b.begin(),b.end()));
        } while (next_permutation(a.begin(),a.end()));
    }
    return 1;
}

void sol(){
    cin>>n;
    s.resize(n);
    for (int i=0;i<n;i++) cin>>s[i];
    int BB=0;
    for (int i=0;i<n*n;i++)
        if (s[i/n][i%n]=='0') BB|=(1<<i);
    int ans=__builtin_popcount(BB);
    for (int B=BB;B;B=((B-1)&BB))
    if (can(B)) ans=min(ans,__builtin_popcount(B));
    if (can(0)) ans=0;

    cout<<"Case #"<<++test<<": "<<ans<<endl;
}

int main() {
    freopen("D.in","r",stdin);
    freopen("D.txt","w",stdout);
    int t;
    cin>>t;
    while (t--){
        sol();
    }
    return 0;
}
