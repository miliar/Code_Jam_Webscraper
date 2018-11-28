#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

int f[2][200];

int dp(int U,int L){
    if(L==1){
        return U^1;
    }
    if(f[U][L]!=-1) return f[U][L];
    return f[U][L] = 1 + dp(U^1,L-1);
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    memset(f,-1,sizeof(f));
    string in;
    int T;
    cin>>T;
    for(int cas=1;cas<=T;cas++){
        cin>>in;
        int  N = 1;
        int  len = in.length();
        for(int i = 1;i<len;i++ ){
            if(in[i-1]!=in[i]) N++;
        }
        int ans = dp(int(in[0]=='+'),N);
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
