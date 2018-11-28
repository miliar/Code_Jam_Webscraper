#include<stdio.h>
#include<unordered_map>
using namespace std;
long long n,i,x,l,test,ans=0,j,a[50],p[11][50],t[20];
unordered_map<long long,bool> mp;
bool prime(long long num){
    for(long long i = 2; i * i <= num; i++){
        if(num % i == 0){
            t[l - 1] = i;
            return false;
        }
    }
    return true;
}
void search(int num,int i,long long pos){
    if(i > 16) return;
    if(j == 0) return;
    a[i] = num;
    if(i == 16){
        if(num == 0) return;
        l = 0;
        long long k = 0,val=0;
        for(long long x = 2; x <= 10; x++){
            k = 0,val = 0;
            for(long long j = 16; j >= 1; j--){
                val += a[j] * p[x][k],k++;
            }
            t[l++] = val;
            if(prime(val)){
                return;
            }
        }
        printf("%lld ",pos);
        for(long long x = 0; x < l; x++){
          printf("%lld ",t[x]);
        }
        printf("\n");
        mp[pos] = 1,j--;
    }
    search(0,i + 1,pos * 10);
    search(1,i + 1,pos * 10 + 1);
}
int main(){
    
    for(i = 0; i <= 32; i++){
        for(x = 2; x <= 10; x++){
            if(i == 0) p[x][i] = 1;
            else if(i == 1) p[x][i] = x;
            else
                p[x][i] = x * p[x][i - 1];
        }
    }
    freopen("jam.txt","r",stdin);
    freopen("555.txt","w",stdout);
    
    printf("Case #1:\n");
    scanf("%lld",&test);
    scanf("%lld%lld",&n,&j);
    search(1,16 - n + 1,1);


}