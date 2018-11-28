#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<iostream>
#include<sstream>
#include<map>
#include<set>
#include<string>
using namespace std;

#define MAX(a,b) a>b?a:b
#define MIN(a,b) a<b?a:b
#define PI acos(-1.0)
#define SQ(x) ((x)*(x))
#define CUBE(x) ((x)*(x)*(x))
#define MAX_INT 2147483647
#define inf 1<<30
#define FOR(i,a,b) for(i=(a);i<=(b);i++)
#define FORV(i,a,b) for(i=(a);i>=(b);i--)
#define REP(i,n) for(i=0;i<(n);i++)
#define pb push_back
#define pf push_front
#define ppb pop_back
#define ppf pop_front
#define nl printf("\n")
#define set(A,x) memset(A,x,sizeof(A))
#define in(x) scanf("%d",&x)
#define inll(x) scanf("%lld",&x)
#define LL long long
//#define LL __int64
#define MX 100000200

template<class T>inline T _abs(T n){return n<0?-n:n;}
template<class T>inline T _gcd(T a, T b){return b==0?a:_gcd(b,a%b);}
template<class T>inline T _lcm(T a, T b){return a/_gcd(a,b)*b;}

int setb(int N,int pos){return N= N | (1<<pos);}
int resetb(int N,int pos){return N= N & ~(1<<pos);}
bool checkb(int N,int pos){return (bool)(N & (1<<pos));}

bool A[MX];
vector<int>prime;
char binary[100];

void sieve(void)
{
    int i,j;
    int len=sqrt(MX);
    for(i=3;i<=len;i+=2)
    {
        if(A[i]==false)
            for(j=i*i;j<MX;j+=(i+i))
                A[j]=true;//has divisor
    }
    prime.pb(2);
    for(i=3;i<MX;i+=2)
        if(!A[i])
            prime.pb(i);
}

void rev(char *s)
{
    int len = strlen(s);
    for(int i=0,j=len-1;i<len/2;i++,j--)
    {
        swap(s[i],s[j]);
    }
}

void decimanl_to_binary(int n)
{
    int i=0;
    while(n!=0)
    {
        binary[i++] = (n%2)+'0';
        n/=2;
    }
    binary[i++]='\0';
    //printf("before reverse %s\n",binary);
    rev(binary);
    //printf("after reverse %s\n",binary);
}

long long any_to_decimal(char *str, int base)
{
    int l=strlen(str);
    LL num=0;
    int i;
    for(i=0;i<l;i++)
        num = (num*base+ (str[i]-'0'));
    return num;
}


int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output_small_c.txt","w",stdout);
    sieve();
    int test,cases=0;
    int n,j;
    in(test);
    while(test--)
    {
        in(n);
        in(j);
        printf("Case #%d:\n",++cases);
        int num = (1<<(n-1)) + 1;
        //decimanl_to_binary(num);
        //printf("start %d %s\n",num,binary);
        //printf("length %d\n", strlen(binary));
        //printf("%s\n",binary);
        while(j)
        {
            //break;
            if(num%2==0 || A[num]==true)//not prime base 2
            {
                decimanl_to_binary(num);
                //printf("test %s",binary);
                vector<LL> divisor;
                divisor.clear();
                for(int base=2;base<=10;base++)
                {
                    LL new_num = any_to_decimal(binary, base);
                    if(new_num<MX)
                    {
                        if(new_num%2==0 || A[new_num]==true)
                        {
                            for(int i=0;i<prime.size() && prime[i]<new_num;i++)
                                if(new_num%prime[i]==0)
                                {
                                    divisor.pb(prime[i]);
                                    break;
                                }
                        }
                        else
                            break;
                    }
                    else
                    {
                        bool divisor_found = false;
                        int len_new_num = sqrt(new_num);
                        for(int i=0;i<prime.size() && prime[i]<=len_new_num;i++)
                            if(new_num%prime[i]==0)
                            {
                                divisor.pb(prime[i]);
                                divisor_found = true;
                                break;
                            }
                        if(divisor_found==false)
                            break;
                    }
                }
                if(divisor.size()==9)
                {
                    //print
                    printf("%s",binary);
                    for(int i=0;i<divisor.size();i++)
                        printf(" %lld",divisor[i]);
                    nl;
                    j--;
                }
            }


            num+=2;
        }
    }

    return 0;
}
