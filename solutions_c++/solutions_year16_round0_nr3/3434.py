#include<cstdio>
#include<cstring>
#include<bitset>
#include<stack>
#include<queue>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<iostream>
#include<cmath>
#include<cassert>
#include<climits>
#include<sstream>
#define N 111111
#define M 555555
#define LL long long
#define FOE(i,a,b) for(int i=(a);i<=(b);++i)
#define FOD(i,a,b) for(int i=(b);i>=(a);--i)
#define CLR(a,b) memset(a,b,sizeof(a))
#define lc(x) (x<<1)
#define rc(x) (lc(x)|1)
#define inf 0x3f3f3f3f
using namespace std;
int t,n,m,q,k,cs=0;
int a[N],b[N];
vector<int> ans;
int getFactor(LL x){
    int lim= sqrt(x+1);
    for(int i=2;i<=lim;++i){
        if(x%i == 0)return i;
    }
    return -1;
}
bool isJamCoint(string pk){
    ans.clear();
    int sl=pk.length();
    for(int i=2;i<=10;++i){
        LL tmp=0;
        for(int j =0;j<sl;++j){
            tmp = tmp*i + pk[j]- '0';
        }
        int me =getFactor(tmp);
        if(me<0)return false;
        //printf("tmp:%lld fac:%d\n",tmp,me);
        ans.push_back(me);
    }
    return true;
}
int main(){
    scanf("%d",&t);
    while(t--){
        printf("Case #%d:\n",++cs);
        scanf("%d%d",&n,&k);
        int ct=0;
        LL mx = 1<<n;
        for(LL i=1;i<=mx;++i){
            string pk="";
            LL tmp = i;
            int d=0;
            do{
                ++d;
                pk += (tmp& 0x01)?'1':'0';
                tmp >>= 1;
            }while(d<n);
            reverse(pk.begin(),pk.end());
            if(pk[0]=='1' && pk[n-1]=='1' && isJamCoint(pk)){
                ++ct;
                //printf("ct:%d \n",ct);
                printf("%s",pk.c_str());
                for(int j=0;j<(int)ans.size();++j)printf(" %d",ans[j]);
                puts("");
            }
            if(ct==k)break;
        }
    }
    return 0;
}

