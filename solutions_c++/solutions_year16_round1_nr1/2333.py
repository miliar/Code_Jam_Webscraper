#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
using namespace std;
void solve(){
    printf(" ");
    string str;
    cin >> str;
    int len=str.size();
    
    string ret;
    ret += str[0];
    for (int i=1;i<len;++i){
        if (ret[0]>str[i])
            ret += str[i];
        else ret = str[i] + ret;
    }
    cout << ret << endl;
}

int main(){
    int ntest;
    scanf("%d",&ntest);
    for (int test=1;test<=ntest;++test){
        printf("Case #%d:",test);
        solve();
    }
    return 0;
}
