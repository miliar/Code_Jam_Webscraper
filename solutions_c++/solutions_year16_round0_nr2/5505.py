#include <bits/stdc++.h>
#include<iostream>
using namespace std;
typedef long long int lli;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
#define read() freopen("B-large.in", "r", stdin)
#define write() freopen("output1.txt", "w", stdout)
int main(){
    read();
    write();
    lli t, x;
    cin>>t;x=t;
    while(t--){
        lli n, c=0; char f='-';
        string a; cin>>a;n= a.length();
        for(lli i= n-1; i>=0; i--){ lli j=i;
            for(j=i; j>=0 && a[j]==f;j--);
            if(j!=i){
                f=(f=='-')?'+':'-'; c++;
              //  cout<<f<<endl;
                i=j+1;
            };
        }
        cout<<"Case #"<<x-t<<": "<<c<<endl;
    }
}
