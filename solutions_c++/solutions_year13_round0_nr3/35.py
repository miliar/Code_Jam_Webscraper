#include<stdio.h>
#include<string.h>
#include<vector>
#include<string>
#include<iostream>
#define pb push_back
using namespace std;
int cs;
vector<string>d[51];
bool compare(string &str1,string &str2){
    if(str1.size()<str2.size())return 1;
    if(str1.size()>str2.size())return 0;
    for(int i=0;i<str1.size();i++){
        if(str1[i]<str2[i])return 1;
        if(str1[i]>str2[i])return 0;
    }
    return 1;
}
int a[111],N,b[55];
void dfs(int x){
    if(x>N-1-x){
        string str="";
        int i;
        for(i=N*2;a[i]==0;i--);
        for(int j=0;j<=i;j++)
            if(a[j]!=a[i-j])return;
        for(;i>=0;i--)str+='0'+a[i];
        d[N].pb(str);
        cout<<str<<endl;
        return;
    }
    int i,j;
    if(x==0)i=1;
    else i=0;
    for(;i<3;i++){
        b[x]=i;
        for(j=0;j<N;j++){
            if(b[j]==-1)continue;
            if(x==j)a[x+j]+=b[x]*b[j];
            else a[x+j]+=b[x]*b[j]*2;
        }
        if(x<N-1-x){
            b[N-1-x]=i;
            for(j=0;j<N;j++){
                if(b[j]==-1)continue;
                if(N-1-x==j)a[N-1-x+j]+=b[N-1-x]*b[j];
                else a[N-1-x+j]+=b[N-1-x]*b[j]*2;
            }
        }
        for(j=0;j<N+N;j++){
            a[j+1]+=a[j]/10;
            a[j]%=10;
        }
        int len;
        for(len=N+N;a[len]==0;len--);
        for(j=0;j<=x;j++){
            if(a[j]!=a[len-j])break;
        }
        if(j>x){
            dfs(x+1);
        }
        for(j=0;j<N;j++){
            if(b[j]==-1)continue;
            if(N-1-x==j)a[N-1-x+j]-=b[N-1-x]*b[j];
            else a[N-1-x+j]-=b[N-1-x]*b[j]*2;
        }
        b[N-1-x]=-1;
        if(b[x]!=-1){
            for(j=0;j<N;j++){
                if(b[j]==-1)continue;
                if(x==j)a[x+j]-=b[x]*b[j];
                else a[x+j]-=b[x]*b[j]*2;
            }
            b[x]=-1;
        }
        for(j=0;j<N+N;j++){
            a[j+1]-=(a[j]/10);
            a[j]+=(a[j]/10)*10;
            while(a[j]<0){
                a[j+1]--;
                a[j]+=10;
            }
        }
    }
}
void go(int n){
    N=n;
    memset(a,0,sizeof(a));
    memset(b,-1,sizeof(b));
    dfs(0);
    fprintf(stderr,"len:%d num:%d\n",n,(int)d[n].size());
}
int main(){
    int T,i,j;
    d[1].pb("1");
    d[1].pb("4");
    d[1].pb("9");
    for(i=2;i<=50;i++)go(i);
    fprintf(stderr,"end\n");
    return 0;
    scanf("%d",&T);
    while(T--){
        string A,B;
        cin>>A>>B;
        printf("Case #%d: ",++cs);
        int an=0;
        for(i=1;i<=50;i++)
            for(j=0;j<d[i].size();j++)if(compare(A,d[i][j])&&compare(d[i][j],B))an++;
        printf("%d\n",an);
        
    }
}
