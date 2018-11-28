#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<queue>
#include<vector>
#include<stack>
#include<string>
#include<map>
#include<cmath>
#include<fstream>
using namespace std;

#define Min(a,b) a<b:a?b
#define Max(a,b) a>b:a?b
#define INF 0xfffffff

typedef long long ll;
int a[100],ans[3000];
int tot;
bool hui(int p){
    int cnt=0;
    while(p){
        a[cnt++]=p%10;
        p/=10;
    }
    for(int i=0;i<cnt/2;i++){
        if(a[i]!=a[cnt-1-i]) return 0;
    }
    return 1;
}

void init(){
    tot=0;
    memset(ans,0,sizeof(ans));
    for(int i=1;i<40;i++){
        if(hui(i)&&hui(i*i)) ans[i*i]=1;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    int T,l,r,cs=0;
    cin>>T;
    ofstream ff("a.out");
    while(T--){
        cin>>l>>r;
        cs++;
        int num=0;
        init();
        for(int i=l;i<=r;i++){
            if(ans[i]) num++;
        }
        ff<<"Case #"<<cs<<": "<<num<<endl;
    }
    ff.close();
    return 0;
}
