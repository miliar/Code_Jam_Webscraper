#include<bits/stdc++.h>
using namespace std;
typedef __int128 LL;
vector<int>V;
bool isp(LL x){
    for(LL i=2;i*i<=x&&i<=1000;i++){
        if(x%i==0){
            V.push_back(i);
            return 0;
        }
    }
    return 1;
}
int a[42];
int len=32;
int cnt;
bool check(int x){
    for(int i=0;i<len-2;i++){
        a[1+i]=x>>i&1;
    }
    V.clear();
    for(int base=2;base<=10;base++){
        LL tmp=0;
        for(int j=len-1;j>=0;j--)tmp=tmp*base+a[j];
        if(isp(tmp))return 0;
    }
    for(int i=len-1;i>=0;i--)printf("%d",a[i]);
    for(int i=0;i<V.size();i++)printf(" %d",V[i]);
    puts("");
    return 1;
}
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    puts("Case #1:");
        a[0]=a[len-1]=1;
        for(int i=0;i<1<<(len-2)&&cnt<500;i++)cnt+=check(i);
    //printf("cnt=%d\n",cnt);
}
