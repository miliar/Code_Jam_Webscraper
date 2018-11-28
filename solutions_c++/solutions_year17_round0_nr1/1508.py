#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int t;
    cin>>t;int c=0;
    while(t--){
        c++;
        
        string s;
        cin>>s;
        int k;
        cin>>k;
        int n=s.length();
        int cnt=0;
        for(int i=0;i<=n-k;i++){
            if(s[i]=='-' ){
                for(int j=i;j<i+k;j++){
                   if(s[j]=='-') s[j]='+';
                    else s[j]='-';
                }
                cnt++;
            }
         //       cout<<s<<endl;
        }
        bool flag=true;
        for(int i=0;i<n;i++){
            if(s[i]=='-') flag=false;
        }
        cout<<"Case #"<<c<<": ";
        if(flag) cout<<cnt;
        else cout<<"IMPOSSIBLE";
        cout<<endl;
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
