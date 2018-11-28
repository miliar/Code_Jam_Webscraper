/*  ^^ ====== ^^
ID: meixiuxiu
PROG: test
LANG: C++11
*/
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <cmath>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cctype>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int ,int> pii;
#define MEM(a,b) memset(a,b,sizeof a)
#define CLR(a) memset(a,0,sizeof a);
#define pi acos(-1.0)
#define maxn 40000
#define maxv 100005
int MAXN = 10;
const int inf = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
#define LOCAL
bool vis[10000005];
bool ok[10000005];
int a[100];
const int S=20;//����㷨�ж�������SԽ���д����ԽС
//���� (a*b)%c.   a,b����long long������ֱ����˿��������
//  a,b,c <2^63
long long mult_mod(long long a,long long b,long long c)
{
    a%=c;
    b%=c;
    long long ret=0;
    while(b)
    {
        if(b&1){ret+=a;ret%=c;}
        a<<=1;
        if(a>=c)a%=c;
        b>>=1;
    }
    return ret;
}

//����  x^n %c
long long pow_mod(long long x,long long n,long long mod)//x^n%c
{
    if(n==1)return x%mod;
    x%=mod;
    long long tmp=x;
    long long ret=1;
    while(n)
    {
        if(n&1) ret=mult_mod(ret,tmp,mod);
        tmp=mult_mod(tmp,tmp,mod);
        n>>=1;
    }
    return ret;
}
//��aΪ��,n-1=x*2^t      a^(n-1)=1(mod n)  ��֤n�ǲ��Ǻ���
//һ���Ǻ�������true,��һ������false
bool check(long long a,long long n,long long x,long long t)
{
    long long ret=pow_mod(a,x,n);
    long long last=ret;
    for(int i=1;i<=t;i++)
    {
        ret=mult_mod(ret,ret,n);
        if(ret==1&&last!=1&&last!=n-1) return true;//����
        last=ret;
    }
    if(ret!=1) return true;
    return false;
}

// Miller_Rabin()�㷨�����ж�
//����������true.(������α�����������ʼ�С)
//��������false;

bool Miller_Rabin(long long n)
{
    if(n<2)return false;
    if(n==2)return true;
    if((n&1)==0) return false;//ż��
    long long x=n-1;
    long long t=0;
    while((x&1)==0){x>>=1;t++;}
    for(int i=0;i<S;i++)
    {
        long long a=rand()%(n-1)+1;//rand()��Ҫstdlib.hͷ�ļ�
        if(check(a,n,x,t))
            return false;//����
    }
    return true;
}
//************************************************
//pollard_rho �㷨�����������ֽ�
//************************************************
long long factor[100];//�������ֽ������շ���ʱ������ģ�
long long ans[300];
ll cnt[300];
int tol;//�������ĸ���������С���0��ʼ

long long gcd(long long a,long long b)
{
    if(a==0)return 1;//???????
    if(a<0) return gcd(-a,b);
    while(b)
    {
        long long t=a%b;
        a=b;
        b=t;
    }
    return a;
}

long long Pollard_rho(long long x,long long c)
{
    long long i=1,k=2;
    long long x0=rand()%x;
    long long y=x0;
    while(1)
    {
        i++;
        x0=(mult_mod(x0,x0,x)+c)%x;
        long long d=gcd(y-x0,x);
        if(d!=1&&d!=x) return d;
        if(y==x0) return x;
        if(i==k){y=x0;k+=k;}
    }
}
//��n���������ӷֽ�
void findfac(long long n)
{
    if(Miller_Rabin(n))//����
    {
        factor[tol++]=n;
        return;
    }
    long long p=n;
    while(p>=n)p=Pollard_rho(p,rand()%(n-1)+1);
    findfac(p);
    findfac(n/p);
}
int l = 0;
bool okk(int x){
    l =0;
    int n = x;
    while(x){
        a[l++] = x&1;
        x>>=1;
    }
    ll base = 1;
    for(int i=2;i<=10;i++){
        ll k = 0;
        base = 1;
        for(int j=0;j<l;j++){
            if(a[j]){
                k += base;
            }
            base = base*i;
        }
        if(k<=10000000){
            if(ok[k])return 0;
        }
        else{
            if(Miller_Rabin(k))return 0;
        }
    }
    return 1;
}
void print(){
    for(int i=l-1;i>=0;i--){
        printf("%d",a[i]);
    }
    for(int i=2;i<=10;i++){
        ll k = 0;
        ll base = 1;
        for(int j=0;j<l;j++){
            if(a[j]) k+=base;
            base *= i;
        }
        tol = 0,findfac(k),printf(" %d",factor[0]);
    }
}
int main()
{
#ifdef LOCAL
	freopen("C:\\Users\\honm\\Desktop\\in.txt", "r", stdin);
	freopen("C:\\Users\\honm\\Desktop\\out.txt","w",stdout);
#endif
    int n,m;
    int t;cin >> t;
    printf("Case #1: \n");
    for(int i=2;i<=10000000;i++){
        if(!vis[i]){
            ok[i] = 1;
            for(int j=i;j<=10000000;j+=i) vis[j] = 1;
        }
    }
    int cnt = 0;
   // cout << Miller_Rabin(1111111111111111);
   // ll i = 1111111111111111;
   while(cin >> n >> m){
        int cnt = 0;
        for(int i=1;i<(1<<n) && m;i++){
            if(i&1 && (i&(1<<(n-1)))){
                if(okk(i)){
                    cnt++;
                  //cout << i << endl;
                   print();
                    m--;
                    printf("\n");
                }
            }
        }
        //cout << cnt << endl;
    }
    return 0;
}
