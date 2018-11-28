#include <stdio.h>
#include <string.h>
#include <queue>
#include <algorithm>
#include <iostream>
#include <string>

int index(char i){
    if(i=='i') return 2;
    if(i=='j') return 3;
    return 4;
}

int map[5][5]={{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}
};

int cal(int a,int b){
    int ans=1;
    if(a<0) ans*=-1,a*=-1;
    ans*=map[a][b];
    return ans;
}

int get(int all,int x){
    int tag=1;
    if(x<0){
        tag=-1;x*=-1;
    }
    for(int i=1;i<=4;i++){
        if(tag * map[x][i] == all){
            return i;
        }
        if(tag * map[x][i] == -all){
            return -i;
        }
    }
    return -1;
}

int t,l,x;
std::string s,ss;
int ans[10005];
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    std::cin>>t;
    for(int ca=1;ca<=t;ca++){
        std::cin>>l>>x;
        std::cin>>s;
        ss.clear();
        for(int i=0;i<x;i++){
            ss += s;
        }
        int le=ss.size();
        ans[0]=index(ss[0]);
        for(int i=1;i<le;i++){
            ans[i]=cal(ans[i-1],index(ss[i]));
        }
        bool ok=0;
        for(int i=1;i<le && !ok;i++){
            for(int j=i+1;j<le && !ok;j++){
                int a=ans[i-1];
                int b=get(ans[j-1],ans[i-1]);
                int c=get(ans[le-1],ans[j-1]);

                if(a==2 && b==3 && c==4){
                    ok=1;break;
                }
            }
       }
        printf("Case #%d: %s\n",ca,ok?"YES":"NO");
    }
    return 0;
}
