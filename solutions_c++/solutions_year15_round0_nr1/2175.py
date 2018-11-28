#include<stdio.h>
#include<iostream>
#include<string>
using namespace std;
int T,N;
string s;
int main(){
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    cin >> T;
    int tt = 0;
    while(T--){
        ++tt;
        cin>>N;
        cin>>s;
        int ret = 0;
        int num = 0;
        for(int i=0;i<s.size();++i){
            if(i<=num){
                num += (s[i]-'0');
            } else {
                ret += (i - num);
                num = i;
                num += (s[i]-'0');
            }
        }
        printf("Case #%d: %d\n",tt, ret);
    }
    return 0;
}
