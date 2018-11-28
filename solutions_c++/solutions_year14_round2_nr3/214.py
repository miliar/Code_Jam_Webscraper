#include<stdio.h>
#include<algorithm>
#include<vector>
#include<stdlib.h>
#include<iostream>
using namespace std;

int n,m;
string zipCode[10];
string ans="";
vector<int> e[10];
int ret[100];
int top=0;
void solve(){
    ans="";
    top=0;
    scanf("%d %d",&n,&m);
    vector<int> perm;
    for(int i = 0 ; i < n ; ++ i ){
        cin >> zipCode[i];
        e[i].clear();
        perm.push_back(i);
    }
    for(int i = 0 ; i < m ; ++ i ){
        int a,b;
        scanf("%d %d",&a,&b);
        a--;b--;
        e[a].push_back(b);
        e[b].push_back(a);
    }

    do{
        string tmp="";
        for(int i = 0 ; i < n ; ++ i ) tmp=tmp+zipCode[perm[i]];
        top=0;
        int now=perm[0];
        bool isOkay=true;
        for(int i = 1 ; i < n && isOkay ; ++ i ){
            bool couldGo=false;
            while(!couldGo){
                for(int j = 0 ; j < e[now].size();++j)
                    if(e[now][j]==perm[i])couldGo=true;
                if(!couldGo){
                    if(top){
                        now=ret[--top];
                    }
                    else {
                        isOkay=false;
                        break;
                    }
                }
            }
            if(couldGo){
                ret[top++]=now;
                now=perm[i];
            }

        }

        if(isOkay){
            if(ans==""|| tmp<ans)ans=tmp;
        }
    }while(next_permutation(perm.begin(),perm.end()));
    printf("%s\n",ans.c_str());
}

int main(){
    freopen("C-small-attempt0"".in","r",stdin);
    freopen("C-small-attempt0"".out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i = 1 ; i <= t ; ++ i ){
        printf("Case #%d: ",i);
        solve();
    }
}
