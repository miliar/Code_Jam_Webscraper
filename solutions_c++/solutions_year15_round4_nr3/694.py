#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <cstdio>
#include <map>
#include <set>
using namespace std;
const long long mod = 1e9+7;
const long long PP = 1123;
set<long long> P[30];
vector<int> CP[30];
int Ans[4000];
string S;
int col[30];
int solve(){
    int n; cin>>n;
    vector<long long>A;
    for(int id=0;id<n;id++){
        P[id].clear(); CP[id].clear();
        getline(cin,S);
        if(S.length()==0)getline(cin,S);
        //cout<<S<<endl;
        int m = (int)S.length();
        int i=0,j=0;
        while(i<m){
            while(S[i]==' ' && i<m)i++;
            if(i>=m)break;
            j=i;
            while(S[j]!=' ' && j<m)j++;
            long long cur=S[i];
            for(int k=i+1;k<j;k++){
                cur = (cur*PP+S[k])%mod;
            }
            //cout<<i<<","<<j<<"::"<<A<<endl;
            P[id].insert(cur);
            A.push_back(cur);
            i=j;
        }
    }
    sort(A.begin(),A.end());
    A.erase(unique(A.begin(), A.end()),A.end());
    //cout<<A.size()<<endl;
    for(int id=0;id<n;id++){
        for(set<long long>::iterator ij=P[id].begin();ij!=P[id].end();ij++){
            int pos = (int)(lower_bound(A.begin(), A.end(), *ij)-A.begin());
            //cout<<*ij<<"::"<<pos<<endl;
            CP[id].push_back(pos);
        }
    }
    memset(col,0,sizeof(col));
    col[0]=0;col[1]=1;
    int mi=1e9;
    for(int i=0;i<1<<(n-2);i++){
        for(int j=0;j<(n-2);j++){
            if((1<<j)&i)col[j+2]=1;
            else col[j+2]=0;
        }
        memset(Ans,0,sizeof(Ans));
        for(int id=0;id<n;id++){
            for(vector<int>::iterator it=CP[id].begin();it!=CP[id].end();it++){
                Ans[*it]|=1<<col[id];
            }
        }
        int cur=0;
        for(int j=0;j<(int)A.size();j++){
            if(Ans[j]==3)cur++;
        }
        mi=min(cur,mi);
    }
    return mi;
}
int main(){
    freopen("/Users/DXY/Desktop/DXY/in","r",stdin);
    freopen("/Users/DXY/Desktop/DXY/out","w",stdout);
    //freopen("/Users/DXY/Desktop/DXY/aaa","w",stdout);
    int T;cin>>T;
    for(int i=1;i<=T;i++){
        printf("Case #%d: %d\n",i,solve());
    }   return 0;
}

/*
int R,C;
vector<int> Got(int mask){
    vector<int> x;
    for(int j=0;j<R;j++){
        int k = 1<<(2*j);
        int cur=0;
        if(mask & k)cur++;
        if(mask & (k<<1))cur+=2;
        x.push_back(cur);
    }
    return x;
}
int X[10][10];
int work(){
    for(int r=0;r<R;r++){
        int cnt=0;
        if(r-1>=0 && X[r-1][0]==X[r][0])cnt++;
        if(r+1<R && X[r+1][0]==X[r][0])cnt++;
        if(X[r][1]==X[r][0])cnt++;
        if(cnt>X[r][0])return 0;
    }
    for(int c=1;c<C;c++){
        for(int r=0;r<R;r++){
            int cnt=0;
            if(r-1>=0 && X[r-1][1]==X[r][1])cnt++;
            if(r+1<R && X[r+1][1]==X[r][1])cnt++;
            if(X[r][1]==X[r][0])cnt++;
            if(cnt>X[r][1])return 0;
            
        }
    }
}
int solve(){
    int ans=0;
    for(int i=0;i<(1<<(R*2));i++){
        vector<int> cur = Got(i);
        for(int r=0;r<R;r++){
            X[r][0]=cur[r]+1;
        }
        if(X[0][0]==4 || X[R-1][0]==4)continue;
        for(int j=0;j<(1<<R*2);i++){
            cur = Got(j);
            for(int r=0;r<R;r++){
                X[r][1]=cur[r]+1;
            }
            ans+=work();
        }
    }
    return ans;
}
int main(){
    //freopen("/Users/DXY/Desktop/DXY/in","r",stdin);
    //freopen("/Users/DXY/Desktop/DXY/out","w",stdout);
    freopen("/Users/DXY/Desktop/DXY/aaa","w",stdout);
    for(R=2;R<=6;R++){
        for(C=3;C<=6;C++){
            printf("mp[%d][%d]=%d;\n",R,C,solve());
        }
    }
    /*
    int T;cin>>T;
    for(int i=1;i<=T;i++){
        int ans=solve();
        printf("Case #%d: ",i);
        if(ans==-1)printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);
    }
    return 0;
}*/