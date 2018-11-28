#include<iostream>
#include<stack>
#include<string>
#include<cmath>
#include<vector>
using namespace std;
//#define SMALL
#define LARGE

int main(){
#ifdef SMALL
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
#endif
    
#ifdef LARGE
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
#endif
    
    int T,ans;
    cin>>T;
    getchar();
    for(int i=1;i<=T;i++){
        string s;
        getline(cin,s);
        auto last=unique(s.begin(),s.end());///////////
        s.erase(last, s.end());///////////
        int n=count(s.begin(),s.end(),'-');
        if(s[0]=='-') ans=2*n-1;
        else ans=2*n;
        cout<<"Case #"<<i<<": "<<ans<<endl;
        //cout<<"Case #"<<i<<": "<<s<<endl;
    }
}
