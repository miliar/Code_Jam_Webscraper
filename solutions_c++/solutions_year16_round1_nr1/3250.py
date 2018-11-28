#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int tests;
string str;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
cin >> tests;
for(int t=1;t<=tests;t++){
    cin >> str;
    string ans="";
    ans+=str[0];
    for(int i=1;i<str.size();i++){
        if(ans[0]<=str[i]){
            ans=str[i]+ans;
        } else {
            ans=ans+str[i];
        }
    }
    printf("Case #%d: %s\n",t,ans.c_str());


}



}
