#include <bits/stdc++.h>
#define pr(l) printf("Case #%d: ",l)
#define mod 1000000007
#define Int long long int
using namespace std;
 int main(){
    freopen("blarge.txt","r",stdin);
    freopen("out2b.txt","w",stdout);
    int test;
    cin>>test;
    Int l = 0;
    while(test--){
        l++;
        string str;
        cin>>str;
        Int ans = 0;
        Int i;
        int fl = 0;
        for(i=0;i<str.size();i++){
            if(str[i]=='-'){
                while(i<str.size()&&str[i]=='-'){
                    i++;
                }
                if(fl==0){
                    ans+=1LL;
                    fl = 1;
                }
                else{
                    ans+=2LL;
                }
            }
            else{
                fl = 1;
            }
        }
        pr(l);
        cout<<ans<<"\n";
    }
    return 0;
 }
