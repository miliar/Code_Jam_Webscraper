#include <bits/stdc++.h>
using namespace std;
vector <int> q;
int k, j;
bool check_prime(long long mask){
    if(mask<=1)return false;
    for(long long i=2;i*i<=mask;i++){
        if(mask%i==0)
            return false;
    }
    return true;
}
long long convert(long long n, int base){
    long long temp=0;
    long long a=1;
    for(int i=0;(1LL<<i)<=n;i++){
        if((1LL<<i)&n)temp+=a;
        a*=base;
    }
    return temp;
}
bool checkpair(long long n){
    for(int i=2;i*i+0LL<=n;i++){
        if(n%i==0){
            q.push_back(i);
            return true;
        }
    }
    return false;
}
bool check(long long mask){
    q.clear();
    for(int i=2;i<=10;i++){
        long long temp = convert(mask, i);
        if(check_prime(temp)|| !checkpair(temp))return false;
    }
    return true;
}
void fillit(int i, long long mask){
    if(i>=k)return;
    if(i==k-1){
        mask = mask|(1LL<<i);
        if(check(mask)){
            printf("%I64d ", convert(mask, 10));
            for (int i=0;i<q.size();i++){
                printf("%d ", q[i]);
            }
            j--;
            if(j==0)exit(0);
            printf("\n");
        }
    }
    if(j==0)return;
    fillit(i+1, mask);
    fillit(i+1, (mask|(1LL<<i)));
}

int main(){
    int T, cases=1;
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    scanf("%d", &T);
    while(T--){
        scanf("%d%d", &k, &j);
        printf("Case #%d:\n", cases++);
        fillit(1, 1LL);
    }
    return 0;
}
