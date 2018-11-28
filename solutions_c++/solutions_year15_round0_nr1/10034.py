#include<bits/stdc++.h>

using namespace std;

int main(){
    int test;
    cin>>test;
    for(int t=1;t<=test;t++){
        int max_shy;
        cin>>max_shy;
        string shy_arr;
        cin>>shy_arr;
        int clapped=0,needed=0;
        for(int i=0;i<shy_arr.size();i++){
            if(i==0){
                clapped+=shy_arr[i]-48;
            }
            else if(i<=clapped){
                clapped+=shy_arr[i]-48;
            }
            else{
                if(shy_arr[i]=='0')
                continue;
                else{
                    needed += i-clapped;
                    clapped+=(i-clapped)+(shy_arr[i]-48);
                }
            }
        }
        printf("Case #%d: %d\n",t,needed);
    }
    return 0;
}
