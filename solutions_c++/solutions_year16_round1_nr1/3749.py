#include<cstdio>
#include<algorithm>
#include<cstring>
#include<iostream>
#include<vector>
using namespace std;
char s[1005];
int vis[1005];
vector<pair<int ,int> > res;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,n,cnt=0,now,first,icas=0;
    scanf("%d",&T);
    while(T--){
        scanf("%s",s);
        n= strlen(s);
        cnt=0;
        memset(vis,0,sizeof vis);
        res.clear();
        while(1){
            now=-1;
            if(n==0) break;
            bool flag=0;
            int num=0;
            for(int i=0;i<n;i++){
                if(now<s[i]-'A')
                    now=s[i]-'A';
            }
            for(int i=0;i<n;i++){
                if(s[i]-'A'==now&&flag==0){
                    first=i;  flag=1;
                    num++;
                    vis[i]=1;
                }
                else if(s[i]-'A'==now&&flag){
                    num++;
                    vis[i]=1;
                }
            }
            res.push_back(pair<int,int>(now,num));
            cnt++;
            n=first;
        }
        printf("Case #%d: ",++icas);

        for(int i=0;i<cnt;i++){
            int a=res[i].first,b=res[i].second;
            for(int j=0;j<b;++j){
                printf("%c",a+'A');
            }
            //printf("%d %d\n",a,b);
        }
        n=strlen(s);
        for(int i=0;i<n;++i){
            if(!vis[i])
                printf("%c",s[i]);
        }
        printf("\n");
    }

    return 0;
}
