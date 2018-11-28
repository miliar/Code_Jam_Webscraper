    #include <iostream>
    #include <cstdio>
    using namespace std;
     
    int main() {
    int T;
    long int A, B, K;
    scanf("%d", &T);
    for(int i=0; i<T; i++) {
    int res = 0;
    printf("Case #%d: ", i+1);
    scanf("%ld %ld %ld", &A, &B, &K);
    for(int i=0; i<A; i++) {
    for(int j=0; j<B; j++) {
    if((i & j) < K) {
    res+=1;
    }
    }
    }
    printf("%d\n", res);
    }
    return 0;
    }
     
