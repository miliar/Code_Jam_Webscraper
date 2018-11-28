#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;
int main(){
    freopen("inputB.in", "r", stdin);
    freopen("outputB.out", "w", stdout);
    int T;
    cin>>T;
    for(int t = 1; t <= T; t++){
        string str;
        cin>>str;
        int ans = 0;
        for(int i = 1; str[i]; i++)
            ans += (str[i - 1] != str[i]);
        cout<<"Case #"<<t<<": "<<ans + (str[str.size() - 1] == '-')<<endl;
    }
}
