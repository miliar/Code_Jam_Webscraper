#include<iostream>
#include<stack>
#include<string>
#include<cmath>
#include<vector>
using namespace std;
//#define SMALL
//#define LARGE

int main(){
#ifdef SMALL
    freopen("B-small-practice.in","r",stdin);
    freopen("B-small-practice.out","w",stdout);
#endif
    
#ifdef LARGE
    freopen("B-large-practice.in","r",stdin);
    freopen("B-large-practice.out","w",stdout);
#endif
    
    int T,N,j;
    cin>>T;
    for(int i=1;i<=T;i++){
        cin>>N;
        string s="0123456789";
        if(N==0) {cout<<"Case #"<<i<<": INSOMNIA"<<endl;continue;}
        for(j=1;s!="aaaaaaaaaa";j++){
            string s1=to_string(j*N);
            for(int k=0;k<s1.size();k++){
                replace(s.begin(),s.end(),s1[k],'a');
            }
        }
        double ans=(j-1)*N;
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
}
