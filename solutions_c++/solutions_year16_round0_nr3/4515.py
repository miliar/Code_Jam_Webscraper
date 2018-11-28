#include <cstdio>
#include <algorithm>

using namespace std;
#define MAX_PRIME 1000000000
int n,j;
bool sieve[MAX_PRIME];
vector<int> prime;
void genprime(){
    for(int i = 2 ; i < MAX_PRIME ; i ++){
        if(!sieve[i])prime.push_back(i);
        for(int j = 0 ; i*prime[j] < MAX_PRIME ; j ++){
            sieve[i*prime[j]]=true;
            if(i % prime[j] == 0)break;
        }
    }
}
inline bool check(int x){
    return (x&(1<<(n-1)))&&(x&1);
}
int notprime(long long x){
    for(int i = 0 ; ((long long)prime[i])*prime[i]<=x ; i ++){
        if(x%prime[i]==0)return prime[i];
    }
    return -1;
}
int main (){
    genprime();
    int T;
    scanf("%d",&T);
    for(int I=1 ; I <=T ; I ++){
        scanf("%d%d",&n,&j);
        int cnt=0;
        printf("Case #%d:\n",I);
        for(int i = 1<<(n-1) ; i < 1<<n && cnt < j ; i ++){
            if(check(i)){
                vector<int> v;
                for(int b = 2 ; b <= 10 ; b++){
                    int temp=i;
                    long long x=0;
                    for(int k = n-1 ; k >= 0; k --){
                        x*=b;
                        x+=(temp&(1<<k))!=0;
                    }
                    int k=notprime(x);
                    if(k==-1)break;
                    v.push_back(k);
                }
                if(v.size()!=9)continue;
                for(int j = n-1 ; j >=0 ; j --){
                    printf("%d",(i&(1<<j))!=0);
                }
                for(int j = 0 ; j < 9 ; j ++)printf(" %d",v[j]);
                puts("");
                cnt++;
            }
        }
    }

}
