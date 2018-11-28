#include <bits/stdc++.h>
using namespace std;
typedef long long int64;
typedef __int128 int128;
struct Time{
    clock_t c_lock=clock();
    ~Time(){
        fprintf(stderr,"\nrunning time: %lums\n",1000*(clock()-c_lock)/CLOCKS_PER_SEC);
    }
}Time;//return running time.
const int S=10;
const size_t N=16;
bool bit[N+1],tmp[N+1];
int cases,n,J;
int128 num[11][33];
void init(){
    for (int i=2; i<11; i++) {
        int128 tmp=1;
        for (int j=0; j<33; j++) {
            num[i][j]=tmp;
            tmp*=(int128)i;
        }
    }
}
int128 mult_mod(int128 a,int128 b,int128 c)//计算 (a*b)%c.a,b,c <2^63
{
    a%=c;
    b%=c;
    int128 ret=0;
    while(b)
    {
        if(b&1){ret+=a;ret%=c;}
        a<<=1;
        if(a>=c)a%=c;
        b>>=1;
    }
    return ret;
}
int128 pow_mod(int128 x,int128 n,int128 mod)//x^n%c
{
    if(n==1)return x%mod;
    x%=mod;
    int128 tmp=x;
    int128 ret=1;
    while(n)
    {
        if(n&1) ret=mult_mod(ret,tmp,mod);
        tmp=mult_mod(tmp,tmp,mod);
        n>>=1;
    }
    return ret;
}
//a^(n-1)=1(mod n)  一定是合数返回true不一定返回false
bool check(int128 a,int128 n,int128 x,int128 t)
{
    int128 ret=pow_mod(a,x,n);
    int128 last=ret;
    for(int i=1;i<=t;i++)
    {
        ret=mult_mod(ret,ret,n);
        if(ret==1&&last!=1&&last!=n-1) return true;//合数
        last=ret;
    }
    if(ret!=1) return true;
    return false;
}
bool Miller_Rabin(int128 n)
{
    if(n<2)return false;
    if(n==2)return true;
    if((n&1)==0) return false;//偶数
    int128 x=n-1;
    int128 t=0;
    while((x&1)==0){x>>=1;t++;}
    for(int i=0;i<S;i++)
    {
        int128 a=rand()%(n-1)+1;
        if(check(a,n,x,t))
            return false;//合数
    }
    return true;
}
inline void print128(int128 &i){
    int128 p=i;
    stack<int>print;
    while (p>0) {
        print.push(p%10);
        p/=10;
    }
    while(!print.empty()){printf("%d",print.top());print.pop();}
}
int128 getfac(int128 &t){
    int128 temp=(int128)((double)sqrt(t)+1);
    for (int i=2; i<=temp; i++) {
        if (t%i==0) {
            return i;
        }
    }
    return 1;
}
void print(vector<int128>& pp){
    print128(pp[8]);
    for (int i=0; i<=8; i++) {
        int128 res=getfac(pp[i]);
        printf(" ");
        print128(res);
    }
    puts("");
}
void solve(){
    int cnt=0;
    for (int i=0;cnt<J&&i<=N-2; i++) {
        if(i){bit[N-i]=!bit[N-i];}
        memcpy(tmp, bit, sizeof bit);
        do{
            int flag=0;vector<int128>store;
            for (int j=2; j<=10; j++) {
                int128 temp=0;
                for (int k=1; k<=N; k++) {
                    temp+=bit[k]*num[j][N-k];
                }
                if (Miller_Rabin(temp)) {
                    flag=1;break;
                }
                store.push_back(temp);
            }
            if (!flag) {
                ++cnt;print(store);
            }
        }while(cnt<J&&next_permutation(bit+2, bit+N));
        memcpy(bit,tmp,sizeof tmp);
    }
}
int main(){
    freopen("out.txt", "w", stdout);
    init();
    scanf("%d",&cases);
    puts("Case #1:");
    scanf("%d%d",&n,&J);
    memset(bit, 0, sizeof bit);
    bit[1]=bit[16]=1;
    solve();
}