#include<cstdio>
#include<algorithm>
#include<iostream>
#include<map>
using namespace std;
map<int,int>num;
int Case = 1;
int main(){
    int t;
    long long int n;
    #ifndef ONLINE_JUDGE
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    #endif
    scanf("%d",&t);
    while(t--){
        scanf("%lld",&n);
        for(int i=0;i<10;i++)
            num[i] = i;
        long long int k;
        long long int c;
        int count_0 = 0;
        for(k=1;k<=100;k++){
            if(n==0){
                k=100;
                break;
            }
            c = k*n;
            while(c!=0){
                long long int a = c%10;
                for(int i=0;i<10;i++){
                    if(a==num[i]){
                        num[i] = -1;
                        count_0++;
                        break;
                    }
                }
                c = c/10;
            }
            if(count_0==10)
                break;
        }
        if(k==100)
            printf("Case #%d: INSOMNIA\n",Case++);
        else
            printf("Case #%d: %lld\n",Case++,k*n);
    }
    return 0;
}
