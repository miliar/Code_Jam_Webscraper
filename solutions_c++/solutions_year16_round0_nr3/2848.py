#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;
vector<vector<long long > > ans;
long long allp[11][17];
int n,t,jj,isp[10000007];
map<long long ,bool>mp;
vector<int> all;
int f(long long num){

int ret=-1;
for(int i=0;i<all.size();i++){
    if(num%all[i]==0&&num!=(long long)all[i]){ret=all[i];break;}
}
return ret;
}
void bk(string ss,int pos){
if(ans.size()>=jj||pos==0){return;}
long long bs[11];
for(int i=0;i<=10;i++){bs[i]=0;}
for(int i=0;i<ss.size();i++){
    bs[10]*=10;
    bs[10]+=(int)(ss[i]-'0');
}
bs[1]=bs[10];
for(int i=n-1;i>-1;i--){
    if(ss[i]=='1'){
for(int k=2;k<10;k++){
bs[k]+=allp[k][n-i-1];
}}}
int ok=1;
vector<long long > v;
v.push_back(bs[1]);
for(int i=2;i<=10;i++){
    bs[i]=f(bs[i]);
    if(bs[i]==-1){ok=0;break;}
    v.push_back(bs[i]);
}
if(ok&&!mp.count(bs[1])){
    ans.push_back(v);
mp[bs[1]]=1;
}

string aa=ss;
aa[pos-1]='1';
bk(aa,pos-1);bk(ss,pos-1);
}
int main()
{
    for(int i=2;i<=9;i++){
        long long p=1;
        for(int j=0;j<17;j++){
            allp[i][j]=p;
            p*=i;
        }
    }
    for(int i=2;i<=1000;i++){
        if(!isp[i]){
            for(long long j=i*i;j<=10000000;j+=i)
            isp[j]=1;
        }}

    for(int i=2;i<=10000000;i++){
        if(!isp[i]){all.push_back(i);}
        }

     freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
scanf("%d",&t);
for(int tt=1;tt<=t;tt++){
       printf("Case #%d:\n",tt);

    scanf("%d %d",&n,&jj);
    ans.clear();
    string s="1000000000000000";
    s[n-1]='1';
    bk(s.substr(0,n),n-1);
for(int i=0;i<jj;i++){
    for(int k=0;k<10;k++){
if(k){printf(" ");}
        printf("%lld",ans[i][k]);
    }
   printf("\n");
}}
    return 0;
}
