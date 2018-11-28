#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<algorithm>
#include<queue>
#include<map>
#include<vector>
#include<set>
#define FOR(i,a,b) for(LL i=a;i<b;i++)
#define FORr(i,a,b) for(int i=a;i>=b;i--)
#define tr(it,M) for(it=M.begin();it!=M.end();it++)
#define F first
#define S second
#define lim 1000
#define infi 10000
#define MOD 5000000
using namespace std;
typedef long long LL;
int k;
LL cmax=100000000000000;
//bool check(LL n){
//    LL x=n,i=0;
//    int A[30];
//    while(x>0){
//        A[i++]=x%10;
//        x/=10;
//    }
//    bool fp=1;
//    FOR(j,0,i){
//        if(A[j]!=A[i-j-1]){fp=0;break;}
//    }
//    return fp;
//}
//void preprocess(){
//    k=0;
//    FOR(i,1,sqrt(cmax)){
//        if(check(i)){
//            if(i*i<cmax && check(i*i)){
//                num[k++]=i*i;
//            }
//        }
//    }
//}
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int test,t=0;scanf("%d",&test);
    LL num[]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
    while(test--){
        t++;
        k=39;
        LL l,r;
        scanf("%lld%lld",&l,&r);
        int ans=0;
        int left=(int)(lower_bound(num,num+k,l)-num);
        int right=(int)(lower_bound(num,num+k,r)-num);
        if(num[left]==l && num[right]==r) ans=right-left+1;
        else if(num[right]==r && num[left]!=l) ans=right-left+1;
        else if(num[left]==l && num[right]!=r) ans=right-left;
        else ans=right-left;
//        cout<<left<<"  "<<right<<"  "<<ans<<endl;
        printf("Case #%d: %d\n",t,ans);

    }
    return 0;
}


