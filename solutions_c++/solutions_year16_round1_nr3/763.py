#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
using namespace std;

typedef long long LL;

#define INF 100000000
int N;
int nxt[1024];
int hitP[1024];
int len[1024];
bool vst[1024];

void dfs(int x,int h ,int start){
    if(vst[x]){
        len[start]  = h;
        hitP[start] = x;
        return;
    }
    vst[x] = true;
    dfs(nxt[x],h+1,start);
}

int solve1(int i){
    if(hitP[i]==i) {
        return len[i];
    }
    return 0;
}

int solve2(int i){
    int ans = len[i];
    int v = nxt[hitP[i]];
    for(int ii=0;ii<N;ii++){
        if(hitP[ii]==v){
            ans = max(ans,len[i]+len[ii]-2);
        }
    }
    return ans;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int T;
    cin>>T;
    for(int cas=1;cas<=T;cas++){
        cin>>N;
        int x;
        for(int i=0;i<N;i++){
           cin >> nxt[i];
           nxt[i]--;
        }
        for(int i=0;i<N;i++) {
            memset(vst,0,sizeof(vst));
            dfs(i,0,i);
        }

        map<int,int> hash2;

        int ans = 0;
        for(int i=0;i<N;i++){
            int v = hitP[i];
            if(nxt[ nxt[v] ] == v ){
                int s = solve2(i);
                ans = max(ans,s);

                int a = hitP[i];
                int b = nxt[a];
                if(a<b) swap(a,b);
                int key = a*10000+b;
                if(hash2.find(key)==hash2.end()) hash2[key] = s;
                else hash2[key] = max(hash2[key],s);

            }
            else{
                ans = max(ans,solve1(i));
            }
        }
        int tmp = 0;
        for(auto it = hash2.begin();it!=hash2.end();it++){
            tmp+=it->second;
        }
        ans = max(ans,tmp);



        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
