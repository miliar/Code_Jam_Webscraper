#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#define fr(i,a,b) for(int i=a; i<b; i++)

using namespace std;
typedef vector<int> vi;


int main(){
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T, S;
    cin>>T;
    fr(t,0,T){
        int ans=0, total=0;
        string str;
        cin>>S>>str;
        fr(i,0,S+1){
            ans=max(ans,i-total);
            total+=str[i]-'0';
        }
        cout<<"Case #"<<t+1<<": "<<ans<<endl;
    }
}
