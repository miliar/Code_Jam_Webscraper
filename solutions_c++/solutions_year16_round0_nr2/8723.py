#include <iostream>
#include <cstdio>
#include <string>
using namespace std;
int T;
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin>>T;
    string str;
    for (int i = 1; i <= T; ++i) {
        cin>>str;
        int ans=0;
        for (int j = 0; j < str.length()-1; ++j)
            if(str[j]!=str[j+1])ans++;
        if(str[str.length()-1]=='-')ans++;
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}