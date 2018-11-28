#include <iostream>
#include <memory.h>
#include <stdio.h>
using namespace std;
int ans[17];
void work(int r){
    int tmp;
    for(int i=1; i<=4; i++){
        for(int j=1; j<=4; j++){
            cin>>tmp;
            if(i == r){
                ans[tmp] ++;
            }
        }
    }
}
int res(){
    int ret = 0;
    for(int i=1; i<=16; i++){
        if(ans[i] > 1){
            if(ret == 0){
                ret = i;
            } else {
                return -1;
            }
        }
    }
    return ret;
}
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t,r;
    cin>>t;
    for(int i=1; i<=t; i++){
        memset(ans, 0, sizeof(ans));
        cin>>r;
        work(r);
        cin>>r;
        work(r);
        int tmp = res();
        cout<<"Case #"<<i<<": ";
        if(tmp == -1)cout<<"Bad magician!"<<endl;
        else if(tmp == 0)cout<<"Volunteer cheated!"<<endl;
        else cout<<tmp<<endl;
    }
}
