#include<bits/stdc++.h>
using namespace std;
map<string, int> mp;
bitset<2005> s[2], s0, s1;
bitset<2005> sentance[20];
int tot;
int insert(string str){
    if(mp.find(str)==mp.end()){
        mp[str]=tot++;
    }
    return mp[str];
}
char str[2005];
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int T; cin>>T;
    for(int cs=1; cs<=T; cs++){
        int n; cin>>n; cin.ignore();
        char ch; tot=0; mp.clear();
        s[0].reset(); s[1].reset();
        while(scanf("%s%c",str,&ch)!=EOF){
            s[0].set(insert(str));
            if(ch==EOF||ch=='\n') break;
        }
        while(scanf("%s%c",str,&ch)!=EOF){
            s[1].set(insert(str));
            if(ch==EOF||ch=='\n') break;
        }
        n-=2;
        for(int i=0; i<n; i++){
            sentance[i].reset();
            while(scanf("%s%c",str,&ch)!=EOF){
                sentance[i].set(insert(str));
                if(ch==EOF||ch=='\n') break;
            }
        }
        if(n==0){
            printf("Case #%d: %d\n",cs,(s[0]&s[1]).count());
            continue;
        }
        int ans=1000000;
        for(int i=0; i<(1<<n); i++){
            s0=s[0]; s1=s[1];
            for(int j=0; j<n; j++){
                if(i>>j&1){
                    s0|=sentance[j];
                }
                else{
                    s1|=sentance[j];
                }
            }
            int ret=(s0&s1).count();
            ans=min(ans,ret);
        }
        printf("Case #%d: %d\n",cs,ans);
    }
    return 0;
}


