#include<bits/stdc++.h>
using namespace std;
int main(){
    int T;
    freopen("B-large.in","r",stdin);
    freopen("yLarge.txt","w",stdout);
    scanf("%d",&T);
    for(int t=1;t<=T;++t){
        string s;
        cin>>s;
        int L=s.size();
        int cnt=0,idx=0;
        if(s[0]=='-'){
            ++cnt;
            while(idx<L && s[idx]=='-')
                ++idx;
        }
        while(idx<L){
            while(idx<L && s[idx]=='+')
                ++idx;
            if(idx==L)
                break;
            else{
                while(idx<L && s[idx]=='-')
                    ++idx;
                cnt+=2;
            }
        }
        printf("Case #%d: %d\n",t,cnt);
    }
    return 0;
}
