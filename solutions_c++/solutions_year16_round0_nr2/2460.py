#include <cstdio>
#include <algorithm>
#include <iostream>
#include <deque>
#include <cstring>
using namespace std;

char S[111];

int main () {
    int T;
    cin>>T;
    for (int casenum=1;casenum<=T;casenum++) {
        memset(S,0,sizeof S);
        scanf("%s",S);
        int len=strlen(S),ans=0;
        for (int i=1;i<len;i++) ans+=(S[i]!=S[i-1]);
        ans+=(S[len-1]=='-');
        cout<<"Case #"<<casenum<<": "<<ans<<endl;
    }
}
