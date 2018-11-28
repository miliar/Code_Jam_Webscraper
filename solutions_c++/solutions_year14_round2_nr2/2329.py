#include<cstdio>
#include<bitset>
#include<string>
#include<iostream>
#include<algorithm>
using namespace std;

int A, B, K;
int get(int a, int b){
    bitset<32> s(a), s2(b), ans;
    ans = s&s2;
    string str = ans.to_string();
    int k = 1, answer = 0;
    for(int i = 31; i>=0; i--){
        if(str[i]=='1')
            answer += k;
        k *= 2;
    }
    return answer;
}
int main(){

    int t, ca=1;
    scanf("%d", &t);

    for(; t>0; t--){
        printf("Case #%d: ", ca++);
        scanf("%d%d%d", &A, &B, &K);
        long long ans = 0;
        ans += min(A, K)*B;
        if(A>K){
            ans += (A-K)*min(B, K);
            if(B>K){
                for(int i=K; i<A; i++){
                    for(int j=K; j<B; j++){
                        if(get(i, j)<K)
                            ans++;
                    }
                }
            }
        }
        printf("%lld\n", ans);
    }

    return 0;
}


