#include "bits/stdc++.h"
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define rep(i,n) for(ll i=0;i<(ll)(n);i++)
#define all(a)  (a).begin(),(a).end()
#define vi vector<int>
#define pb push_back
#define INF 999999999

int main(){
    int t;
    cin>>t;
    rep(i,t){
        int c=0;
        string s;
        cin>>s;
        for(int j=s.size()-1;j>=0;j--){
            if(s[j]=='-'){
                c++;
                for(int k=0;k<=j;k++){
                    if(s[k]=='-')   s[k]='+';
                    else            s[k]='-';
                }
            }
        }
        cout<<"Case #"<<i+1<<": ";
        cout<<c<<endl;
    }
}