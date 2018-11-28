#include "stdio.h"
#include "iostream"
using namespace std;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("a_big.out","w",stdout);
    int t;
    string d;
    cin>>t;
    for(int l=1;l<=t;l++){
        cin>>d;
        printf("Case #%d: ",l);
        string ans;
        for(int i=0;i<d.length();i++){
            if(ans.length()==0) ans.insert(ans.end(),d[i]);
            else if(d[i]<ans[0]) ans.insert(ans.end(),d[i]);
            else ans.insert(ans.begin(),d[i]);
        }
        cout<<ans<<endl;
    }
}
