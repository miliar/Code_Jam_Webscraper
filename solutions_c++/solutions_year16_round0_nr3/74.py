#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

typedef unsigned int uint;

int prime[1000],pn;
bool vst[1000];
void init_prime(){
    memset(vst,0,sizeof(vst));
    pn=0;
    for(int i=2;i<1000;i++) {
        if(vst[i]==false){
            prime[pn++]=i;
            for(int j=i*i;j<1000;j+=i) vst[j]=true;
        }
    }
}

bool fastcheck(uint mask,int n,int div[]){
    int check_prime_num = 20;

    for(int base=2;base<=10;base++){
        int ok_prime = -1;
        for(int p=0;p<check_prime_num;p++){
            int mod = prime[p];
            int lef = 0;
            for(int b=0;b<n;b++){
                lef *= base;
                if((mask>>(n-b-1))&1U) lef++;
                lef %= mod;
            }
            if(lef==0){
                ok_prime = mod;
                break;
            }
        }
        if(ok_prime==-1) return false;
        div[base] = ok_prime;
    }
    return true;
}

/// =========================================
int N,J;
int NUM = 0;
uint ans[1024][11];

void tryFind(int from,int to){
    int div[11];
    for(int test=from;test<to;test++){
        if(NUM>=J) return;
        uint num = (1U<<(N-1))+(((uint)test)<<1)+1U;
        bool ok = fastcheck(num,N,div);
        if(ok){

            ans[NUM][0] = num;
            for(int i=2;i<=10;i++) ans[NUM][i] = div[i];
            NUM++;

        }
    }
}


void solve(int id,int fullnum){
    int UP = 1<<(N-2);
    int s = UP/fullnum * id;
    int e = UP/fullnum * (id+1);
    if(id==fullnum-1) e = UP;
    tryFind(s,e);
}

char b_wd[100];
void print_b(uint x){
    for(int i=0;i<N;i++){
        if((x>>i)&1U) b_wd[N-i-1]='1';
        else  b_wd[N-i-1]='0';
    }
    b_wd[N]=0;
    printf("%s",b_wd);
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    init_prime();

    int T;
    cin>>T;
    for(int cas=1;cas<=T;cas++){
        printf("Case #%d:\n",cas);
        cin>>N>>J;

        solve(0,1);

        for(int i=0;i<J;i++){
            print_b(ans[i][0]);
            for(int ii=2;ii<=10;ii++) printf(" %d",(int)ans[i][ii]);
            cout<<endl;
        }

    }
    return 0;
}
