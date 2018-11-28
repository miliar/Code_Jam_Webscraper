#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> II;
typedef vector<II> VII;
typedef vector<VII> VVII;
typedef vector<VI> VVI;

#define INF 2000000000
#define INFLL (1LL<<62)
#define FI first
#define SE second
#define PB push_back
#define SS ({int x;scanf("%d", &x);x;})
#define SSL ({LL x;scanf("%lld", &x);x;})
#define rep(i,n) for(i=0;i<(n);i++)
#define SSF getint()
#define _mp make_pair

inline void _min(int &a,int b)
{
        if(a>b)
                a=b;
}
inline void _max(int &a,int b)
{
        if(a<b)
                a=b;
}

/********************* FAST IO *********************************/

#define BUFSIZE (10000)

char inputbuffer[BUFSIZE];
char *ioptr=inputbuffer+BUFSIZE,*ioend=inputbuffer+BUFSIZE;
int input_eof=0;

#define getchar() ({if (ioptr >= ioend) init_input(); *ioptr++;})
#define eof() (ioptr>=ioend && input_eof)
#define eoln() ({if(ioptr >= ioend) init_input(); *ioptr == '\n';})

void init_input()
{
        if (input_eof)
                return;
        int existing = BUFSIZE - (ioend - inputbuffer);
        memcpy(inputbuffer, ioend, existing);
        int wanted = ioend - inputbuffer;
        int count=fread(inputbuffer + existing, 1, wanted, stdin);
        if (count < wanted)
                input_eof = 1;
        ioend = inputbuffer + BUFSIZE - (wanted - count);
        while (*--ioend > ' ');
        ioend++;
        ioptr=inputbuffer;
}

inline void non_whitespace()
{
        for(;;)
        {
                if(ioptr>=ioend)
                        init_input();
                if(*ioptr>' ')
                        return;
                ioptr++;
        }
}

inline int getint()
{
        non_whitespace();
        int n=0;
        while(*ioptr>' ')
                n=(n<<3)+(n<<1)+*ioptr++-'0';
        ioptr++;
        return n;
}

//******************************** programme code starts here*************************//
int rev(int i){
    int k=0;
    while(i>0){
        k=k*10+i%10;
        i/=10;
    }
return k;
}
int A[1005];
void pre(){
    int i;
    rep(i,1005){
        int j=sqrt(i);
        int k=i-j*j;
       // cout<<k<<" "<<rev(i)<<endl;
        if(i==rev(i) && !k && j==rev(j)){
                A[i]=1;
        }}
    A[0]=0;
    for(i=2;i<1004;i++)
        A[i]+=A[i-1];

}
int main(){
    pre();

    int t=SS,q,a,b;

       rep(q,t){
           a=SS;
           b=SS;
           printf("Case #%d: %d\n",q+1,A[b]-A[a-1]);
       }
     return 0;
     }
