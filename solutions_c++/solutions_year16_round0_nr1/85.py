#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

void split(int x,vector<bool>& vst){
    while(x){
        vst[x%10]=true;
        x/=10;
    }
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,N;
    int ans;
    cin>>T;
    for(int cas=1;cas<=T;cas++){
        cin>>N;
        if(N==0) {printf("Case #%d: INSOMNIA\n",cas);continue;}
        vector<bool> vst(10,false);
        ans = -1;
        for(int i=1;i<=200;i++){
            split(i*N,vst);
            bool ok = true;
            for(int b=0;b<10;b++) if(!vst[b]) ok=false;
            if(ok){
                ans = i*N;
                break;
            }
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
