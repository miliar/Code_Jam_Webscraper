#include<iostream>
#include<vector>
#include<string>
#define FOR(i,n) for(int i=0;i<n;i++)
using namespace std;


int main(){
    int T;
    cin>>T;
    FOR(k,T){
        int n;
        cin>>n;
        n++;
        string str;
        cin>>str;
        int tot=0;
        int needed = 0;
        FOR(i,n){
            int cur = (str[i]-'0');
            if(tot >= i){
                tot+=cur;
            }else{
                needed += (i-tot);
                tot += (i-tot)+cur;
            }
        }
        cout<<"Case #"<<k+1<<": "<<needed<<endl;
    }
}
